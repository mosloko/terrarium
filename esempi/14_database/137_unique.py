# Esempio 137 — Un vincolo UNIQUE evita duplicati a livello database.
import sqlite3
with sqlite3.connect(":memory:") as con:
    con.execute("CREATE TABLE richieste (chiave TEXT UNIQUE)")
    con.execute("INSERT INTO richieste VALUES (?)", ("idem-1",))
    print("Vincolo UNIQUE creato; il duplicato sarebbe rifiutato.")
