# Esempio 139 — Usare context manager per chiudere la connessione correttamente.
import sqlite3
with sqlite3.connect(":memory:") as con:
    con.execute("SELECT 1")
print("Connessione chiusa automaticamente")
