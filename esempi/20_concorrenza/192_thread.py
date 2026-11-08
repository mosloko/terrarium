# Esempio 192 — threading esegue lavoro concorrente; non condivide segreti nei log.
from threading import Thread
risultati = []
def lavoro():
    risultati.append("completato")
t = Thread(target=lavoro)
t.start(); t.join()
print(risultati)
