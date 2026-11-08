# Esempio 170 — Configurazione esplicita rende l'applicazione più prevedibile.
config = {"ambiente": "locale", "timeout_secondi": 3, "retry": 2}
assert config["timeout_secondi"] > 0
print(config)
