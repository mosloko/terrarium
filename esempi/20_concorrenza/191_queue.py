# Esempio 191 — queue fornisce una coda thread-safe tra thread.
from queue import Queue
coda = Queue()
coda.put("evento demo")
print(coda.get())
