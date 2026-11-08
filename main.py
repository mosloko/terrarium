# Esegue in ordine tutti gli esempi numerati nelle cartelle.
# runpy dà a ogni file un namespace separato; unittest negli esempi viene eseguito.
from pathlib import Path
import runpy

cartella_esempi = Path(__file__).parent / "esempi"
file_esempi = sorted(
    (percorso for percorso in cartella_esempi.glob("**/*.py")
     if percorso.stem[:1].isdigit()),
    key=lambda percorso: int(percorso.stem.split("_", 1)[0]),
)
for file_esempio in file_esempi:
    print(f"\n### {file_esempio.relative_to(cartella_esempi)} ###")
    runpy.run_path(str(file_esempio), run_name="__main__")
print(f"\nCompletato: {len(file_esempi)} esempi eseguiti.")
