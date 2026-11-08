# Esempio 115 — Parse della query string in un handler.
from urllib.parse import urlparse, parse_qs
url = "/clienti?stato=attivo&pagina=2"
print(parse_qs(urlparse(url).query))
