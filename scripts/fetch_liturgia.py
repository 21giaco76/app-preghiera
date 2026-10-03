import os
import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def genera_dati_liturgia():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    # Formato data per lachiesa.it: AAAAMMGG
    oggi = datetime.now()
    data_path = oggi.strftime("%Y%m%d")
    
    dati = {
        "lodi": "",
        "vespri": "",
        "compieta": "",
        "letture": "",
        "audio_url": ""
    }

    def estrai_testo_pulito(url):
        try:
            r = requests.get(url, headers=headers, timeout=10)
            r.encoding = 'utf-8'
            if r.status_code == 200:
                soup = BeautifulSoup(r.text, 'html.parser')
                
                # Rimuove elementi grafici, menu e script
                for tag in soup.find_all(['script', 'style', 'iframe', 'form', 'img', 'a', 'nav']):
                    tag.decompose()
                
                # Cerca il blocco di testo principale
                main_box = soup.find('div', id='content') or soup.find('body')
                if main_box:
                    return str(main_box)
        except Exception as e:
            print(f"Errore su {url}: {e}")
        return ""

    # 1. Recupero Letture della Messa e Audio MP3 da lachiesa.it
    url_letture = f"https://www.lachiesa.it/liturgia/{data_path}.html"
    try:
        r = requests.get(url_letture, headers=headers, timeout=10)
        r.encoding = 'utf-8'
        if r.status_code == 200:
            soup = BeautifulSoup(r.text, 'html.parser')
            
            # Cerca il file audio MP3
            for a in soup.find_all('a', href=True):
                if '.mp3' in a['href']:
                    dati["audio_url"] = a['href'] if a['href'].startswith('http') else f"https://www.lachiesa.it{a['href']}"
                    break
            if not dati["audio_url"]:
                audio_tag = soup.find('audio')
                if audio_tag and audio_tag.get('src'):
                    dati["audio_url"] = audio_tag['src']

            # Pulisce e assegna il testo
            for tag in soup.find_all(['script', 'style', 'iframe', 'form', 'nav']):
                tag.decompose()
            body_content = soup.find('body')
            if body_content:
                dati["letture"] = str(body_content)
    except Exception as e:
        print(f"Errore Letture: {e}")
        dati["letture"] = "<p>Impossibile caricare le Letture del giorno.</p>"

    # 2. Recupero Lodi, Vespri, Compieta da sorgente alternativa leggera
    # Utilizziamo le pagine dedicate della Liturgia delle Ore
    ore_urls = {
        "lodi": f"https://www.lachiesa.it/liturgia/ore/{data_path}_lodi.html",
        "vespri": f"https://www.lachiesa.it/liturgia/ore/{data_path}_vespri.html",
        "compieta": f"https://www.lachiesa.it/liturgia/ore/{data_path}_compieta.html"
    }

    for chiave, url in ore_urls.items():
        testo = estrai_testo_pulito(url)
        if testo:
            dati[chiave] = testo
        else:
            # Fallback se la pagina specifica dell'ora non è direttamente raggiungibile
            dati[chiave] = f"<p>Testo delle {chiave.capitalize()} del giorno in aggiornamento.</p>"

    # Salva il file JSON
    os.makedirs('dati', exist_ok=True)
    with open('dati/oggi.json', 'w', encoding='utf-8') as f:
        json.dump(dati, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    genera_dati_liturgia()
