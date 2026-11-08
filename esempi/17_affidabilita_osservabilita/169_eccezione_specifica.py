# Esempio 169 — Non catturare eccezioni generiche senza re-raise o gestione adeguata.
try:
    int("abc")
except ValueError as errore:
    print("Errore previsto:", type(errore).__name__)
