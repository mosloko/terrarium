# Esempio 123 — Controllare i campi richiesti prima di elaborare dati.
dati = {"id": "x1", "importo_cent": 500}
richiesti = {"id", "importo_cent"}
assert richiesti <= dati.keys()
print("Campi obbligatori presenti")
