# Esempio 78 — Leggiamo un file temporaneo in modalità testo.
from pathlib import Path
import tempfile
with tempfile.TemporaryDirectory() as cartella:
    file = Path(cartella) / "nota.txt"
    file.write_text("Una riga di testo", encoding="utf-8")
    print(file.read_text(encoding="utf-8"))
