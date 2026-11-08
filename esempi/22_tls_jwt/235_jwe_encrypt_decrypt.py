# JWT/JWS 235 — JWE compatto: cifrare e decifrare un payload per il destinatario.
# La chiave RSA è effimera e generata solo in memoria per la dimostrazione.
try:
    from jwcrypto import jwk, jwe
except ImportError:
    print("Installa requirements.txt per questo esempio.")
else:
    privata = jwk.JWK.generate(kty="RSA", size=2048)
    oggetto = jwe.JWE(b'{"messaggio":"segreto-demo"}', protected={"alg": "RSA-OAEP-256", "enc": "A256GCM"})
    oggetto.add_recipient(privata.public())
    token = oggetto.serialize(compact=True)
    decifrato = jwe.JWE()
    decifrato.deserialize(token, key=privata)
    print("JWE decifrato localmente:", decifrato.payload.decode())
