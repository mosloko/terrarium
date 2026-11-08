# Esempio 185 — Mockare un client API evita rete nei test.
from unittest.mock import Mock
client = Mock()
client.get.return_value = {"id": "demo"}
assert client.get("/risorsa")["id"] == "demo"
print("Test senza rete completato")
