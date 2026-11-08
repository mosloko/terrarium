# Esempio 184 — Mock consente test senza chiamare servizi esterni.
from unittest.mock import Mock
servizio = Mock(return_value={"stato": "ok"})
print(servizio(), "chiamate:", servizio.call_count)
