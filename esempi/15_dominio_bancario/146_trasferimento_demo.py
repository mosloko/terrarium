# Esempio 146 — Un trasferimento deve applicare entrambe le variazioni insieme.
from decimal import Decimal
conti = {"A": Decimal("20.00"), "B": Decimal("5.00")}
importo = Decimal("3.00")
conti["A"] -= importo
conti["B"] += importo
print(conti)  # Solo simulazione in memoria, non un sistema bancario reale.
