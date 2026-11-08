# Esempio 95 — pathlib rappresenta percorsi di file in modo portabile.
from pathlib import Path
percorso = Path("appunti") / "lezione.txt"
print(percorso.name, percorso.suffix)
