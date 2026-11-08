# API 202 — Costruire un path parameter codificando caratteri speciali.
import os
from urllib.parse import quote
from urllib.request import Request, urlopen

BASE = os.getenv("API_BASE_URL", "https://jsonplaceholder.typicode.com").rstrip("/")
resource_id = "post/1"  # Esempio: slash nel valore va codificato nel segmento.
segmento = quote(resource_id, safe="")
url = f"{BASE}/posts/{segmento}"
print("URL composto:", url)
if os.getenv("ESEMPIO_RETE") == "1":
    with urlopen(Request(url, headers={"Accept": "application/json"}), timeout=5) as response:
        print(response.status, response.read(500).decode("utf-8", errors="replace"))
else:
    print("Chiamata disattivata: imposta ESEMPIO_RETE=1.")
