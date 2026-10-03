import os
import json
import requests
from bs4 import BeautifulSoup

def genera_dati_liturgia():
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    # Struttura base dei dati
    dati = {
        "lodi": "<h3>Lodi Mattutine</h3><p>Testo delle Lodi del giorno in caricamento...</p>",
        "vespri": "<h3>Vespri</h3><p>Testo dei Vespri del giorno in caricamento...</p>",
        "compieta": "<h3>Compieta</h3><p>Testo della Compieta del giorno in caricamento...</p>",
        "letture": "<h3>Letture della Messa</h3><p>Testo delle Letture del giorno in caricamento...</p>",
        "audio_url": "https://www.lachiesa.it/liturgia/audio/oggi.mp3" # Sorgente audio diretta e stabile
    }

    # Assicurati che la cartella dati esista
    os.makedirs('dati', exist_ok=True)
    
    # Salva il file JSON
    with open('dati/oggi.json', 'w', encoding='utf-8') as f:
        json.dump(dati, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    genera_dati_liturgia()
