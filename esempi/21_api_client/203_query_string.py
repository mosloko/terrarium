# API 203 — Query string con valori ripetuti e caratteri speciali.
import os
from urllib.parse import urlencode
from urllib.request import Request, urlopen

BASE = os.getenv("API_BASE_URL", "https://jsonplaceholder.typicode.com").rstrip("/")
params = [("tag", "conto corrente"), ("tag", "demo"), ("page", "1")]
url = f"{BASE}/posts?{urlencode(params)}"
print("URL:", url)
if os.getenv("ESEMPIO_RETE") == "1":
    with urlopen(Request(url, headers={"Accept": "application/json"}), timeout=5) as response:
        print("HTTP:", response.status)
else:
    print("Rete disattivata; osserva la query string codificata.")
