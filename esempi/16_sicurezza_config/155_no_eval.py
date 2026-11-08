# Esempio 155 — Non usare eval su dati ricevuti da utenti o servizi.
import ast
# literal_eval accetta solo letterali Python; per API usare normalmente JSON.
dato = ast.literal_eval("{'esito': True}")
print(dato)
