# Esempio 193 — Lock protegge una sezione critica condivisa.
from threading import Lock
lock = Lock()
with lock:
    valore = 1
print(valore)
