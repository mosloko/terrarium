# Esempio 165 — Un circuit breaker semplificato apre dopo errori ripetuti.
errori = 3
stato = "aperto" if errori >= 3 else "chiuso"
print(stato)
