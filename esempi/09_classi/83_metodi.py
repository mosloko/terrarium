# Esempio 83 — Un metodo è una funzione definita dentro una classe.
class Salvadanaio:
    def __init__(self):
        self.monete = 0
    def aggiungi(self, quantita):
        self.monete += quantita

salvadanaio = Salvadanaio()
salvadanaio.aggiungi(3)
print(salvadanaio.monete)
