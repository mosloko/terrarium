# Esempio 75 — raise genera intenzionalmente un'eccezione.
def controlla_eta(eta):
    if eta < 0:
        raise ValueError("L'età non può essere negativa")
    return eta
try:
    controlla_eta(-1)
except ValueError as errore:
    print(errore)
