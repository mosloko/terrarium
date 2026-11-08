# Esempio 120 — Il server della libreria standard è didattico, non production-ready.
from http.server import HTTPServer
print("In produzione usare un server supportato, TLS, autenticazione e controlli operativi.")
print("HTTPServer disponibile:", HTTPServer.__name__)
