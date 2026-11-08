# Esempio 128 — Le annotazioni aiutano lettori e strumenti, non validano da sole.
def descrivi(riferimento: str, importo_cent: int) -> str:
    return f"{riferimento}: {importo_cent} centesimi"
print(descrivi("demo-2", 250))
