# Esempio 107 — Usare un endpoint configurabile e validare lo schema minimo.
import os
from urllib.parse import urlparse
url = os.getenv("API_URL", "https://example.com")
parti = urlparse(url)
assert parti.scheme in {"https", "http"} and parti.netloc
print("Endpoint configurato:", parti.scheme, parti.hostname)
