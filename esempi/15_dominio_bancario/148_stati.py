# Esempio 148 — Rappresentare lo stato di un pagamento con enum.
from enum import Enum
class StatoPagamento(Enum):
    RICEVUTO = "ricevuto"
    IN_VERIFICA = "in_verifica"
    RIFIUTATO = "rifiutato"
print(StatoPagamento.IN_VERIFICA.value)
