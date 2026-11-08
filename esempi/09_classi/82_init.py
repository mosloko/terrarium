# Esempio 82 — __init__ inizializza i dati di un oggetto.
class Animale:
    def __init__(self, nome):
        self.nome = nome

gatto = Animale("Milo")
print(gatto.nome)
