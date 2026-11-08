# mTLS/JWT/JWE 240 — Checklist didattica per integrazioni sicure.
checklist = [
    "certificati client e CA distribuiti tramite PKI/secret manager",
    "verifica TLS e hostname sempre attiva; truststore aggiornato",
    "chiave privata non committata, non stampata e accessibile solo al servizio",
    "JWT: algoritmo allowlist, firma, iss, aud, exp e nbf verificati",
    "JWS non cifra il payload; usare JWE solo se richiesto dal protocollo",
    "rotazione/revoca e gestione kid definite con il provider",
    "endpoint sandbox autorizzati, timeout, log senza token o dati sensibili",
]
for voce in checklist:
    print("[ ]", voce)
print("Esempi didattici: richiedere revisione sicurezza/PKI prima della produzione.")
