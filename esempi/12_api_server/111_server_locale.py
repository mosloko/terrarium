# Esempio 111 — Creare un server HTTP locale per una demo, solo su loopback.
from http.server import BaseHTTPRequestHandler, HTTPServer
class Gestore(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200); self.end_headers(); self.wfile.write(b"demo locale")
server = HTTPServer(("127.0.0.1", 0), Gestore)
print("Server demo disponibile solo su localhost:", server.server_address)
server.server_close()
