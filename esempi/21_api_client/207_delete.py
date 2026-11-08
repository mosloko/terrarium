# API 207 — DELETE: usare solo su risorse di test autorizzate.
import os
from urllib.request import Request, urlopen

BASE = os.getenv("API_BASE_URL", "https://jsonplaceholder.typicode.com").rstrip("/")
req = Request(f"{BASE}/posts/1", method="DELETE", headers={"Accept": "application/json"})
if os.getenv("ESEMPIO_RETE") == "1":
    with urlopen(req, timeout=5) as response:
        print("HTTP:", response.status)
else:
    print("DELETE non inviato: abilita la rete solo verso un ambiente di test.")
