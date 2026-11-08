# API 201 — GET con header, query string e path parameter.
# Solo rete opt-in: ESEMPIO_RETE=1 python questo_file.py
import json
import os
from urllib.parse import urlencode
from urllib.request import Request, urlopen

BASE = os.getenv("API_BASE_URL", "https://jsonplaceholder.typicode.com").rstrip("/")
if os.getenv("ESEMPIO_RETE") == "1":
    user_id = 1  # Path parameter: identifica la risorsa richiesta.
    query = urlencode({"_limit": 3, "userId": user_id})  # Query string: filtra/pagina.
    req = Request(f"{BASE}/posts?{query}", headers={"Accept": "application/json", "User-Agent": "python-api-learning/1.0"})
    with urlopen(req, timeout=5) as response:
        print("HTTP:", response.status, "Content-Type:", response.headers.get("Content-Type"))
        print(json.load(response))
else:
    print("Demo senza rete. Imposta ESEMPIO_RETE=1 per chiamare API_BASE_URL.")
