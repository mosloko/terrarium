# Esempio 103 — Aggiungere query string senza concatenare manualmente i caratteri.
from urllib.parse import urlencode
parametri = {"stato": "attivo", "pagina": 1}
print("https://example.com/clienti?" + urlencode(parametri))
