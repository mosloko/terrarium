# Esempio 178 — Un importo negativo può indicare un accredito o un addebito secondo convenzione.
movimenti_cent = {"accredito": 2500, "addebito": -700}
print(sum(movimenti_cent.values()))
