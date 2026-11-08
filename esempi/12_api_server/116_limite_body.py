# Esempio 116 — Verificare che un body non superi una dimensione massima.
LIMITE = 1024 * 1024
lunghezza_ricevuta = 512
if not 0 <= lunghezza_ricevuta <= LIMITE:
    raise ValueError("Body troppo grande")
print("Dimensione accettata:", lunghezza_ricevuta)
