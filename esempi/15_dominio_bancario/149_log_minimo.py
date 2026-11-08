# Esempio 149 — Non registrare numeri completi di carta o credenziali nei log.
def log_operazione(riferimento, stato):
    print({"riferimento": riferimento, "stato": stato})
log_operazione("demo-42", "accettato")
