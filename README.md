# Python per principianti — 240 esempi in italiano

Il percorso contiene 240 esempi autonomi in 22 cartelle tematiche: basi Python, librerie standard, API, database, sicurezza, test, concorrenza, TLS/mTLS e token JSON. Sono commentati in italiano e hanno finalità didattiche.

## Requisiti e avvio

Serve Python 3.10 o successivo. Per gli esempi di JWT/JWS/JWE installa le dipendenze:

```bash
python -m pip install -r requirements.txt
```

Poi esegui tutti gli esempi con:

```bash
python main.py
```

Gli esempi 221–240 sono in `esempi/22_tls_jwt/`; la guida è in `esempi/22_tls_jwt/README.md`.

## Esempi mTLS

Le richieste di rete restano disattivate per impostazione predefinita. Per abilitarne una servono esplicitamente `ESEMPIO_RETE=1`, endpoint di sandbox autorizzato, CA bundle, certificato client e chiave privata. La chiave non deve essere committata. Le connessioni mantengono la verifica TLS/hostname attiva.

## Sicurezza e uso enterprise

Questi esempi sono materiale didattico, non software bancario pronto per la produzione. Non usare dati o credenziali reali. mTLS, gestione PKI, truststore, JWT/JWS/JWE, algoritmi, rotazione chiavi, audit e autorizzazioni devono seguire i profili e le policy dell'organizzazione ed essere revisionati da specialisti.
