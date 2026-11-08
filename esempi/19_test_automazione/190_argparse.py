# Esempio 190 — argparse crea interfacce a riga di comando.
import argparse
parser = argparse.ArgumentParser(description="Demo didattica")
parser.add_argument("--ambiente", default="locale")
args = parser.parse_args([])  # Lista vuota: demo deterministica senza leggere argomenti esterni.
print(args.ambiente)
