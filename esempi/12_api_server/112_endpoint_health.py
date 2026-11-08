# Esempio 112 — Definire un endpoint GET minimo senza avviare un server pubblico.
from http.server import BaseHTTPRequestHandler
class Gestore(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            self.send_response(200); self.end_headers(); self.wfile.write(b"ok")
        else:
            self.send_error(404)
print("Handler /health definito; eseguirlo solo in ambiente locale di test.")
