# Esempio 86 — Una sottoclasse può aggiungere un proprio metodo.
class Animale:
    def __init__(self, nome):
        self.nome = nome
class Cane(Animale):
    def verso(self):
        return "bau"
print(Cane("Luna").verso())
