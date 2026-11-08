# Esempio 73 — else viene eseguito quando try non incontra errori.
try:
    numero = int("25")
except ValueError:
    print("Testo non valido")
else:
    print("Numero:", numero)
