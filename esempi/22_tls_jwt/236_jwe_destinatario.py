# JWT/JWS 236 — JWE usa la chiave pubblica del destinatario per cifrare.
try:
    from jwcrypto import jwk, jwe
except ImportError:
    print("Installa requirements.txt per questo esempio.")
else:
    destinatario = jwk.JWK.generate(kty="RSA", size=2048)
    demo = jwe.JWE(b"payload demo", protected={"alg": "RSA-OAEP-256", "enc": "A256GCM"})
    demo.add_recipient(destinatario.public())
    print("Solo la chiave privata corrispondente può decifrare; token compatto creato:", bool(demo.serialize(compact=True)))
