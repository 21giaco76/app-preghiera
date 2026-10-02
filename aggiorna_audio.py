import urllib.request
import re
import datetime

def aggiorna():
    print("Inizio ricerca audio del giorno da Vatican News...")
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    }
    
    nuovo_audio_url = ""
    
    # Sorgenti da scansione in ordine di affidabilità
    urls_sorgenti = [
        "https://www.vaticannews.va/it/vangelo-del-giorno-e-parola-del-giorno.html",
        "https://www.vaticannews.va/it/vangelo-del-giorno-e-parola-del-giorno.rss.xml",
        "https://www.vaticannews.va/it/epg.podcast.giorno.html"
    ]

    # Pattern per catturare i file mp3 di Vatican News (come quello estratto da DevTools)
    pattern_media = r'https?://media\.vaticannews\.va/media2/audio/[^\s\'"\\]+\.mp3'
    pattern_generico = r'https?://[^\s\'"\\]+\.mp3'

    for url in urls_sorgenti:
        try:
            print(f"Scansione sorgente: {url}")
            req = urllib.request.Request(url, headers=headers)
            html = urllib.request.urlopen(req).read().decode('utf-8')

            # 1. Cerca il pattern specifico dei server media2 di Vatican News
            trovati = re.findall(pattern_media, html)
            if trovati:
                nuovo_audio_url = trovati[0]
                break

            # 2. Se non trova il dominio specifico, cerca qualsiasi mp3
            trovati_generici = re.findall(pattern_generico, html)
            if trovati_generici:
                nuovo_audio_url = trovati_generici[0]
                break

        except Exception as e:
            print(f"Errore su {url}: {e}")

    if not nuovo_audio_url:
        print("ATTENZIONE: Nessun file audio MP3 trovato. Il file contenuti.js non verrà modificato.")
        return

    print(f"Audio trovato con successo: {nuovo_audio_url}")

    # Aggiornamento del file contenuti.js
    nome_file_js = "contenuti.js"

    try:
        with open(nome_file_js, "r", encoding="utf-8") as f:
            contenuto = f.read()

        # Sovrascrive il parametro audioLetture mantenendo intatta la struttura
        nuovo_contenuto = re.sub(
            r'audioLetture:\s*".*?"',
            f'audioLetture: "{nuovo_audio_url}"',
            contenuto
        )

        with open(nome_file_js, "w", encoding="utf-8") as f:
            f.write(nuovo_contenuto)
            
        print(f"File {nome_file_js} aggiornato con successo!")

    except Exception as e:
        print(f"Errore durante la scrittura su {nome_file_js}: {e}")

if __name__ == "__main__":
    aggiorna()
