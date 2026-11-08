# Esempio 72 — ValueError può verificarsi convertendo testo non numerico.
try:
    print(int("ciao"))
except ValueError:
    print("Il testo non è un numero intero")
