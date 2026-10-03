import os
import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def genera_dati_liturgia():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    oggi = datetime.now()
    data_str = oggi.strftime("%Y-%m-%d")  # Formato YYYY-MM-DD

    dati = {
        "lodi": "",
        "vespri": "",
        "compieta": "",
        "letture": "",
        "audio_url": ""  # Lasciato vuoto per ora
    }

    # Funzione per isolare solo il testo delle preghiere e rimuovere i menu di iBreviary
    def pulisci_e_estrai_testo(raw_html):
        if not raw_html:
            return ""
        soup = BeautifulSoup(raw_html, 'html.parser')
        
        # 1. Rimuove elementi di disturbo (script, stili, link, immagini, form)
        for elem in soup.find_all(['script', 'style', 'iframe', 'form', 'img', 'a', 'nav', 'header', 'footer']):
            elem.decompose()
            
        # 2. Rimuove specifici blocchi di menu o intestazioni di iBreviary
        for menu in soup.find_all('div', class_=['top_menu', 'header', 'navbar', 'menu', 'breadcrumb', 'nav_menu']):
            menu.decompose()
            
        # 3. Cerca il contenitore principale dove risiede il testo liturgico
        contenuto = soup.find('div', id='content') or soup.find('div', class_='text') or soup.find('body')
        
        if contenuto:
            # Elimina eventuali menu interni residui
            for sub_menu in contenuto.find_all('div', class_=['menu', 'nav']):
                sub_menu.decompose()
            
            # Pulisce tutti gli stili inline così il testo risponde ai tasti A- e A+ dell'app
            for tag in contenuto.find_all(True):
                if 'style' in tag.attrs:
                    del tag.attrs['style']
                if 'class' in tag.attrs:
                    del tag.attrs['class']
                    
            return str(contenuto)
            
        return ""

    # 1. RECUPERO ORE LITURGICHE (Lodi, Vespri, Compieta)
    ore_map = {
        "lodi": "lodi",
        "vespri": "vespri",
        "compieta": "compieta"
    }

    for chiave, ora_name in ore_map.items():
        url = f"https://www.ibreviary.com/m2/breviario.php?s={ora_name}&data={data_str}&lang=it"
        try:
            r = requests.get(url, headers=headers, timeout=12)
            if r.status_code == 200:
                testo = pulisci_e_estrai_testo(r.text)
                dati[chiave] = testo if testo else f"<p>Testo per {chiave.capitalize()} non disponibile.</p>"
            else:
                dati[chiave] = f"<p>Impossibile caricare {chiave.capitalize()}.</p>"
        except Exception as e:
            print(f"Errore {chiave}: {e}")
            dati[chiave] = f"<p>Errore nel caricamento di {chiave.capitalize()}.</p>"

    # 2. RECUPERO LETTURE DELLA MESSA
    url_messa = f"https://www.ibreviary.com/m2/messa.php?data={data_str}&lang=it"
    try:
        r_messa = requests.get(url_messa, headers=headers, timeout=12)
        if r_messa.status_code == 200:
            testo_m = pulisci_e_estrai_testo(r_messa.text)
            dati["letture"] = testo_m if testo_m else "<p>Letture del giorno non disponibili.</p>"
        else:
            dati["letture"] = "<p>Impossibile caricare le Letture della Messa.</p>"
    except Exception as e:
        print(f"Errore Letture: {e}")
        dati["letture"] = "<p>Errore nel caricamento delle Letture del giorno.</p>"

    # Salva il file JSON aggiornato
    os.makedirs('dati', exist_ok=True)
    with open('dati/oggi.json', 'w', encoding='utf-8') as f:
        json.dump(dati, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    genera_dati_liturgia()
