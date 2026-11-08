# Esempio 77 — with chiude automaticamente un file al termine del blocco.
from pathlib import Path
import tempfile
with tempfile.TemporaryDirectory() as cartella:
    file = Path(cartella) / "nota.txt"
    with file.open("w", encoding="utf-8") as f:
        f.write("Ciao dal file")
    print("File temporaneo scritto")
