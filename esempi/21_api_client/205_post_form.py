# API 205 — POST form URL-encoded per API che non accettano JSON.
import os
from urllib.parse import urlencode
from urllib.request import Request, urlopen

BASE = os.getenv("API_BASE_URL", "https://jsonplaceholder.typicode.com").rstrip("/")
form = urlencode({"titolo": "demo", "stato": "bozza"}).encode("utf-8")
req = Request(f"{BASE}/posts", data=form, method="POST", headers={"Content-Type": "application/x-www-form-urlencoded", "Accept": "application/json"})
print("Body form:", form.decode())
if os.getenv("ESEMPIO_RETE") == "1":
    with urlopen(req, timeout=5) as response:
        print("HTTP:", response.status, response.read(500).decode("utf-8", errors="replace"))
else:
    print("Richiesta form preparata ma non inviata.")
