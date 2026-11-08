# Esempio 101 — urllib è incluso in Python; questa chiamata richiede rete.
# Per sicurezza non parte senza consenso esplicito e usa un timeout.
import os
from urllib.request import urlopen

if os.getenv("ESEMPIO_RETE") == "1":
    with urlopen("https://example.com", timeout=3) as risposta:
        print(risposta.status, risposta.headers.get("content-type"))
else:
    print("Demo disattivata: imposta ESEMPIO_RETE=1 per autorizzare la richiesta.")
