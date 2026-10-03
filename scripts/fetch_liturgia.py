import os
import json
import requests
from datetime import datetime

def genera_dati_liturgia():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }
    
    oggi = datetime.now()
    data_iso = oggi.strftime("%Y-%m-%d") # YYYY-MM-DD per API
    data_str = oggi.strftime("%Y%m%d")   # YYYYMMDD
    
    dati = {
        "lodi": "",
        "vespri": "",
        "compieta": "",
        "letture": "",
        "audio_url": ""
    }

    # 1. LETTURE DEL GIORNO (Via API REST Evangelizo / Liturgia)
    try:
        # API ufficiale italiana per il testo delle letture
        url_api_letture = f"https://api.evangelizo.org/v1/it/reading/{data_iso}"
        r = requests.get(url_api_letture, headers=headers, timeout=10)
        
        if r.status_code == 200:
            res = r.json()
            html_letture = ""
            for item in res.get("data", []):
                titolo = item.get("title", "")
                riferimento = item.get("source", "")
                testo = item.get("text", "").replace("\n", "<br>")
                
                html_letture += f"<h3 style='color:#C05A3E; margin-top:15px;'>{titolo}</h3>"
                if riferimento:
                    html_letture += f"<p><em>{riferimento}</em></p>"
                html_letture += f"<p style='margin-top:8px;'>{testo}</p><br>"
            
            dati["letture"] = html_letture
    except Exception as e:
        print(f"Errore API Letture: {e}")

    # Fallback Letture se l'API principale non risponde
    if not dati["letture"]:
        try:
            r_alt = requests.get(f"https://www.lachiesa.it/liturgia/xml/liturgia.php?data={data_str}", headers=headers, timeout=10)
            if r_alt.status_code == 200:
                dati["letture"] = r_alt.text
        except Exception as e:
            print(f"Errore Fallback Letture: {e}")
            dati["letture"] = "<p>Letture della Messa in aggiornamento.</p>"

    # 2. AUDIO DEL VANGELO / LETTURE
    # Feed audio diretto
    dati["audio_url"] = f"https://www.lachiesa.it/liturgia/audio/{data_str}.mp3"

    # 3. LITURGIA DELLE ORE (Lodi, Vespri, Compieta via Feed dati)
    ore_keys = [("lodi", "lodi-mattutine"), ("vespri", "vespri"), ("compieta", "compieta")]
    
    for key, ora_param in ore_keys:
        try:
            # API / Endpoint leggero dedicato per le ore
            url_ora = f"https://www.maranatha.it/Mobile/liturgiaore.asp?data={data_str}&ora={key}"
            r_ora = requests.get(url_ora, headers=headers, timeout=8)
            if r_ora.status_code == 200 and len(r_ora.text) > 200:
                dati[key] = r_ora.text
            else:
                # Sorgente secondaria pulita
                url_sec = f"https://www.chiesacattolica.it/la-liturgia-delle-ore/?data-liturgia={data_str}&ora={ora_param}"
                r_sec = requests.get(url_sec, headers=headers, timeout=8)
                if r_sec.status_code == 200:
                    from bs4 import BeautifulSoup
                    soup = BeautifulSoup(r_sec.text, 'html.parser')
                    for tag in soup.find_all(['script', 'style', 'nav', 'header', 'footer', 'form']):
                        tag.decompose()
                    content = soup.find('div', class_='entry-content') or soup.find('article')
                    if content:
                        dati[key] = str(content)
        except Exception as e:
            print(f"Errore recupero {key}: {e}")
            dati[key] = f"<p>Testo delle {key.capitalize()} non disponibile.</p>"

    # Salva il file JSON pulito
    os.makedirs('dati', exist_ok=True)
    with open('dati/oggi.json', 'w', encoding='utf-8') as f:
        json.dump(dati, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    genera_dati_liturgia()
