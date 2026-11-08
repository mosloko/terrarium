# API 215 — Paginazione: seguire una pagina alla volta e imporre un limite.
# Questa demo mostra la costruzione delle query, senza inviare richieste.
from urllib.parse import urlencode
BASE = "https://api.example.test/movimenti"
limite_pagine = 3
for pagina in range(1, limite_pagine + 1):
    print(f"{BASE}?{urlencode({'page': pagina, 'page_size': 50})}")
