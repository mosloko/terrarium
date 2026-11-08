# Esempio 125 — Rifiutare campi inattesi può rendere il contratto API più chiaro.
richiesta = {"id": "p1", "importo_cent": 500}
ammessi = {"id", "importo_cent"}
assert richiesta.keys() <= ammessi
print("Campi consentiti")
