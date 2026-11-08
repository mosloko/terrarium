# API 204 — POST JSON: serializzare il body e dichiarare Content-Type.
import json
import os
from urllib.request import Request, urlopen

BASE = os.getenv("API_BASE_URL", "https://jsonplaceholder.typicode.com").rstrip("/")
payload = {"title": "Esempio didattico", "body": "Dati fittizi", "userId": 1}
body = json.dumps(payload).encode("utf-8")
req = Request(f"{BASE}/posts", data=body, method="POST", headers={"Content-Type": "application/json; charset=utf-8", "Accept": "application/json"})
print("Body JSON:", body.decode())
if os.getenv("ESEMPIO_RETE") == "1":
    with urlopen(req, timeout=5) as response:
        print("HTTP:", response.status, json.load(response))
else:
    print("POST non inviato. Imposta ESEMPIO_RETE=1 per autorizzare la chiamata.")
