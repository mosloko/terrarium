# Esempio 158 — secrets genera token imprevedibili per casi crittografici.
import secrets
token_demo = secrets.token_urlsafe(16)
print("Token generato (demo, non loggare segreti reali):", len(token_demo), "caratteri")
