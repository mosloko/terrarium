# API 210 — Leggere body con limite massimo per evitare consumi incontrollati.
import os
from urllib.request import Request, urlopen

BASE = os.getenv("API_BASE_URL", "https://jsonplaceholder.typicode.com").rstrip("/")
LIMITE = 64 * 1024
if os.getenv("ESEMPIO_RETE") == "1":
    with urlopen(Request(f"{BASE}/posts/1"), timeout=5) as response:
        body = response.read(LIMITE + 1)
        if len(body) > LIMITE:
            raise ValueError("Response oltre il limite consentito")
        print("Byte letti:", len(body))
else:
    print("Lettura disattivata; il client legge al massimo LIMITE+1 byte.")
