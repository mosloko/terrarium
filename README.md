# Python per principianti — 100 esempi in italiano

Un piccolo percorso pratico per imparare Python leggendo ed eseguendo esempi brevi, con commenti e spiegazioni in italiano.

## Requisiti

- Python 3.10 o successivo
- Non servono pacchetti da installare: gli esempi usano Python e la sua **libreria standard**.

## Avvio

Dalla cartella del progetto, esegui:

```bash
python esempi.py
```

Su alcuni sistemi il comando può essere `python3 esempi.py`.

Il programma mostra tutti gli esempi in sequenza. Puoi anche aprire `esempi.py` e studiare o modificare un esempio alla volta. Se vuoi eseguire un singolo esempio, commenta temporaneamente le altre sezioni oppure copia il codice in un file nuovo.

## Percorso di studio

Gli esempi sono raggruppati in dieci capitoli: variabili e tipi, stringhe, collezioni, condizioni e cicli, funzioni, comprensioni, eccezioni, file e JSON, classi, moduli e librerie standard.

## Librerie usate

Tutte le librerie mostrate fanno parte della **libreria standard di Python**: non devi installarle separatamente.

- `math`: funzioni e costanti matematiche.
- `random`: scelta e generazione casuale; i risultati cambiano a ogni esecuzione.
- `datetime`: date e orari.
- `json`: conversione tra dati Python e testo JSON.
- `statistics`: calcoli statistici semplici.
- `collections`: strutture dati aggiuntive, come `Counter`.
- `pathlib`: rappresentazione e manipolazione dei percorsi dei file.
- `re`: ricerca di schemi nel testo tramite espressioni regolari.
- `tempfile`: file temporanei, rimossi automaticamente quando si chiude il contesto.

## Suggerimenti

1. Leggi il commento prima di eseguire il codice.
2. Cambia i valori e osserva come cambia il risultato.
3. Prova a prevedere il risultato prima di avviare il programma.
4. Se qualcosa non è chiaro, usa `print()` per visualizzare i valori intermedi.

Gli esempi non richiedono rete, non chiedono input e non modificano file permanenti. L'esempio sui file usa un file temporaneo che viene eliminato automaticamente.
