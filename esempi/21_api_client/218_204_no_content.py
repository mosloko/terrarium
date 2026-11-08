# API 218 — Gestire 204 No Content senza tentare di decodificare JSON vuoto.
def interpreta_response(status, body):
    if status == 204 or not body:
        return None
    import json
    return json.loads(body)
print(interpreta_response(204, b""))
print(interpreta_response(200, b'{"ok": true}'))
