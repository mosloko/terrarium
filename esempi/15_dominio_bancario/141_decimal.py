# Esempio 141 — Decimal rappresenta importi decimali senza errori tipici dei float.
from decimal import Decimal
importi = Decimal("10.25") + Decimal("0.10")
print(importi)
