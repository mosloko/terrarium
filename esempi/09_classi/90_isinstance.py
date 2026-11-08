# Esempio 90 — isinstance verifica se un oggetto è di una certa classe.
class Animale:
    pass
class Gatto(Animale):
    pass
print(isinstance(Gatto(), Animale))
