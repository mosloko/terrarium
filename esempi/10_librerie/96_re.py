# Esempio 96 — re cerca un modello di testo con un'espressione regolare.
import re
risultato = re.search(r"\d+", "Ho 3 mele")
print(risultato.group() if risultato else "Nessun numero")
