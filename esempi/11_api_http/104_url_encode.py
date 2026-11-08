# Esempio 104 — Un URL va codificato per gestire spazi e caratteri speciali.
from urllib.parse import quote
termine = "conto corrente"
print("/ricerca/" + quote(termine))
