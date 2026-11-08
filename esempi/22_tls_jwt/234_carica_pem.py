# JWT/JWS 234 — Verificare una chiave pubblica caricata da PEM fidato.
try:
    import jwt
    from cryptography.hazmat.primitives.asymmetric import rsa
    from cryptography.hazmat.primitives import serialization
except ImportError:
    print("Installa requirements.txt per questo esempio.")
else:
    privata = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    pem = privata.public_key().public_bytes(serialization.Encoding.PEM, serialization.PublicFormat.SubjectPublicKeyInfo)
    chiave_verifica = serialization.load_pem_public_key(pem)
    token = jwt.encode({"sub": "demo"}, privata, algorithm="RS256")
    print(jwt.decode(token, chiave_verifica, algorithms=["RS256"])["sub"])
