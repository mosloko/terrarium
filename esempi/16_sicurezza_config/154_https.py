# Esempio 154 — Usare HTTPS per endpoint remoti; rifiutare HTTP non cifrato.
from urllib.parse import urlparse
url = "https://api.example.test"
assert urlparse(url).scheme == "https"
print("Schema HTTPS richiesto")
