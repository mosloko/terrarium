# Esempio 197 — contextvars conserva valori contestuali in codice asincrono.
from contextvars import ContextVar
correlation = ContextVar("correlation", default="non impostato")
correlation.set("demo-123")
print(correlation.get())
