import os
import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def genera_dati_liturgia():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    # Data odierna YYYYMMDD
    oggi_str = datetime.now().strftime("%Y%m%d")
    
    dati = {
        "lodi": "",
        "vespri": "",
        "compieta": "",
        "letture": "",
        "audio_url": ""
    }

    # Helper per scaricare la liturgia
    def scarica_ora(ora_nome):
        url = f"https://www.chiesacattolica.it/la-liturgia-delle-ore/?data-liturgia={oggi_str}&ora={ora_nome}"
        try:
            r = requests.get(url, headers=headers, timeout=10)
            if r.status_code == 200:
                soup = BeautifulSoup(r.text, 'html.parser')
                content = soup.find('div', class_='entry-content') or soup.find('article')
                if content:
                    return str(content)
        except Exception as e:
            print(f"Errore {ora_nome}: {e}")
        return f"<p>Impossibile caricare {ora_nome} per il giorno corrente.</p>"

    print("Download Lodi...")
    dati["lodi"] = scarica_ora("lodi-mattutine")
    
    print("Download Vespri...")
    dati["vespri"] = scarica_ora("vespri")
    
    print("Download Compieta...")
    dati["compieta"] = scarica_ora("compieta")

    # Download Letture del giorno + Audio
    print("Download Letture...")
    try:
        url_letture = f"https://www.chiesacattolica.it/liturgia-del-giorno/?data-liturgia={oggi_str}"
        r = requests.get(url_letture, headers=headers, timeout=10)
        if r.status_code == 200:
            soup = BeautifulSoup(r.text, 'html.parser')
            
            # Cerca il file audio mp3
            audio_tag = soup.find('audio')
            if audio_tag and audio_tag.get('src'):
                dati["audio_url"] = audio_tag['src']
            else:
                source_tag = soup.find('source', type='audio/mpeg')
                if source_tag and source_tag.get('src'):
                    dati["audio_url"] = source_tag['src']
            
            content = soup.find('div', class_='entry-content') or soup.find('article')
            if content:
                dati["letture"] = str(content)
    except Exception as e:
        print(f"Errore Letture: {e}")
        dati["letture"] = "<p>Impossibile caricare le Letture del giorno.</p>"

    # Assicurati che la cartella dati esista
    os.makedirs('dati', exist_ok=True)

    # Salva il file JSON
    with open('dati/oggi.json', 'w', encoding='utf-8') as f:
        json.dump(dati, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    genera_dati_liturgia()
