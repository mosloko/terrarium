# Esempio 159 — Limitare input per ridurre errori e abusi.
def valida_riferimento(testo):
    return isinstance(testo, str) and 1 <= len(testo) <= 40
print(valida_riferimento("demo-1"), valida_riferimento(""))
