# Python per principianti — 100 esempi in italiano

Ho riorganizzato gli esempi in **100 file Python separati**, raggruppati in 10 cartelle tematiche. Ogni file è un esempio autonomo, numerato e commentato in italiano.

## Requisiti

- Python 3.10 o successivo.
- Nessuna dipendenza esterna: si usano solo Python e la sua libreria standard.

## Avvio

Per eseguire tutti gli esempi in sequenza:

```bash
python main.py
```

Puoi anche eseguire un solo esempio direttamente, per esempio:

```bash
python esempi/01_fondamenta/01_variabili.py
```

Su alcuni sistemi il comando è `python3` invece di `python`.

## Cartelle

- `esempi/01_fondamenta/`: variabili, tipi e operatori.
- `esempi/02_stringhe/`: manipolazione del testo.
- `esempi/03_collezioni/`: liste, tuple, set e dizionari.
- `esempi/04_condizioni/`: confronti e decisioni.
- `esempi/05_cicli/`: ripetizioni, `for`, `while` e strumenti di iterazione.
- `esempi/06_funzioni/`: funzioni, parametri e valori restituiti.
- `esempi/07_strumenti/`: comprehension e utilità per iterare.
- `esempi/08_errori_file/`: eccezioni, file temporanei e JSON.
- `esempi/09_classi/`: classi, oggetti ed ereditarietà.
- `esempi/10_librerie/`: moduli utili della libreria standard.

## Librerie spiegate negli esempi

Sono tutte incluse in Python, quindi non serve installarle: `math` per la matematica, `random` per scelte casuali, `datetime` per date e orari, `statistics` per media e mediana, `pathlib` per i percorsi, `re` per cercare schemi nel testo, `calendar` per calendari, `collections` per contatori, `string` per modelli di testo, `pprint` per stampare strutture dati e `dataclasses` per semplici classi di dati.

Gli esempi sui file usano una cartella temporanea, che viene eliminata automaticamente: non modificano file permanenti.

## Come studiare

Leggi i commenti, prova a prevedere il risultato e poi esegui il file. Modifica i valori per osservare cosa cambia. Puoi cominciare dai primi capitoli e procedere nell'ordine numerico.
