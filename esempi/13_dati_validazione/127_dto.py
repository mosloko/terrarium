# Esempio 127 — Dataclass definisce la forma dei dati dell'applicazione.
from dataclasses import dataclass
@dataclass(frozen=True)
class Pagamento:
    riferimento: str
    importo_cent: int
print(Pagamento("demo-1", 500))
