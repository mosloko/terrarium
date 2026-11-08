# Esempio 189 — Il modulo csv legge dati tabellari senza librerie esterne.
import csv
from io import StringIO
righe = list(csv.DictReader(StringIO("id,stato\n1,ok\n")))
print(righe)
