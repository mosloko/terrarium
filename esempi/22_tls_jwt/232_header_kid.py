# JWT/JWS 232 — Leggere header JWT solo per routing; non fidarsi finché la firma non è verificata.
try:
    import jwt
    from cryptography.hazmat.primitives.asymmetric import rsa
except ImportError:
    print("Installa requirements.txt per questo esempio.")
else:
    key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    token = jwt.encode({"sub": "demo"}, key, algorithm="RS256", headers={"kid": "key-demo"})
    print("Header non verificato:", jwt.get_unverified_header(token))
    print("Usare kid solo per selezionare chiavi da un insieme fidato, poi verificare la firma.")
