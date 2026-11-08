# Esempio 143 — ROUND_HALF_UP mostra una modalità di arrotondamento esplicita.
from decimal import Decimal, ROUND_HALF_UP
valore = Decimal("1.005").quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
print(valore)
