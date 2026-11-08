# Esempio 105 — Preparare una richiesta POST JSON senza inviarla.
import json
from urllib.request import Request
corpo = json.dumps({"tipo": "demo", "importo_cent": 1250}).encode("utf-8")
richiesta = Request("https://example.com/api", data=corpo, headers={"Content-Type": "application/json"}, method="POST")
print(richiesta.method, richiesta.full_url, richiesta.get_header("Content-type"), len(corpo))
