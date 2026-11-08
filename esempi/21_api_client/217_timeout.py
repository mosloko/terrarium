# API 217 — Timeout: impostare limiti espliciti per ogni richiesta.
import os
from urllib.request import urlopen

URL = os.getenv("API_BASE_URL", "https://jsonplaceholder.typicode.com") + "/posts/1"
TIMEOUT_SECONDI = 3
if os.getenv("ESEMPIO_RETE") == "1":
    with urlopen(URL, timeout=TIMEOUT_SECONDI) as response:
        print("HTTP:", response.status)
else:
    print("Timeout configurato:", TIMEOUT_SECONDI, "secondi; rete disattivata.")
