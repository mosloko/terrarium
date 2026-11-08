# Esempio 196 — multiprocessing usa processi separati per lavoro CPU-bound.
from multiprocessing import cpu_count
print("CPU logiche disponibili:", cpu_count())
# Avviare processi in applicazioni reali richiede struttura e test dedicati.
