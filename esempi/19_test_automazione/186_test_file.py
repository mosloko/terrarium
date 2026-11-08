# Esempio 186 — TemporaryDirectory isola dati di test e li elimina dopo.
from pathlib import Path
from tempfile import TemporaryDirectory
with TemporaryDirectory() as cartella:
    path = Path(cartella) / "testo.txt"
    path.write_text("test", encoding="utf-8")
    assert path.read_text(encoding="utf-8") == "test"
print("File temporaneo eliminato automaticamente")
