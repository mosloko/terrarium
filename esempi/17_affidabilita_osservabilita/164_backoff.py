# Esempio 164 — Backoff esponenziale; questa demo calcola i ritardi senza attendere.
ritardi = [min(0.5 * (2 ** n), 8) for n in range(5)]
print(ritardi)
