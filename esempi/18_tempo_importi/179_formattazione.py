# Esempio 179 — Formattare un importo per visualizzazione, non per ricalcolare.
from decimal import Decimal
importo = Decimal("1234.50")
print(f"EUR {importo:.2f}")
