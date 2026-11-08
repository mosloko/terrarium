# Esempio 56 — Una funzione può restituire più valori.
def dividi(a, b):
    return a // b, a % b
quoziente, resto = dividi(10, 3)
print(quoziente, resto)
