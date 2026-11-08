# Esempio 132 — Creare tabella in un database in memoria.
import sqlite3
with sqlite3.connect(":memory:") as con:
    con.execute("CREATE TABLE clienti (id INTEGER PRIMARY KEY, nome TEXT NOT NULL)")
    print("Tabella clienti creata")
