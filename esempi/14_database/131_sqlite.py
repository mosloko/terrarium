# Esempio 131 — SQLite è incluso in Python; :memory: crea un database volatile.
import sqlite3
con = sqlite3.connect(":memory:")
print(con.execute("select sqlite_version()").fetchone()[0])
con.close()
