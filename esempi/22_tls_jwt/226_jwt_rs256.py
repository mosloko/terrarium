# JWT/JWS 226 — Creare e verificare localmente un JWT firmato RS256.
# Dipendenze: PyJWT e cryptography; chiave RSA effimera solo per questa demo.
try:
    import jwt
    from cryptography.hazmat.primitives.asymmetric import rsa
except ImportError:
    print("Installa requirements.txt per questo esempio.")
else:
    privata = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    pubblica = privata.public_key()
    token = jwt.encode({"sub": "utente-demo", "iss": "esempio", "aud": "api-demo"}, privata, algorithm="RS256")
    claims = jwt.decode(token, pubblica, algorithms=["RS256"], issuer="esempio", audience="api-demo")
    print("Token firmato e verificato; subject:", claims["sub"])
