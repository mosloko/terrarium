# Esempio 134 — Selezionare dati con query parametrizzata.
import sqlite3
with sqlite3.connect(":memory:") as con:
    con.execute("CREATE TABLE demo (id INTEGER, stato TEXT)")
    con.executemany("INSERT INTO demo VALUES (?, ?)", [(1, "ok"), (2, "in attesa")])
    print(con.execute("SELECT id FROM demo WHERE stato = ?", ("ok",)).fetchall())
