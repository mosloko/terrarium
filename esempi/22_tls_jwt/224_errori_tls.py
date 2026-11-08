# mTLS 224 — Distinguere errori TLS/certificato da errori HTTP o rete.
import ssl
from urllib.error import HTTPError, URLError

try:
    raise ssl.SSLCertVerificationError("Esempio simulato: CA non attendibile")
except ssl.SSLCertVerificationError as errore:
    print("Verifica certificato fallita:", type(errore).__name__)
except HTTPError as errore:
    print("Errore HTTP:", errore.code)
except URLError as errore:
    print("Errore trasporto:", errore.reason)
# Non risolvere disabilitando la verifica TLS: correggere CA, hostname o certificato.
