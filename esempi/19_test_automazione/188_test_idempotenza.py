# Esempio 188 — Un test d'idempotenza verifica che un retry non duplichi l'operazione.
registrati = set()
def registra(key):
    gia_presente = key in registrati
    registrati.add(key)
    return not gia_presente
assert registra("k1") is True
assert registra("k1") is False
print("Idempotenza verificata")
