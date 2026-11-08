# Esempio 138 — Un indice può accelerare ricerche ripetute su una colonna.
import sqlite3
with sqlite3.connect(":memory:") as con:
    con.execute("CREATE TABLE movimenti (riferimento TEXT)")
    con.execute("CREATE INDEX idx_riferimento ON movimenti(riferimento)")
    print("Indice creato")
