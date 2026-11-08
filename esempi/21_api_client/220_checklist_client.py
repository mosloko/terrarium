# API 220 — Checklist client: TLS, timeout, input validato, errori, segreti e log puliti.
checklist = [
    "HTTPS e verifica certificati", "timeout", "body e response con limiti",
    "header e Content-Type corretti", "query/path codificati", "errori HTTP e rete distinti",
    "token da secret manager/ambiente", "niente dati sensibili nei log",
    "retry limitati e idempotenza", "test con mock e sandbox autorizzata",
]
for elemento in checklist:
    print("[ ]", elemento)
print("Esempi didattici: non usare direttamente in produzione bancaria.")
