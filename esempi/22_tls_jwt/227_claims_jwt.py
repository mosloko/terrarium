# JWT/JWS 227 — Aggiungere exp, iat e jti ai claim di un JWT.
from datetime import datetime, timedelta, timezone
try:
    import jwt
    from cryptography.hazmat.primitives.asymmetric import rsa
except ImportError:
    print("Installa requirements.txt per questo esempio.")
else:
    key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    now = datetime.now(timezone.utc)
    claims = {"sub": "demo", "iat": now, "exp": now + timedelta(minutes=5), "jti": "id-demo-001"}
    token = jwt.encode(claims, key, algorithm="RS256")
    decodificati = jwt.decode(token, key.public_key(), algorithms=["RS256"])
    print("Scadenza UTC:", datetime.fromtimestamp(decodificati["exp"], timezone.utc).isoformat())
# In produzione jti deve essere un identificatore unico e le chiavi vanno gestite fuori dal codice.
