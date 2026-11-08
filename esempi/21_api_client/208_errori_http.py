# API 208 — Trattare HTTPError separatamente dagli errori di connessione.
import os
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

BASE = os.getenv("API_BASE_URL", "https://jsonplaceholder.typicode.com").rstrip("/")
if os.getenv("ESEMPIO_RETE") == "1":
    try:
        with urlopen(Request(f"{BASE}/posts/0", headers={"Accept": "application/json"}), timeout=5) as response:
            print("Successo:", response.status)
    except HTTPError as errore:
        # HTTPError è anche una response: leggere un body limitato può aiutare il debug.
        print("Errore HTTP:", errore.code, errore.reason)
        print("Body:", errore.read(1000).decode("utf-8", errors="replace"))
    except URLError as errore:
        print("Errore di rete/DNS:", errore.reason)
else:
    print("Richiesta errore demo disattivata; imposta ESEMPIO_RETE=1.")
