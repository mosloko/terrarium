# Esempio 130 — Evitare di includere dati sensibili nei messaggi di errore.
def messaggio_errore(codice):
    return {"errore": codice, "dettagli": "Richiesta non elaborabile"}
print(messaggio_errore("INPUT_NON_VALIDO"))
