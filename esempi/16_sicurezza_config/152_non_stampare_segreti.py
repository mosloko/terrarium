# Esempio 152 — Non stampare il segreto; mostrare solo se è configurato.
import os
segreto = os.getenv("API_TOKEN")
print("Token presente" if segreto else "Token assente")
