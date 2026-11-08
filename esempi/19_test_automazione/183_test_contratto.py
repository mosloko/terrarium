# Esempio 183 — Un test di contratto semplice verifica forma della risposta API.
risposta = {"stato": "ok", "codice": 200}
assert set(risposta) == {"stato", "codice"}
assert isinstance(risposta["codice"], int)
print("Contratto demo valido")
