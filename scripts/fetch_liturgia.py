import os
import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def genera_dati_liturgia():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    oggi_str = datetime.now().strftime("%Y%m%d")
    
    dati = {
        "lodi": "",
        "vespri": "",
        "compieta": "",
        "letture": "",
        "audio_url": ""
    }

    def pulisci_html(soup_elem):
        if not soup_elem:
            return ""
        # Rimuove link di condivisione o stampa
        for tag in soup_elem.find_all(['script', 'style', 'iframe']):
            tag.decompose()
        return str(soup_elem)

    def scarica_pagina(url):
        try:
            r = requests.get(url, headers=headers, timeout=12)
            if r.status_code == 200:
                soup = BeautifulSoup(r.text, 'html.parser')
                content = soup.find('div', class_='entry-content') or soup.find('article') or soup.find('main')
                return soup, content
        except Exception as e:
            print(f"Errore download {url}: {e}")
        return None, None

    # 1. Lodi, Vespri, Compieta
    for ora, key in [("lodi-mattutine", "lodi"), ("vespri", "vespri"), ("compieta", "compieta")]:
        url = f"https://www.chiesacattolica.it/la-liturgia-delle-ore/?data-liturgia={oggi_str}&ora={ora}"
        _, content = scarica_pagina(url)
        if content:
            dati[key] = pulisci_html(content)
        else:
            dati[key] = f"<p>Impossibile caricare {key} per la data odierna.</p>"

    # 2. Letture del giorno + Audio mp3
    url_letture = f"https://www.chiesacattolica.it/liturgia-del-giorno/?data-liturgia={oggi_str}"
    soup_l, content_l = scarica_pagina(url_letture)
    
    if soup_l:
        # Cerca il file audio
        audio_tag = soup_l.find('audio')
        if audio_tag and audio_tag.get('src'):
            dati["audio_url"] = audio_tag['src']
        else:
            source_tag = soup_l.find('source')
            if source_tag and source_tag.get('src'):
                dati["audio_url"] = source_tag['src']
                
    if content_l:
        dati["letture"] = pulisci_html(content_l)
    else:
        dati["letture"] = "<p>Impossibile caricare le Letture della Messa.</p>"

    os.makedirs('dati', exist_ok=True)
    with open('dati/oggi.json', 'w', encoding='utf-8') as f:
        json.dump(dati, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    genera_dati_liturgia()
