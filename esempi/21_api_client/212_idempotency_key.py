# API 212 — Idempotency-Key per rendere sicuri i retry di una POST, se il server la supporta.
import json
import os
import uuid
from urllib.request import Request, urlopen

BASE = os.getenv("API_BASE_URL", "https://jsonplaceholder.typicode.com").rstrip("/")
chiave_idempotenza = str(uuid.uuid4())  # Riutilizzare la stessa chiave per retry della stessa operazione.
body = json.dumps({"title": "demo", "userId": 1}).encode()
req = Request(f"{BASE}/posts", data=body, method="POST", headers={"Content-Type": "application/json", "Idempotency-Key": chiave_idempotenza})
print("Chiave generata:", chiave_idempotenza)
if os.getenv("ESEMPIO_RETE") == "1":
    with urlopen(req, timeout=5) as response:
        print("HTTP:", response.status)
else:
    print("POST non inviata. Una chiave funziona solo se il servizio implementa idempotenza.")
