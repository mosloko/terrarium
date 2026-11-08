# Esempio 129 — Normalizzare spazi ai bordi prima di validare un identificatore.
riferimento = "  DEMO-12  ".strip()
assert riferimento and len(riferimento) <= 40
print(riferimento)
