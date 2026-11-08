# Esempio 54 — Un parametro può avere un valore predefinito.
def benvenuto(nome="amico"):
    return f"Benvenuto, {nome}!"
print(benvenuto(), benvenuto("Luca"))
