# API 213 — Bearer token da variabile d'ambiente (mai hardcodato o stampato).
import os
from urllib.request import Request, urlopen

BASE = os.getenv("API_BASE_URL", "https://jsonplaceholder.typicode.com").rstrip("/")
token = os.getenv("API_TOKEN")
if not token:
    print("API_TOKEN assente: nessun header Authorization inviato.")
else:
    req = Request(f"{BASE}/posts/1", headers={"Authorization": f"Bearer {token}", "Accept": "application/json"})
    print("Header Authorization preparato senza mostrare il segreto.")
    if os.getenv("ESEMPIO_RETE") == "1":
        # Configura API_BASE_URL solo verso il servizio autorizzato per quel token.
        with urlopen(req, timeout=5) as response:
            print("HTTP:", response.status)
    else:
        print("Chiamata disattivata. Non inviare token a servizi non autorizzati.")
