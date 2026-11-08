# API 209 — Validare status, Content-Type e JSON della response.
import json
import os
from urllib.request import Request, urlopen

BASE = os.getenv("API_BASE_URL", "https://jsonplaceholder.typicode.com").rstrip("/")
if os.getenv("ESEMPIO_RETE") == "1":
    with urlopen(Request(f"{BASE}/posts/1", headers={"Accept": "application/json"}), timeout=5) as response:
        content_type = response.headers.get_content_type()
        if response.status != 200:
            raise RuntimeError(f"Status inatteso: {response.status}")
        if content_type != "application/json":
            raise ValueError(f"Content-Type inatteso: {content_type}")
        dato = json.load(response)
        print("Risposta JSON valida; campi:", sorted(dato))
else:
    print("Validazione reale disattivata; usare ESEMPIO_RETE=1 per una chiamata.")
