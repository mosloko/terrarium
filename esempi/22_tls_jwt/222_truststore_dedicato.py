# mTLS 222 — Usare un truststore CA dedicato (file PEM), oltre al certificato client.
# Il bundle CA deve provenire dalla PKI approvata dall'organizzazione.
import os
import ssl
from urllib.request import Request, urlopen

url, ca, cert, key = (os.getenv(nome) for nome in ("MTLS_URL", "TLS_CA_BUNDLE", "MTLS_CLIENT_CERT", "MTLS_CLIENT_KEY"))
if os.getenv("ESEMPIO_RETE") != "1":
    print("Demo senza rete. Imposta ESEMPIO_RETE=1 e le variabili TLS descritte nel README.")
elif not all((url, ca, cert, key)):
    raise SystemExit("Servono MTLS_URL, TLS_CA_BUNDLE, MTLS_CLIENT_CERT e MTLS_CLIENT_KEY.")
else:
    context = ssl.create_default_context(cafile=ca)  # Truststore dedicato, verifica hostname/TLS attiva.
    context.load_cert_chain(certfile=cert, keyfile=key, password=os.getenv("MTLS_KEY_PASSWORD"))
    with urlopen(Request(url), context=context, timeout=5) as response:
        print("HTTP:", response.status)
