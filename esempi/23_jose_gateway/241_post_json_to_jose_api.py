"""Esempio integrato: riceve JSON, firma in JWS, cifra in JWE e inoltra a un'API JOSE.

Installare dal root del repository: python -m pip install -r requirements.txt

Configurazione (variabili d'ambiente; mai inserire chiavi nel codice):
  ESEMPIO_RETE=1
  JOSE_API_URL=https://api-sandbox.example.test/jose
  JOSE_SIGNING_PRIVATE_PEM=/percorso/sicuro/signing-private.pem
  JOSE_RECIPIENT_PUBLIC_PEM=/percorso/sicuro/recipient-public.pem
  JOSE_SIGNING_KID=chiave-firma-test
  JOSE_RECIPIENT_KID=chiave-destinatario-test

Opzionali:
  JOSE_CA_BUNDLE=/percorso/sicuro/ca-bundle.pem
  MTLS_CLIENT_CERT=/percorso/sicuro/client-cert.pem
  MTLS_CLIENT_KEY=/percorso/sicuro/client-key.pem
  MTLS_KEY_PASSWORD=...     # meglio iniettata da secret manager
  JOSE_API_TOKEN=...        # se richiesto dal servizio; mai loggato

Avvio: python esempi/23_jose_gateway/241_post_json_to_jose_api.py

Il server in ingresso ascolta SOLO su 127.0.0.1:8080 e accetta POST /forward
con Content-Type application/json e body JSON oggetto. L'inoltro esterno è
abilitato solo con ESEMPIO_RETE=1 e richiede URL HTTPS. Il body viene serializzato
in modo deterministico, firmato come JWS RS256 e poi cifrato come JWE
RSA-OAEP-256 + A256GCM (nested JOSE); l'API esterna riceve il compact JWE con
Content-Type: application/jose. Redirect disabilitati per non inoltrare il body
(o il bearer token) a un host diverso.

È un esempio locale didattico, NON un gateway production-ready. Per produzione
servono server ASGI/WSGI gestito, autenticazione e autorizzazione inbound,
rate limit, audit senza payload/segreti, policy sui dati, gestione chiavi in
KMS/HSM, rotazione/revoca, osservabilità e revisione sicurezza/compliance.
"""

from __future__ import annotations

import json
import os
import ssl
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import (HTTPRedirectHandler, HTTPSHandler, Request,
                            build_opener)

from jwcrypto import jwk, jwe, jws

MAX_REQUEST_BYTES = 64 * 1024
MAX_UPSTREAM_RESPONSE_BYTES = 16 * 1024
TIMEOUT_SECONDS = 5


class NoRedirect(HTTPRedirectHandler):
    """Non seguire redirect: il body JOSE resta destinato all'host configurato."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def required_env(name: str) -> str:
    """Legge una configurazione obbligatoria senza mostrare il suo valore."""
    value = os.getenv(name)
    if not value:
        raise ValueError(f"Variabile obbligatoria non configurata: {name}")
    return value


def read_key(path_variable: str) -> bytes:
    """Carica un PEM da un percorso fornito dall'ambiente, mai dal repository."""
    path = Path(required_env(path_variable))
    if not path.is_file():
        raise ValueError(f"File PEM non trovato per {path_variable}")
    return path.read_bytes()


def create_tls_context() -> ssl.SSLContext:
    """Crea TLS con verifica CA/hostname e mTLS opzionale."""
    ca_bundle = os.getenv("JOSE_CA_BUNDLE")
    context = ssl.create_default_context(cafile=ca_bundle or None)
    cert = os.getenv("MTLS_CLIENT_CERT")
    key = os.getenv("MTLS_CLIENT_KEY")
    if bool(cert) != bool(key):
        raise ValueError("Per mTLS impostare sia MTLS_CLIENT_CERT sia MTLS_CLIENT_KEY")
    if cert and key:
        context.load_cert_chain(
            certfile=cert,
            keyfile=key,
            password=os.getenv("MTLS_KEY_PASSWORD") or None,
        )
    return context


def make_jose(body: dict) -> str:
    """Produce un JWS del JSON e lo incapsula in un JWE per il destinatario."""
    signing_key = jwk.JWK.from_pem(
        read_key("JOSE_SIGNING_PRIVATE_PEM"),
        password=(os.getenv("JOSE_SIGNING_KEY_PASSWORD") or None),
    )
    recipient_key = jwk.JWK.from_pem(read_key("JOSE_RECIPIENT_PUBLIC_PEM")).public()

    # JSON deterministico per rendere stabile il contenuto firmato.
    payload = json.dumps(
        body, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False
    ).encode("utf-8")

    signed = jws.JWS(payload)
    signed.add_signature(
        signing_key,
        protected={
            "alg": "RS256",
            "kid": required_env("JOSE_SIGNING_KID"),
            "typ": "JOSE",
        },
    )
    compact_jws = signed.serialize(compact=True)

    encrypted = jwe.JWE(
        plaintext=compact_jws.encode("ascii"),
        protected={
            "alg": "RSA-OAEP-256",
            "enc": "A256GCM",
            "cty": "JWS",
        },
    )
    encrypted.add_recipient(
        recipient_key,
        header={"kid": required_env("JOSE_RECIPIENT_KID")},
    )
    return encrypted.serialize(compact=True)


