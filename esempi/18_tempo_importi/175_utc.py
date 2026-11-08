# Esempio 175 — datetime con timezone UTC evita date/ore ambigue.
from datetime import datetime, timezone
ora = datetime.now(timezone.utc)
print(ora.isoformat())
