# Esempio 71 — try/except gestisce un errore previsto.
try:
    risultato = 10 / 0
except ZeroDivisionError:
    risultato = "divisione non possibile"
print(risultato)
