# Esempio 85 — L'ereditarietà riusa metodi di una classe genitore.
class Veicolo:
    def muovi(self):
        return "Il veicolo si muove"
class Bicicletta(Veicolo):
    pass
print(Bicicletta().muovi())
