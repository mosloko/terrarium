# API 219 — ETag/If-None-Match: validazione condizionale e risposta 304.
# Demo della composizione degli header, non invia rete.
from urllib.request import Request
etag = '"versione-demo-1"'
req = Request("https://api.example.test/risorsa/1", headers={"If-None-Match": etag, "Accept": "application/json"})
print(req.get_header("If-none-match"))
print("304 significa che la copia locale è ancora valida; non c'è body da leggere.")
