# JWT/JWS 231 — Il payload JWS è firmato ma NON cifrato: è leggibile da chiunque lo riceva.
import base64
import json
try:
    import jwt
    from cryptography.hazmat.primitives.asymmetric import rsa
except ImportError:
    print("Installa requirements.txt per questo esempio.")
else:
    key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    token = jwt.encode({"sub": "demo", "scope": "read"}, key, algorithm="RS256")
    parte_payload = token.split(".")[1]
    parte_payload += "=" * (-len(parte_payload) % 4)
    print("Payload visibile:", json.loads(base64.urlsafe_b64decode(parte_payload)))
    print("Non inserire segreti o dati personali nei claim leggibili.")
