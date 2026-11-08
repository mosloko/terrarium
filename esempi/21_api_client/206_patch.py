# API 206 — PATCH aggiorna parzialmente una risorsa (endpoint demo).
import json
import os
from urllib.request import Request, urlopen

BASE = os.getenv("API_BASE_URL", "https://jsonplaceholder.typicode.com").rstrip("/")
resource_id = 1
payload = json.dumps({"title": "Titolo aggiornato"}).encode()
req = Request(f"{BASE}/posts/{resource_id}", data=payload, method="PATCH", headers={"Content-Type": "application/json", "Accept": "application/json"})
if os.getenv("ESEMPIO_RETE") == "1":
    with urlopen(req, timeout=5) as response:
        print(response.status, response.read(500).decode("utf-8", errors="replace"))
else:
    print("PATCH preparata ma non inviata. Endpoint demo può simulare la modifica.")
