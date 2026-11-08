# Python per principianti — 220 esempi in italiano

Il percorso contiene 220 esempi autonomi in 21 cartelle tematiche: basi Python, librerie standard, API, database, sicurezza, test e concorrenza. Gli esempi sono didattici e commentati in italiano.

## Requisiti e avvio

Serve Python 3.10 o successivo. Non sono richiesti pacchetti esterni: viene usata la libreria standard.

```bash
python main.py
```

Per eseguire un singolo esempio:

```bash
python esempi/21_api_client/201_get_header_query_path.py
```

Gli esempi 201–220 sono raccolti in `esempi/21_api_client/`. Una guida pratica è disponibile in `esempi/21_api_client/README.md`.

## Abilitare una chiamata API

Le richieste di rete sono disattivate per impostazione predefinita. Per attivare una demo verso un'API di test:

```bash
ESEMPIO_RETE=1 python esempi/21_api_client/201_get_header_query_path.py
```

Gli esempi usano `urllib`, incluso in Python; `API_BASE_URL` può indicare il base URL di un servizio di test autorizzato. Alcuni esempi usano JSONPlaceholder come servizio pubblico dimostrativo. Non inviare credenziali o dati reali a servizi pubblici. I POST/PUT/PATCH/DELETE vanno provati solo su sandbox autorizzate.

## Contenuti API aggiunti

Header e request ID; path parameter codificati; query string; body JSON e form; GET/POST/PATCH/DELETE; Bearer e Basic Auth didattici; gestione errori HTTP/rete e body JSON; controlli status e Content-Type; limiti response; paginazione; timeout e retry limitati; idempotency key; ETag/304; checklist di sicurezza.

## Librerie standard mostrate

`urllib`, `urllib.parse`, `http.server`, `json`, `sqlite3`, `decimal`, `datetime`, `ssl`, `hashlib`, `secrets`, `logging`, `unittest`, `unittest.mock`, `tempfile`, `pathlib`, `asyncio`, `threading`, `queue`, `csv`, `argparse`, `dataclasses`, `enum`, `statistics`, `calendar`, `collections` e altre.

## Nota per contesti bancari/enterprise

Questi esempi sono materiale didattico, non software bancario pronto per la produzione e non sostituiscono revisioni di sicurezza, architettura, compliance o controlli aziendali. Gli esempi DB usano SQLite in memoria; i movimenti sono simulati. Un sistema reale richiede autorizzazioni e segregazione dei ruoli, audit, gestione sicura delle chiavi, cifratura, idempotenza, transazioni e locking adeguati, monitoraggio, test, procedure di recovery e revisione specialistica. Non usare dati reali di clienti o account.
