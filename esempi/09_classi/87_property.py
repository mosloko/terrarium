# Esempio 87 — @property permette di leggere un metodo come attributo.
class Cerchio:
    def __init__(self, raggio):
        self.raggio = raggio
    @property
    def diametro(self):
        return self.raggio * 2
print(Cerchio(5).diametro)
