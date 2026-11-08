# Esempio 119 — Separare il routing dalla logica applicativa.
def trova_rotta(metodo, percorso):
    return (metodo, percorso) in {("GET", "/health"), ("POST", "/pagamenti")}
print(trova_rotta("GET", "/health"), trova_rotta("GET", "/admin"))
