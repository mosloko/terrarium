# Esempio 199 — itertools.islice limita un flusso di elementi.
from itertools import count, islice
print(list(islice(count(1), 5)))
