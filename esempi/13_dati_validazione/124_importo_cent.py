# Esempio 124 — Validare importi usando interi in centesimi.
importo_cent = 1250
if not isinstance(importo_cent, int) or importo_cent <= 0:
    raise ValueError("Importo non valido")
print("Importo:", importo_cent, "centesimi")
