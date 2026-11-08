# Esempio 110 — Non scrivere token nei sorgenti: leggerli dall'ambiente.
import os
token = os.getenv("API_TOKEN")
print("Token configurato:", token is not None)
# Non stampare o registrare mai il valore del token.
