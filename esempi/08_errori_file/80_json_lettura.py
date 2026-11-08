# Esempio 80 — json.loads converte testo JSON in dati Python.
import json
testo = '{"nome": "Ada", "anni": 36}'
print(json.loads(testo)["nome"])
