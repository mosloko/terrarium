# JWT/JWS 233 — Esportare chiave pubblica PEM; non esportiamo né stampiamo la privata.
try:
    from cryptography.hazmat.primitives.asymmetric import rsa
    from cryptography.hazmat.primitives import serialization
except ImportError:
    print("Installa requirements.txt per questo esempio.")
else:
    privata = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    pem_pubblica = privata.public_key().public_bytes(serialization.Encoding.PEM, serialization.PublicFormat.SubjectPublicKeyInfo)
    print(pem_pubblica.decode().splitlines()[0])
    print("La chiave privata resta in memoria e non viene stampata o salvata.")
