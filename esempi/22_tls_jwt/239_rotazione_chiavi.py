# JWT/JWS 239 — Rotazione: usare kid per scegliere una chiave pubblica da un key set fidato.
# Esempio concettuale; la cache e la distribuzione delle chiavi dipendono dal provider.
chiavi_fidate = {"key-2026-a": "<chiave pubblica caricata da configurazione fidata>"}
kid = "key-2026-a"
chiave = chiavi_fidate.get(kid)
if chiave is None:
    print("Chiave sconosciuta: rifiutare token")
else:
    print("Chiave trovata; verificare la firma prima di usare i claim.")
