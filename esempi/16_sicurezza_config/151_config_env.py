# Esempio 151 — Secrets: leggere configurazione dall'ambiente, mai inserirla nel codice.
import os
url_db = os.getenv("DB_URL")
print("Configurazione DB presente:", url_db is not None)
