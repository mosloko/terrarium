# API 214 — Basic Auth è mostrata solo come costruzione header; preferire OAuth/token.
import base64
import os

utente = os.getenv("API_USER", "demo")
password = os.getenv("API_PASSWORD")
if password:
    valore = base64.b64encode(f"{utente}:{password}".encode()).decode()
    header = f"Basic {valore}"
    print("Header Basic creato in memoria:", header.split()[0], "(segreto non stampato)")
else:
    print("Impostare API_PASSWORD solo in un ambiente di test autorizzato.")
# Basic Auth protegge le credenziali solo se il trasporto HTTPS è verificato.
