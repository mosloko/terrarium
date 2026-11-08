# Esempio 168 — Metriche di base: conteggio e durata misurata con monotonic.
from time import monotonic
inizio = monotonic()
_ = sum(range(1000))
print("Durata secondi:", monotonic() - inizio)
