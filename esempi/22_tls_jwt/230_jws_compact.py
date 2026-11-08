# JWT/JWS 230 — JWS compatto: payload firmato e verificato con jwcrypto.
try:
    from jwcrypto import jwk, jws
except ImportError:
    print("Installa requirements.txt per questo esempio.")
else:
    key = jwk.JWK.generate(kty="RSA", size=2048)
    messaggio = jws.JWS(b'{"evento":"demo"}')
    messaggio.add_signature(key, protected={"alg": "RS256", "kid": "chiave-effimera-demo"})
    compatto = messaggio.serialize(compact=True)
    ricevuto = jws.JWS()
    ricevuto.deserialize(compatto)
    ricevuto.verify(key.public())
    print("JWS verificato; payload:", ricevuto.payload.decode())
