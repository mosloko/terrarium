"""100 esempi fondamentali di Python, commentati in italiano.

Esegui questo file con `python esempi.py`. Gli esempi sono autonomi e
utilizzano soltanto Python e la sua libreria standard.
"""

print("\nPYTHON PER PRINCIPIANTI — 100 ESEMPI\n")

# CAPITOLO 1 — Variabili, tipi e operatori
print("\n--- 1. Variabili, tipi e operatori ---")

# Esempio 001: una variabile dà un nome a un valore.
nome = "Ada"
print("001:", nome)

# Esempio 002: Python riconosce i numeri interi (int).
eta = 36
print("002:", eta, type(eta).__name__)

# Esempio 003: un numero con la virgola è un float; in Python si scrive col punto.
prezzo = 2.50
print("003:", prezzo, type(prezzo).__name__)

# Esempio 004: una stringa è testo racchiuso tra virgolette.
saluto = "Ciao!"
print("004:", saluto, type(saluto).__name__)

# Esempio 005: bool può avere valore True oppure False.
ha_finito = False
print("005:", ha_finito, type(ha_finito).__name__)

# Esempio 006: assegnare un nuovo valore aggiorna la variabile.
punteggio = 10
punteggio = punteggio + 5
print("006:", punteggio)

# Esempio 007: Python supporta le operazioni aritmetiche usuali.
print("007:", 8 + 3, 8 - 3, 8 * 3)

