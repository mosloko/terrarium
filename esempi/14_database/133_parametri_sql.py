# Esempio 133 — Inserire righe con parametri, mai concatenando input nella query.
import sqlite3
with sqlite3.connect(":memory:") as con:
    con.execute("CREATE TABLE demo (nome TEXT)")
    con.execute("INSERT INTO demo VALUES (?)", ("Ada",))
    print(con.execute("SELECT nome FROM demo").fetchone())
