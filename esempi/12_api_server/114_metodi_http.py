# Esempio 114 — Limitare i metodi accettati: gli altri ricevono 405.
from http.server import BaseHTTPRequestHandler
class API(BaseHTTPRequestHandler):
    def do_DELETE(self):
        self.send_error(405, "Metodo non consentito nella demo")
print("Un'API dovrebbe permettere solo i metodi necessari.")
