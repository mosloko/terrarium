# Esempio 198 — un generatore produce elementi a richiesta e limita memoria.
def eventi_demo():
    for n in range(3):
        yield {"numero": n}
print(list(eventi_demo()))
