# Esempio 84 — __str__ definisce come mostrare un oggetto come testo.
class Libro:
    def __init__(self, titolo):
        self.titolo = titolo
    def __str__(self):
        return f"Libro: {self.titolo}"
print(Libro("Il piccolo principe"))
