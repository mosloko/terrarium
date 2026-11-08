# mTLS 223 — Controllare il truststore dedicato e la verifica dei certificati.
import ssl
from pathlib import Path
ca_file = Path("certificati-demo/ca-bundle.pem")
print("Bundle CA configurabile:", ca_file)
# Il file non è incluso nel repository: ottenerlo dalla PKI aziendale.
ctx = ssl.create_default_context(cafile=str(ca_file) if ca_file.exists() else None)
print("Verifica certificati attiva:", ctx.verify_mode == ssl.CERT_REQUIRED)
print("Verifica hostname attiva:", ctx.check_hostname)
