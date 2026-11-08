# Esempio 135 — Una transazione raggruppa modifiche atomiche.
import sqlite3
with sqlite3.connect(":memory:") as con:
    con.execute("CREATE TABLE saldo (valore INTEGER)")
    with con:
        con.execute("INSERT INTO saldo VALUES (?)", (1000,))
    print(con.execute("SELECT valore FROM saldo").fetchone())
