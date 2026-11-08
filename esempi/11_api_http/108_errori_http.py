# Esempio 108 — Gestire errori HTTP e URL in modo specifico.
from urllib.error import HTTPError, URLError
try:
    raise URLError("Esempio simulato: rete non contattata")
except HTTPError as errore:
    print("Errore HTTP:", errore.code)
except URLError as errore:
    print("Errore di rete:", errore.reason)
