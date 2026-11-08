# mTLS 225 — Ispezionare metadati certificato senza stampare chiavi private.
# Richiede un certificato PEM pubblico di test; non stampa dati sensibili.
import os
import ssl

cert = os.getenv("MTLS_CLIENT_CERT")
if not cert:
    print("Imposta MTLS_CLIENT_CERT a un certificato di test per verificare la sintassi.")
else:
    try:
        info = ssl._ssl._test_decode_cert(cert)  # Strumento diagnostico non pubblico/portabile.
        print("Subject:", info.get("subject"))
        print("Scadenza:", info.get("notAfter"))
    except (OSError, ssl.SSLError) as errore:
        print("Certificato non leggibile:", type(errore).__name__)
# In produzione usare strumenti PKI supportati; non affidarsi a API private di ssl.
