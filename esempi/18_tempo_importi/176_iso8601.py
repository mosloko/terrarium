# Esempio 176 — ISO 8601 è un formato pratico per scambiare date.
from datetime import datetime, timezone
valore = datetime.now(timezone.utc).isoformat()
print(datetime.fromisoformat(valore))
