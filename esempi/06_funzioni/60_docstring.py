# Esempio 60 — Una docstring descrive cosa fa una funzione.
def area(base, altezza):
    """Calcola l'area di un rettangolo."""
    return base * altezza
print(area(5, 3), area.__doc__)