def forward_to_external_api(compact_jwe: str) -> int:
    """Invia il compact JWE e ritorna lo status upstream senza esporre il body."""
    url = required_env("JOSE_API_URL")
    parsed = urlparse(url)
    if parsed.scheme != "https" or not parsed.hostname or parsed.username or parsed.password:
        raise ValueError("JOSE_API_URL deve essere HTTPS e non contenere credenziali")

    headers = {
        "Content-Type": "application/jose",
        "Accept": "application/json, application/jose",
        "User-Agent": "python-jose-learning/1.0",
    }
    token = os.getenv("JOSE_API_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"

    request = Request(url, data=compact_jwe.encode("ascii"), headers=headers, method="POST")
    context = create_tls_context()
    opener = build_opener(HTTPSHandler(context=context), NoRedirect())
    with opener.open(request, timeout=TIMEOUT_SECONDS) as response:
        # Leggiamo solo una quantità limitata; non registriamo né rimandiamo il body.
        response.read(MAX_UPSTREAM_RESPONSE_BYTES + 1)
        return response.status


class PostJwsJweHandler(BaseHTTPRequestHandler):
    """Endpoint locale didattico che accetta JSON e lo inoltra come nested JOSE."""

    server_version = "JoseLearningDemo/1.0"

    def log_message(self, format: str, *args) -> None:
        # Non stampare path, header, token o dati applicativi in questo esempio.
        return

    def reply(self, status: int, message: str) -> None:
        data = json.dumps({"status": message}, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def do_POST(self) -> None:
        if self.path != "/forward":
            self.reply(404, "endpoint non trovato")
            return
        if self.headers.get_content_type() != "application/json":
            self.reply(415, "Content-Type deve essere application/json")
            return
        try:
            length = int(self.headers.get("Content-Length", ""))
        except ValueError:
            self.reply(411, "Content-Length obbligatorio")
            return
        if length < 1:
            self.reply(400, "body obbligatorio")
            return
        if length > MAX_REQUEST_BYTES:
            self.reply(413, "body troppo grande")
            return

        raw_body = self.rfile.read(length)
        if len(raw_body) != length:
            self.reply(400, "body incompleto")
            return
        try:
            payload = json.loads(raw_body)
            if not isinstance(payload, dict):
                raise ValueError("Il body JSON deve essere un oggetto")
        except (json.JSONDecodeError, UnicodeDecodeError, ValueError):
            self.reply(400, "JSON non valido: atteso un oggetto")
            return

        try:
            compact_jwe = make_jose(payload)
            status_upstream = forward_to_external_api(compact_jwe)
        except HTTPError as error:
            # Non restituire al chiamante dettagli upstream che potrebbero contenere dati.
            print(f"Upstream ha risposto con HTTP {error.code}")
            self.reply(502, "servizio upstream ha rifiutato la richiesta")
        except (URLError, TimeoutError, ssl.SSLError) as error:
            print(f"Chiamata upstream fallita: {type(error).__name__}")
            self.reply(502, "servizio upstream non raggiungibile")
        except (ValueError, OSError, jwk.JWKError, jws.JWException, jwe.JWEException) as error:
            print(f"Configurazione o trasformazione JOSE non riuscita: {type(error).__name__}")
            self.reply(500, "configurazione JOSE non valida")
        else:
            self.reply(200, f"inoltrato (HTTP upstream {status_upstream})")


def main() -> None:
    if os.getenv("ESEMPIO_RETE") != "1":
        print("Demo disattivata. Configura le variabili richieste e ESEMPIO_RETE=1.")
        print("Il server locale non verrà avviato senza opt-in esplicito.")
        return

    # Verifica configurazione e chiavi prima di aprire il socket locale.
    required_env("JOSE_API_URL")
    required_env("JOSE_SIGNING_KID")
    required_env("JOSE_RECIPIENT_KID")
    create_tls_context()
    server = HTTPServer(("127.0.0.1", 8080), PostJwsJweHandler)
    print("Demo in ascolto solo su http://127.0.0.1:8080/forward (Ctrl+C per terminare)")
    print("Non inviare dati reali: endpoint solo per test locale autorizzato.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nChiusura server demo")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
