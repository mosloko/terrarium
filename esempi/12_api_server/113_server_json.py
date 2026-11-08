# Esempio 113 — Restituire JSON da un handler HTTP.
import json
from http.server import BaseHTTPRequestHandler
class Gestore(BaseHTTPRequestHandler):
    def do_GET(self):
        corpo = json.dumps({"stato": "ok"}).encode()
        self.send_response(200); self.send_header("Content-Type", "application/json"); self.end_headers(); self.wfile.write(corpo)
print("Handler JSON definito; non espone servizi in rete da solo.")
