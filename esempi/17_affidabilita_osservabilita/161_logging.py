# Esempio 161 — Logging standard con livelli e messaggi senza dati sensibili.
import logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
logging.info("Elaborazione demo completata")
