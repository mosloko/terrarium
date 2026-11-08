# Esempio 157 — Per verificare password usare funzioni dedicate e salt; non SHA semplice.
import hashlib
print("Per password usare scrypt/PBKDF2/bcrypt/Argon2 con parametri adeguati.")
print("Disponibile in stdlib:", hasattr(hashlib, "scrypt"))
