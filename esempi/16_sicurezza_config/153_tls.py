# Esempio 153 — SSLContext usa i certificati di sistema per verificare TLS.
import ssl
contesto = ssl.create_default_context()
print("Verifica certificati attiva:", contesto.verify_mode == ssl.CERT_REQUIRED)
