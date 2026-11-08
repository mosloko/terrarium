# Esempio 106 — Le intestazioni identificano il formato del corpo.
from urllib.request import Request
req = Request("https://example.com", headers={"Accept": "application/json"})
print(req.get_header("Accept"))
