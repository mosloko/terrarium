# Esempio 99 — string.Template sostituisce segnaposto in un testo.
from string import Template
modello = Template("Ciao, $nome!")
print(modello.substitute(nome="Ada"))
