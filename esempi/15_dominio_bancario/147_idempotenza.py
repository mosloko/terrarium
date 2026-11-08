# Esempio 147 — Idempotenza: lo stesso riferimento evita di applicare due volte un'operazione.
operazioni = {}
def registra(riferimento, importo):
    if riferimento in operazioni:
        return "gia registrata"
    operazioni[riferimento] = importo
    return "registrata"
print(registra("demo-1", 500), registra("demo-1", 500))
