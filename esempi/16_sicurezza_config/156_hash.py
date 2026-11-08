# Esempio 156 — Hash SHA-256 per integrità, non per cifrare o conservare password.
import hashlib
impronta = hashlib.sha256(b"documento demo").hexdigest()
print(impronta[:12])
