# Esempio 88 — @staticmethod definisce un metodo che non usa l'oggetto.
class Calcoli:
    @staticmethod
    def somma(a, b):
        return a + b
print(Calcoli.somma(2, 3))
