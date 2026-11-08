# Esempio 150 — Le date contabili dovrebbero avere fuso/orario e regole di business definiti.
from datetime import datetime, timezone
ora_utc = datetime.now(timezone.utc)
print(ora_utc.isoformat())
