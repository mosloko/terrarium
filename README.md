# Python per principianti — 200 esempi in italiano

Il percorso contiene **200 esempi autonomi**, organizzati in 20 cartelle tematiche. Gli esempi 1–100 coprono le basi; gli esempi 101–200 introducono API, database, sicurezza, concetti finanziari simulati, test e concorrenza.

## Requisiti e avvio

Serve Python 3.10 o successivo. Non sono richiesti pacchetti esterni: viene usata la libreria standard.

```bash
python main.py
```

Per eseguire un singolo esempio:

```bash
python esempi/11_api_http/101_richiesta_get.py
```

## Nuovi capitoli 101–200

- `11_api_http`: URL, richieste HTTP opt-in, JSON, timeout e token da ambiente.
- `12_api_server`: handler didattici e concetti base di endpoint HTTP.
- `13_dati_validazione`: JSON, controlli input, tipi e contratti.
- `14_database`: SQLite in memoria, SQL parametrizzato e transazioni.
- `15_dominio_bancario`: importi Decimal/centesimi, ledger e idempotenza simulati.
- `16_sicurezza_config`: configurazione e segreti, TLS, hash, input e privilegi.
- `17_affidabilita_osservabilita`: logging, retry, timeout, health check e metriche.
- `18_tempo_importi`: precisione decimale, UTC, date e identificativi.
- `19_test_automazione`: unittest, mock, file temporanei, CSV e CLI.
- `20_concorrenza`: queue, thread, asyncio, generatori e checklist.

## Nota importante su API e servizi esterni

Gli esempi **non contattano servizi esterni per impostazione predefinita**. L'esempio HTTP 101 richiede l'impostazione esplicita di `ESEMPIO_RETE=1`; il 102 usa `API_URL` configurabile. Usa solo sandbox e servizi per cui hai autorizzazione, con timeout. Non inserire mai credenziali nel codice o nei log.

## Nota per contesti bancari/enterprise

Questi esempi sono materiale didattico, non software bancario pronto per la produzione e non sostituiscono revisioni di sicurezza, architettura, compliance o controlli aziendali. Gli esempi DB usano SQLite in memoria; i movimenti sono simulati. Un sistema reale richiede, tra le altre cose, autorizzazioni e segregazione dei ruoli, audit, gestione sicura delle chiavi, cifratura, idempotenza, transazioni e locking adeguati, monitoraggio, test, procedure di recovery e revisione specialistica. Non usare dati reali di clienti o account.

### Librerie standard mostrate

`urllib`, `http.server`, `urllib.parse`, `json`, `sqlite3`, `decimal`, `datetime`, `ssl`, `hashlib`, `secrets`, `logging`, `unittest`, `unittest.mock`, `tempfile`, `pathlib`, `asyncio`, `threading`, `queue`, `csv`, `argparse`, `dataclasses`, `enum`, `statistics`, `calendar`, `collections` e altre.
