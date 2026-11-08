# Esempio 89 — dataclass genera metodi utili per classi che contengono dati.
from dataclasses import dataclass
@dataclass
class Punto:
    x: int
    y: int
print(Punto(2, 5))
