# Esempio 142 — Per calcoli monetari evita float.
print(0.1 + 0.2)  # Approssimazione binaria
from decimal import Decimal
print(Decimal("0.10") + Decimal("0.20"))
