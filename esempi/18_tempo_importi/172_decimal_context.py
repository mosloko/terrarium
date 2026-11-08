# Esempio 172 — Decimal può rifiutare arrotondamenti impliciti con Inexact.
from decimal import Decimal, localcontext, Inexact
with localcontext() as ctx:
    ctx.traps[Inexact] = True
    print(Decimal("1.20") + Decimal("0.30"))