# Esempio 008: / fa la divisione, // la divisione intera, % il resto.
print("008:", 8 / 3, 8 // 3, 8 % 3)

# Esempio 009: ** eleva un numero a potenza.
print("009:", 2 ** 5)

# Esempio 010: int(), float() e str() convertono valori compatibili.
numero = int("42")
print("010:", numero, float(numero), str(numero))

# CAPITOLO 2 — Stringhe
print("\n--- 2. Stringhe ---")

# Esempio 011: len() restituisce il numero di caratteri.
parola = "Python"
print("011:", len(parola))

# Esempio 012: gli indici partono da zero; -1 indica l'ultimo carattere.
print("012:", parola[0], parola[-1])

# Esempio 013: uno slice seleziona una parte della stringa.
print("013:", parola[1:4])

# Esempio 014: upper() e lower() cambiano maiuscole e minuscole.
print("014:", parola.upper(), parola.lower())

# Esempio 015: strip() rimuove spazi ai bordi del testo.
testo = "  ciao  "
print("015:", repr(testo.strip()))

# Esempio 016: replace() sostituisce una parte della stringa.
print("016:", "gatto nero".replace("nero", "bianco"))

# Esempio 017: in controlla se un testo è contenuto in un altro.
print("017:", "thon" in parola)

# Esempio 018: una f-string inserisce valori dentro una stringa.
print(f"018: Mi chiamo {nome} e ho {eta} anni.")

# Esempio 019: split() divide una stringa in una lista di parole.
print("019:", "uno due tre".split())

# Esempio 020: join() unisce stringhe usando un separatore.
print("020:", " - ".join(["uno", "due", "tre"]))

# CAPITOLO 3 — Liste, tuple, set e dizionari
print("\n--- 3. Collezioni ---")

# Esempio 021: una lista è ordinata e può essere modificata.
frutti = ["mela", "pera", "kiwi"]
print("021:", frutti)

# Esempio 022: si accede agli elementi di una lista tramite indice.
print("022:", frutti[1])

# Esempio 023: append() aggiunge un elemento alla fine.
frutti.append("banana")
print("023:", frutti)

# Esempio 024: remove() elimina il primo elemento uguale al valore indicato.
frutti.remove("pera")
print("024:", frutti)

# Esempio 025: sort() ordina la lista sul posto.
numeri = [4, 1, 3, 2]
numeri.sort()
print("025:", numeri)

# Esempio 026: sorted() restituisce una lista ordinata senza cambiare l'originale.
originale = [3, 1, 2]
print("026:", sorted(originale), "originale:", originale)

# Esempio 027: una tupla è ordinata ma non può essere modificata.
punto = (4, 7)
print("027:", punto, "x =", punto[0])

# Esempio 028: un set conserva valori unici, senza garantire un ordine.
colori = {"rosso", "blu", "rosso"}
print("028:", colori)

# Esempio 029: un dizionario associa chiavi a valori.
persona = {"nome": "Lina", "citta": "Roma"}
print("029:", persona["nome"])

# Esempio 030: get() permette di cercare una chiave senza errore se manca.
print("030:", persona.get("eta", "non specificata"))

# Esempio 031: si può aggiungere o aggiornare una coppia chiave-valore.
persona["eta"] = 28
print("031:", persona)

# Esempio 032: items() permette di visitare chiavi e valori.
for chiave, valore in persona.items():
    print("032:", chiave, "->", valore)

# Esempio 033: len() conta gli elementi di una collezione.
print("033:", len(frutti), len(persona))

# Esempio 034: in controlla la presenza di un elemento o di una chiave.
print("034:", "mela" in frutti, "nome" in persona)

# Esempio 035: unpacking assegna gli elementi a più variabili.
primo, secondo = ("sole", "luna")
print("035:", primo, secondo)

# CAPITOLO 4 — Condizioni e cicli
print("\n--- 4. Condizioni e cicli ---")

# Esempio 036: if esegue un blocco solo quando la condizione è vera.
numero = 7
if numero > 0:
    print("036: il numero è positivo")

# Esempio 037: else definisce cosa fare quando if è falso.
if numero % 2 == 0:
    print("037: pari")
else:
    print("037: dispari")

# Esempio 038: elif controlla condizioni alternative in ordine.
voto = 8
if voto >= 9:
    giudizio = "ottimo"
elif voto >= 6:
    giudizio = "sufficiente"
else:
    giudizio = "da riprovare"
print("038:", giudizio)

# Esempio 039: and richiede che entrambe le condizioni siano vere.
print("039:", eta >= 18 and eta < 100)

# Esempio 040: or è vero se almeno una delle condizioni è vera.
print("040:", numero < 0 or numero > 5)

# Esempio 041: not inverte un valore booleano.
print("041:", not False)

# Esempio 042: for visita ogni elemento di una collezione.
for animale in ["gatto", "cane"]:
    print("042:", animale)

# Esempio 043: range(5) produce i numeri da 0 a 4.
for indice in range(5):
    print("043:", indice, end=" ")
print()

# Esempio 044: range può indicare inizio, fine e passo.
print("044:", list(range(2, 10, 2)))

# Esempio 045: while ripete il blocco finché la condizione è vera.
contatore = 0
while contatore < 3:
    print("045:", contatore, end=" ")
    contatore += 1
print()

# Esempio 046: break interrompe un ciclo.
for valore in range(10):
    if valore == 3:
        break
    print("046:", valore, end=" ")
print()

# Esempio 047: continue salta il resto del giro corrente.
for valore in range(4):
    if valore == 2:
        continue
    print("047:", valore, end=" ")
print()

# Esempio 048: enumerate() fornisce sia l'indice sia il valore.
for indice, frutto in enumerate(["mela", "kiwi"], start=1):
    print("048:", indice, frutto)

# Esempio 049: zip() abbina elementi di più sequenze.
for nome_persona, altezza in zip(["Ada", "Lina"], [1.65, 1.72]):
    print("049:", nome_persona, altezza)

# Esempio 050: sum(), min() e max() lavorano su sequenze di numeri.
dati = [4, 8, 2, 6]
print("050:", sum(dati), min(dati), max(dati))

# CAPITOLO 5 — Funzioni
print("\n--- 5. Funzioni ---")

# Esempio 051: def crea una funzione riutilizzabile.
def saluta():
    return "Ciao!"
print("051:", saluta())

# Esempio 052: i parametri ricevono dati quando chiamiamo la funzione.
def saluta_nome(nome):
    return f"Ciao, {nome}!"
print("052:", saluta_nome("Ada"))

# Esempio 053: return restituisce il risultato di una funzione.
def somma(a, b):
    return a + b
print("053:", somma(3, 4))

# Esempio 054: un parametro può avere un valore predefinito.
def benvenuto(nome="amico"):
    return f"Benvenuto, {nome}!"
print("054:", benvenuto(), benvenuto("Luca"))

# Esempio 055: gli argomenti possono essere specificati per nome.
def descrivi(nome, citta):
    return f"{nome} vive a {citta}."
print("055:", descrivi(citta="Torino", nome="Mia"))

# Esempio 056: una funzione può restituire più valori, raccolti in una tupla.
def dividi(a, b):
    return a // b, a % b
quoziente, resto = dividi(10, 3)
print("056:", quoziente, resto)

# Esempio 057: una variabile creata dentro una funzione è locale.
def esempio_locale():
    messaggio = "esisto dentro la funzione"
    return messaggio
print("057:", esempio_locale())

# Esempio 058: lambda crea una breve funzione anonima.
doppio = lambda valore: valore * 2
print("058:", doppio(6))

# Esempio 059: le funzioni possono usare altre funzioni.
def quadrato(valore):
    return valore * valore
print("059:", quadrato(somma(2, 3)))

# Esempio 060: una docstring descrive lo scopo di una funzione.
def area_rettangolo(base, altezza):
    """Restituisce l'area di un rettangolo."""
    return base * altezza
print("060:", area_rettangolo(5, 3), "—", area_rettangolo.__doc__)

# CAPITOLO 6 — Comprensioni e strumenti per iterare
print("\n--- 6. Comprensioni e iterazioni ---")

# Esempio 061: una list comprehension costruisce una lista in modo conciso.
quadrati = [n * n for n in range(5)]
print("061:", quadrati)

# Esempio 062: una comprehension può includere una condizione.
pari = [n for n in range(10) if n % 2 == 0]
print("062:", pari)

# Esempio 063: una dict comprehension costruisce un dizionario.
quadrati_dict = {n: n * n for n in range(4)}
print("063:", quadrati_dict)

# Esempio 064: una set comprehension crea un insieme di valori unici.
resti = {n % 3 for n in range(8)}
print("064:", resti)

# Esempio 065: map() applica una funzione a ogni elemento.
print("065:", list(map(str.upper, ["ciao", "python"])))

# Esempio 066: filter() mantiene gli elementi che superano un test.
print("066:", list(filter(lambda n: n > 3, [1, 2, 3, 4, 5])))

# Esempio 067: reversed() permette di iterare in ordine inverso.
print("067:", list(reversed([1, 2, 3])))

# Esempio 068: any() è vero se almeno un elemento è vero.
print("068:", any([False, False, True]))

# Esempio 069: all() è vero se tutti gli elementi sono veri.
print("069:", all([True, True, True]))

# Esempio 070: sorted() può ordinare usando una chiave personalizzata.
parole = ["sole", "arcobaleno", "mare"]
print("070:", sorted(parole, key=len))

# CAPITOLO 7 — Eccezioni e debugging
print("\n--- 7. Eccezioni ---")

# Esempio 071: try/except gestisce un errore previsto.
try:
    risultato = 10 / 0
except ZeroDivisionError:
    risultato = "non si può dividere per zero"
print("071:", risultato)

# Esempio 072: diverse eccezioni possono essere gestite separatamente.
for testo_numero in ["12", "non è un numero"]:
    try:
        print("072:", int(testo_numero))
    except ValueError:
        print("072: conversione non riuscita")

# Esempio 073: else viene eseguito se non si verifica un'eccezione.
try:
    valore = int("25")
except ValueError:
    print("073: testo non valido")
else:
    print("073:", valore)

# Esempio 074: finally viene eseguito sia in caso di successo sia di errore.
try:
    print("074: operazione conclusa")
finally:
    print("074: questo messaggio appare comunque")

# Esempio 075: raise genera un'eccezione intenzionalmente.
def controlla_eta(valore):
    if valore < 0:
        raise ValueError("L'età non può essere negativa")
    return valore
try:
    controlla_eta(-1)
except ValueError as errore:
    print("075:", errore)

# Esempio 076: assert verifica una condizione durante lo sviluppo.
assert 2 + 2 == 4
print("076: il controllo assert è superato")

# Esempio 077: controllare i dati prima del calcolo evita errori.
def media(valori):
    if not valori:
        return None
    return sum(valori) / len(valori)
print("077:", media([]), media([2, 4, 6]))

# Esempio 078: type() mostra il tipo; isinstance() verifica una famiglia di tipi.
print("078:", type(3.5).__name__, isinstance(True, int))

# Esempio 079: repr() mostra una rappresentazione utile anche per gli spazi.
print("079:", repr("  testo\n"))

# Esempio 080: help() è utile nella console interattiva; qui mostriamo una docstring.
print("080:", area_rettangolo.__doc__)

# CAPITOLO 8 — File e dati JSON
print("\n--- 8. File e JSON ---")

# Esempio 081: open() con modalità w scrive un file; encoding specifica UTF-8.
# tempfile crea un file temporaneo che viene eliminato alla chiusura del contesto.
import tempfile
from pathlib import Path
with tempfile.TemporaryDirectory() as cartella_temporanea:
    percorso = Path(cartella_temporanea) / "nota.txt"
    with percorso.open("w", encoding="utf-8") as file:
        file.write("Ciao dal file!\n")
    print("081: file di testo scritto")

# Esempio 082: il file si legge con modalità r; il contesto lo chiude automaticamente.
    with percorso.open("r", encoding="utf-8") as file:
        contenuto = file.read()
    print("082:", contenuto.strip())

# Esempio 083: read_text() è una scorciatoia di pathlib per leggere testo.
    print("083:", percorso.read_text(encoding="utf-8").strip())

# Esempio 084: write_text() scrive testo; questo file è sempre temporaneo.
    altra_nota = Path(cartella_temporanea) / "altra_nota.txt"
    altra_nota.write_text("Seconda nota", encoding="utf-8")
    print("084:", altra_nota.read_text(encoding="utf-8"))

# Esempio 085: json.dumps() converte un oggetto Python in testo JSON.
import json
persona_json = {"nome": "Ada", "attiva": True, "punteggi": [8, 10]}
testo_json = json.dumps(persona_json, ensure_ascii=False)
print("085:", testo_json)

# Esempio 086: json.loads() riconverte il testo JSON in dati Python.
print("086:", json.loads(testo_json)["nome"])

# Esempio 087: indent rende il JSON più leggibile.
print("087:\n", json.dumps(persona_json, ensure_ascii=False, indent=2))

# Esempio 088: Path.name restituisce il nome finale del percorso.
percorso_esempio = Path("appunti/lezione.txt")
print("088:", percorso_esempio.name)

# Esempio 089: Path.suffix restituisce l'estensione del file.
print("089:", percorso_esempio.suffix)

# Esempio 090: un percorso si può comporre usando l'operatore / di pathlib.
print("090:", Path("dati") / "risultati.txt")

# CAPITOLO 9 — Classi e oggetti
print("\n--- 9. Classi e oggetti ---")

# Esempio 091: una classe descrive un tipo di oggetto.
class Persona:
    pass
print("091:", Persona.__name__)

# Esempio 092: __init__ inizializza i dati di un nuovo oggetto.
class Animale:
    def __init__(self, nome):
        self.nome = nome

gatto = Animale("Milo")
print("092:", gatto.nome)

# Esempio 093: un metodo è una funzione definita dentro una classe.
class Salvadanaio:
    def __init__(self, monete=0):
        self.monete = monete
    def aggiungi(self, quantita):
        self.monete += quantita

salvadanaio = Salvadanaio()
salvadanaio.aggiungi(3)
print("093:", salvadanaio.monete)

# Esempio 094: __str__ controlla la versione leggibile dell'oggetto.
class Libro:
    def __init__(self, titolo):
        self.titolo = titolo
    def __str__(self):
        return f"Libro: {self.titolo}"
print("094:", Libro("Il piccolo principe"))

# Esempio 095: una classe figlia può ereditare da una classe genitore.
class Veicolo:
    def muovi(self):
        return "Il veicolo si muove"
class Bicicletta(Veicolo):
    pass
print("095:", Bicicletta().muovi())

# Esempio 096: un metodo di una classe figlia può specializzare quello ereditato.
class Cane(Animale):
    def verso(self):
        return "bau"
print("096:", Cane("Luna").verso())

# Esempio 097: una dataclass riduce il codice per oggetti che contengono dati.
from dataclasses import dataclass
@dataclass
class Punto:
    x: int
    y: int
print("097:", Punto(2, 5))

# Esempio 098: isinstance() verifica se un oggetto appartiene a una classe.
print("098:", isinstance(gatto, Animale))

# CAPITOLO 10 — Moduli e libreria standard
print("\n--- 10. Moduli e libreria standard ---")

# Esempio 099: math fornisce costanti e funzioni matematiche.
import math
print("099:", math.sqrt(81), math.pi)

# Esempio 100: statistics calcola statistiche; datetime rappresenta date e orari.
import statistics
from datetime import date
valori_statistici = [2, 4, 4, 6]
print("100: media =", statistics.mean(valori_statistici), "oggi =", date.today())

# Altri strumenti standard utili (approfondimento oltre i 100 esempi):

# random fa scelte casuali; il risultato cambia a ogni esecuzione.
import random
print("Extra — random:", random.choice(["rosso", "verde", "blu"]))

# Counter conta quante volte appare ogni elemento.
from collections import Counter
print("Extra — Counter:", Counter("banana"))

# re cerca schemi nel testo; qui cerca un indirizzo email semplice.
import re
indirizzo = re.search(r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}", "scrivi a ciao@example.com")
print("Extra — re:", indirizzo.group() if indirizzo else "nessun indirizzo trovato")

print("\nFine: hai visto 100 esempi fondamentali e alcuni strumenti extra!\n")
