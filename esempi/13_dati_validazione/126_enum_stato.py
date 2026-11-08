# Esempio 126 — Enum limita i valori ammessi a un insieme noto.
from enum import Enum
class Stato(Enum):
    RICEVUTO = "ricevuto"
    COMPLETATO = "completato"
print(Stato.RICEVUTO.value)
