# mTLS 221 — Configurare una richiesta HTTPS con certificato client.
# Solo verso endpoint autorizzati: configura ESEMPIO_RETE=1 e MTLS_URL.
# Non committare certificati o chiavi private; usa secret manager/volume protetti.
import os
import ssl
from urllib.request import Request, urlopen

url = os.getenv("MTLS_URL")
cert = os.getenv("MTLS_CLIENT_CERT")
key = os.getenv("MTLS_CLIENT_KEY")
if os.getenv("ESEMPIO_RETE") != "1":
    print("Rete disattivata: configura ESEMPIO_RETE=1, MTLS_URL, MTLS_CLIENT_CERT e MTLS_CLIENT_KEY.")
elif not all((url, cert, key)):
    raise SystemExit("Configura MTLS_URL, MTLS_CLIENT_CERT e MTLS_CLIENT_KEY.")
else:
    context = ssl.create_default_context()  # Verifica TLS server: non disabilitarla.
    context.load_cert_chain(certfile=cert, keyfile=key, password=os.getenv("MTLS_KEY_PASSWORD"))
    with urlopen(Request(url, headers={"Accept": "application/json"}), context=context, timeout=5) as response:
        print("HTTP:", response.status, "TLS:", response.version())
