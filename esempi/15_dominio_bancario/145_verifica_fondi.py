# Esempio 145 — Verificare fondi sufficienti prima di un addebito simulato.
saldo_cent = 5000
addebito_cent = 1200
if addebito_cent <= 0 or addebito_cent > saldo_cent:
    print("Operazione rifiutata")
else:
    print("Operazione demo accettata")
