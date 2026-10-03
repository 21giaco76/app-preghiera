import os
import json
import requests
from datetime import datetime

def genera_dati_liturgia():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }
    
    oggi = datetime.now()
    data_str = oggi.strftime("%Y-%m-%d") # AAAA-MM-GG
    oggi_param = oggi.strftime("%Y%m%d")
    
    dati = {
        "lodi": "",
        "vespri": "",
        "compieta": "",
        "letture": "",
        "audio_url": ""
    }

    # 1. RECUPERO ORE LITURGICHE DA IBREVIARY (API JSON / HTML pulito)
    ore_ibreviary = {
        "lodi": "lodi",
        "vespri": "vespri",
        "compieta": "compieta",
        "letture": "ufficio" # oppure letture della messa
    }

    for chiave, ora_name in ore_ibreviary.items():
        url_ib = f"https://www.ibreviary.com/m2/breviario.php?s={ora_name}&data={data_str}&lang=it"
        try:
            r = requests.get(url_ib, headers=headers, timeout=10)
            if r.status_code == 200:
                dati[chiave] = r.text
        except Exception as e:
            print(f"Errore {chiave}: {e}")

    # 2. RECUPERO LETTURE E AUDIO MP3 DEL GIORNO
    url_messa = f"https://www.ibreviary.com/m2/messa.php?data={data_str}&lang=it"
    try:
        r_messa = requests.get(url_messa, headers=headers, timeout=10)
        if r_messa.status_code == 200:
            dati["letture"] = r_messa.text
    except Exception as e:
        print(f"Errore Messa: {e}")

    # Fallback Audio MP3 stabile per le letture del giorno
    dati["audio_url"] = f"https://www.lachiesa.it/liturgia/audio/{oggi_param}.mp3"

    # Salva il file JSON
    os.makedirs('dati', exist_ok=True)
    with open('dati/oggi.json', 'w', encoding='utf-8') as f:
        json.dump(dati, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    genera_dati_liturgia()
