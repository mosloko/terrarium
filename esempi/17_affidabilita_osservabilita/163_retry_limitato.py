# Esempio 163 — Retry limitato: evita cicli infiniti e ritardi incontrollati.
max_tentativi = 3
for tentativo in range(1, max_tentativi + 1):
    print("Tentativo demo", tentativo)
