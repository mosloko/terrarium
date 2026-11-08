# Esempio 102 — Leggere una risposta JSON da un servizio remoto (solo su consenso).
import json
import os
from urllib.request import urlopen

url = os.getenv("API_URL", "https://example.com")
if os.getenv("ESEMPIO_RETE") == "1":
    with urlopen(url, timeout=3) as risposta:
        dati = json.load(risposta)
        print("HTTP", risposta.status, "tipo dati:", type(dati).__name__)
else:
    print("Nessuna rete: configura ESEMPIO_RETE=1 e API_URL con un endpoint di test.")
