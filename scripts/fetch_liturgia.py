import os
import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def genera_dati_liturgia():
    # Sessione per mantenere i cookie di navigazione (fondamentale per saltare l'Invitatorio)
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept-Language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7'
    })
    
    oggi_str = datetime.now().strftime("%Y%m%d")
    
    dati = {
        "lodi": "",
        "vespri": "",
        "compieta": "",
        "letture": "",
        "audio_url": ""
    }

    def pulisci_html(elem):
        if not elem:
            return ""
        # Rimuove elementi grafici, pulsanti di stampa/condivisione e script
        for tag in elem.find_all(['script', 'style', 'iframe', 'form', 'nav', 'footer']):
            tag.decompose()
        
        # Pulisce gli attributi inline lasciando che sia il CSS dell'app a formattare
        for tag in elem.find_all(True):
            if 'style' in tag.attrs:
                del tag.attrs['style']
            if 'class' in tag.attrs:
                del tag.attrs['class']
                
        return str(elem)

    # 1. SCARICAMENTO ORE LITURGICHE (Lodi, Vespri, Compieta)
    ore_map = [
        ("lodi-mattutine", "lodi"),
        ("vespri", "vespri"),
        ("compieta", "compieta")
    ]

    for ora_param, chiave in ore_map:
        url = f"https://www.chiesacattolica.it/la-liturgia-delle-ore/?data-liturgia={oggi_str}&ora={ora_param}"
        try:
            r = session.get(url, timeout=12)
            if r.status_code == 200:
                soup = BeautifulSoup(r.text, 'html.parser')
                
                # Rimuove l'invitatorio se presente in cima per Vespri e Compieta
                invitatorio = soup.find('div', id='invitatorio')
                if invitatorio:
                    invitatorio.decompose()

                contenuto = soup.find('div', class_='entry-content') or \
                            soup.find('div', class_='content-liturgia') or \
                            soup.find('article')
                
                if contenuto:
                    dati[chiave] = pulisci_html(contenuto)
                else:
                    dati[chiave] = f"<p>Impossibile caricare il testo di {chiave.capitalize()}.</p>"
        except Exception as e:
            print(f"Errore caricamento {chiave}: {e}")
            dati[chiave] = f"<p>Errore durante il recupero di {chiave.capitalize()}.</p>"

    # 2. SCARICAMENTO LETTURE E AUDIO MP3
    url_letture = f"https://www.chiesacattolica.it/liturgia-del-giorno/?data-liturgia={oggi_str}"
    try:
        r = session.get(url_letture, timeout=12)
        if r.status_code == 200:
            soup = BeautifulSoup(r.text, 'html.parser')
            
            # Cerca audio MP3
            audio_tag = soup.find('audio')
            if audio_tag and audio_tag.get('src'):
                dati["audio_url"] = audio_tag['src']
            else:
                source_tag = soup.find('source')
                if source_tag and source_tag.get('src'):
                    dati["audio_url"] = source_tag['src']
                else:
                    for a in soup.find_all('a', href=True):
                        if a['href'].endswith('.mp3'):
                            dati["audio_url"] = a['href']
                            break

            # Cerca testo delle Letture
            contenuto_l = soup.find('div', class_='entry-content') or \
                          soup.find('div', class_='liturgia-giorno') or \
                          soup.find('article')
                          
            if contenuto_l:
                dati["letture"] = pulisci_html(contenuto_l)
            else:
                dati["letture"] = "<p>Testo delle Letture non trovato.</p>"
    except Exception as e:
        print(f"Errore Letture: {e}")
        dati["letture"] = "<p>Errore nel caricamento delle Letture del giorno.</p>"

    # Salva il file JSON
    os.makedirs('dati', exist_ok=True)
    with open('dati/oggi.json', 'w', encoding='utf-8') as f:
        json.dump(dati, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    genera_dati_liturgia()
