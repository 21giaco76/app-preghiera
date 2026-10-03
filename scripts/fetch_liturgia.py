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

    # Helper per scaricare e pulire il contenuto HTML mantenendo solo il testo formattato
    def estrai_contenuto_pulito(url):
        try:
            r = requests.get(url, headers=headers, timeout=15)
            r.encoding = 'utf-8'
            if r.status_code == 200:
                soup = BeautifulSoup(r.text, 'html.parser')
                
                # Rimuove elementi indesiderati
                for tag in soup.find_all(['script', 'style', 'iframe', 'form', 'nav', 'header', 'footer']):
                    tag.decompose()
                
                # Trova il corpo del testo principale
                contenuto = soup.find('div', class_='entry-content') or \
                            soup.find('div', class_='content-liturgia') or \
                            soup.find('article') or \
                            soup.find('main')
                
                if contenuto:
                    # Pulisce attributi di stile inline per permettere all'app di gestire i font
                    for tag in contenuto.find_all(True):
                        if 'style' in tag.attrs:
                            del tag.attrs['style']
                        if 'class' in tag.attrs:
                            del tag.attrs['class']
                    return str(contenuto)
        except Exception as e:
            print(f"Errore caricamento {url}: {e}")
        return ""

    # 1. Liturgia delle Ore
    ore = [
        ("lodi-mattutine", "lodi"),
        ("vespri", "vespri"),
        ("compieta", "compieta")
    ]

    for ora_param, chiave in ore:
        url = f"https://www.chiesacattolica.it/la-liturgia-delle-ore/?data-liturgia={oggi_str}&ora={ora_param}"
        testo = estrai_contenuto_pulito(url)
        if testo:
            dati[chiave] = testo
        else:
            dati[chiave] = f"<p>Testo delle {chiave.capitalize()} del giorno non disponibile.</p>"

    # 2. Letture della Messa e Audio MP3
    url_letture = f"https://www.chiesacattolica.it/liturgia-del-giorno/?data-liturgia={oggi_str}"
    try:
        r = requests.get(url_letture, headers=headers, timeout=15)
        r.encoding = 'utf-8'
        if r.status_code == 200:
            soup = BeautifulSoup(r.text, 'html.parser')
            
            # Cerca audio MP3
            audio = soup.find('audio')
            if audio and audio.get('src'):
                dati["audio_url"] = audio['src']
            else:
                source = soup.find('source')
                if source and source.get('src'):
                    dati["audio_url"] = source['src']

            # Estrazione testo letture
            for tag in soup.find_all(['script', 'style', 'iframe', 'form', 'nav', 'header', 'footer']):
                tag.decompose()
            contenuto = soup.find('div', class_='entry-content') or soup.find('article') or soup.find('main')
            if contenuto:
                for tag in contenuto.find_all(True):
                    if 'style' in tag.attrs: del tag.attrs['style']
                    if 'class' in tag.attrs: del tag.attrs['class']
                dati["letture"] = str(contenuto)
            else:
                dati["letture"] = "<p>Letture del giorno non disponibili.</p>"
    except Exception as e:
        print(f"Errore Letture: {e}")
        dati["letture"] = "<p>Errore nel caricamento delle Letture del giorno.</p>"

    # Salva il file JSON
    os.makedirs('dati', exist_ok=True)
    with open('dati/oggi.json', 'w', encoding='utf-8') as f:
        json.dump(dati, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    genera_dati_liturgia()
