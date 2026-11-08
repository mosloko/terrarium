# Esempio 79 — json.dumps converte dati Python in testo JSON.
import json
dati = {"nome": "Ada", "attiva": True}
print(json.dumps(dati, ensure_ascii=False))
