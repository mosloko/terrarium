# API 216 — Retry limitato solo per errori temporanei; evitare retry ciechi di POST.
import time

def con_retry(operazione, tentativi=3):
    for numero in range(tentativi):
        try:
            return operazione()
        except TimeoutError:
            if numero + 1 == tentativi:
                raise
            time.sleep(min(0.1 * (2 ** numero), 1))

contatore = {"n": 0}
def demo():
    contatore["n"] += 1
    if contatore["n"] < 2:
        raise TimeoutError("timeout simulato")
    return "ok"
print(con_retry(demo), "tentativi:", contatore["n"])
