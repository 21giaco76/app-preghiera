import urllib.request
import re
import datetime

def aggiorna():
    print("Inizio ricerca audio del giorno...")
    
    # URL della pagina delle letture con audio su Vatican News / Liturgia del Giorno
    url_pagina = "https://www.vaticannews.va/it/vangelo-del-giorno-e-parola-del-giorno.html"
    
    req = urllib.request.Request(
        url_pagina, 
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    )
    
    try:
        html = urllib.request.urlopen(req).read().decode('utf-8')
        # Cerca i link .mp3 all'interno della pagina
        mp3_links = re.findall(r'https?://[^\s\'"]+\.mp3', html)
        
        if not mp3_links:
            print("Nessun file audio MP3 trovato nella pagina.")
            return

        nuovo_audio_url = mp3_links[0]
        print(f"Audio trovato: {nuovo_audio_url}")

        # Legge contenuti.js
        with open("contenuti.js", "r", encoding="utf-8") as f:
            contenuto = f.read()

        # Sostituisce la riga audioLetture
        nuovo_contenuto = re.sub(
            r'audioLetture:\s*".*?"',
            f'audioLetture: "{nuovo_audio_url}"',
            contenuto
        )

        # Salva le modifiche in contenuti.js
        with open("contenuti.js", "w", encoding="utf-8") as f:
            f.write(nuovo_contenuto)
            
        print("contenuti.js aggiornato con successo!")

    except Exception as e:
        print(f"Errore durante l'aggiornamento: {e}")

if __name__ == "__main__":
    aggiorna()
