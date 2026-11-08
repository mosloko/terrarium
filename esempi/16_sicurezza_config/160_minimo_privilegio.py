# Esempio 160 — Il principio del minimo privilegio: descrivere permessi necessari.
ruoli = {"lettore": {"leggi"}, "operatore": {"leggi", "proponi"}}
print("Permessi operatore:", sorted(ruoli["operatore"]))
