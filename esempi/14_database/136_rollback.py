# Esempio 136 — Un errore nel blocco transazionale annulla le modifiche.
import sqlite3
con = sqlite3.connect(":memory:")
con.execute("CREATE TABLE demo (valore INTEGER)")
try:
    with con:
        con.execute("INSERT INTO demo VALUES (1)")
        raise RuntimeError("Errore simulato")
except RuntimeError:
    pass
print(con.execute("SELECT count(*) FROM demo").fetchone()[0])
con.close()
