# API 211 — Impostare headers Accept, User-Agent e request/correlation ID.
import os
import uuid
from urllib.request import Request, urlopen

BASE = os.getenv("API_BASE_URL", "https://jsonplaceholder.typicode.com").rstrip("/")
headers = {"Accept": "application/json", "User-Agent": "python-api-learning/1.0", "X-Request-ID": str(uuid.uuid4())}
req = Request(f"{BASE}/posts/1", headers=headers)
print("Headers inviati:", sorted(headers))
if os.getenv("ESEMPIO_RETE") == "1":
    with urlopen(req, timeout=5) as response:
        print("HTTP:", response.status, "request id:", headers["X-Request-ID"])
else:
    print("Richiesta non inviata; non includere dati personali negli header di correlazione.")
