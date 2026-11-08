# Esempio 171 — Decimal quantize rappresenta importi con due decimali.
from decimal import Decimal
importo = Decimal("12.3").quantize(Decimal("0.01"))
print(importo)
