# Esegue in ordine tutti i 100 esempi, uno alla volta.
# Ogni file viene eseguito isolatamente per evitare conflitti tra variabili.
from pathlib import Path
import runpy

cartella_esempi = Path(__file__).parent / "esempi"
file_esempi = sorted(cartella_esempi.glob("**/[0-9][0-9][0-9]_*.py"))
# I nomi sono a due cifre per capitolo e tre cifre per file? Usiamo il glob più generale.
if not file_esempi:
    file_esempi = sorted(cartella_esempi.glob("**/[0-9][0-9]_*.py"))

for file_esempio in file_esempi:
    print(f"\n### {file_esempio.relative_to(cartella_esempi)} ###")
    runpy.run_path(str(file_esempio), run_name="__main__")

print(f"\nCompletato: {len(file_esempi)} esempi eseguiti.")
