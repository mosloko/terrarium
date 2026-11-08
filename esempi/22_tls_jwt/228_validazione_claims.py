# JWT/JWS 228 — Verificare audience, issuer e algoritmo consentito.
try:
    import jwt
    from cryptography.hazmat.primitives.asymmetric import rsa
except ImportError:
    print("Installa requirements.txt per questo esempio.")
else:
    priv = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    token = jwt.encode({"sub": "client-demo", "iss": "issuer-demo", "aud": "payments-demo"}, priv, algorithm="RS256")
    result = jwt.decode(token, priv.public_key(), algorithms=["RS256"], issuer="issuer-demo", audience="payments-demo")
    print("Audience verificata:", result["aud"])
