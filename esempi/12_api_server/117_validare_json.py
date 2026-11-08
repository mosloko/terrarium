# Esempio 117 — Validare JSON e gestire input malformato.
import json
body = '{"valore": 3}'
try:
    dato = json.loads(body)
except json.JSONDecodeError:
    print("Richiesta non valida")
else:
    print("JSON valido:", dato)
