# Esempio 59 — La ricorsione è una funzione che richiama sé stessa.
def fattoriale(n):
    if n <= 1:
        return 1
    return n * fattoriale(n - 1)
print(fattoriale(5))
