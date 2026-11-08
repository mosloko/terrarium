# Esempio 167 — Un health check dovrebbe rivelare solo lo stato essenziale.
def health():
    return {"status": "ok"}
print(health())
