import os
import json
import requests
from datetime import datetime

def genera_dati_liturgia():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }
    
    # Formato data per API Evangelizo: YYYY-MM-DD
    oggi = datetime.now()
    data_iso = oggi.strftime("%Y-%m-%d")
    data_str = oggi.strftime("%Y%m%d")
    
    dati = {
        "lodi": "",
        "vespri": "",
        "compieta": "",
        "letture": "",
        "audio_url": ""
    }

    # 1. API LETTURE DELLA MESSA (Evangelizo API REST JSON)
    try:
        url_api = f"https://api.evangelizo.org/v1/it/reading/{data_iso}"
        r = requests.get(url_api, headers=headers, timeout=10)
        
        if r.status_code == 200:
            res = r.json()
            html_letture = ""
            
            # L'API restituisce un array 'data' con le varie letture (Prima Lettura, Salmo, Vangelo)
            for item in res.get("data", []):
                titolo = item.get("title", "")
                riferimento = item.get("source", "")
                testo = item.get("text", "").replace("\r\n", "<br>").replace("\n", "<br>")
                
                if titolo:
                    html_letture += f"<h3 style='color:#C05A3E; margin-top:15px;'>{titolo}</h3>"
                if riferimento:
                    html_letture += f"<p style='color:#8C827A; font-style:italic;'>{riferimento}</p>"
                if testo:
                    html_letture += f"<p style='margin-top:8px;'>{testo}</p><br>"
            
            dati["letture"] = html_letture
    except Exception as e:
        print(f"Errore API Letture: {e}")

    # Fallback semplice se l'API non restituisce dati
    if not dati["letture"]:
        dati["letture"] = "<p>Letture della Messa momentaneamente non disponibili.</p>"

    # 2. LINK AUDIO DIRETTO (Standard MP3)
    dati["audio_url"] = f"https://www.lachiesa.it/liturgia/audio/{data_str}.mp3"

    # 3. API LITURGIA DELLE ORE (API JSON)
    # Piattaforma API per le ore liturgiche in formato JSON
    for chiave in ["lodi", "vespri", "compieta"]:
        try:
            url_ora = f"https://api.evangelizo.org/v1/it/liturgyofhours/{data_iso}/{chiave}"
            r_ora = requests.get(url_ora, headers=headers, timeout=10)
            if r_ora.status_code == 200:
                res_ora = r_ora.json()
                dati[chiave] = res_ora.get("data", {}).get("text", "")
        except Exception as e:
            print(f"Errore API {chiave}: {e}")

    # Salva il file JSON pulito
    os.makedirs('dati', exist_ok=True)
    with open('dati/oggi.json', 'w', encoding='utf-8') as f:
        json.dump(dati, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    genera_dati_liturgia()
