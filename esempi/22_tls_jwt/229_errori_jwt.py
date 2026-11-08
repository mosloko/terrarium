# JWT/JWS 229 — Gestire token scaduto e firma non valida.
try:
    import jwt
    from cryptography.hazmat.primitives.asymmetric import rsa
except ImportError:
    print("Installa requirements.txt per questo esempio.")
else:
    a = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    b = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    token = jwt.encode({"sub": "demo"}, a, algorithm="RS256")
    try:
        jwt.decode(token, b.public_key(), algorithms=["RS256"])
    except jwt.InvalidTokenError as errore:
        print("Token rifiutato:", type(errore).__name__)
