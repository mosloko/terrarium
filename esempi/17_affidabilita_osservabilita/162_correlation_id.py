# Esempio 162 — Aggiungere un identificatore di correlazione alle operazioni.
import uuid
correlation_id = str(uuid.uuid4())
print({"correlation_id": correlation_id, "evento": "richiesta_demo"})
