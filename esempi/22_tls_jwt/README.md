# Esempi didattici: mTLS, truststore dedicato, JWT, JWS e JWE

Questi esempi sono nella cartella `esempi/22_tls_jwt/`, numerati 221–240. Gli esempi crittografici sono locali e generano chiavi RSA effimere in memoria; non usano chiavi o token reali.

## Dipendenze

Dalla radice del progetto installa le librerie necessarie a JWT/JWS/JWE:

```bash
python -m pip install -r requirements.txt
```

- `ssl` e `urllib` sono inclusi in Python e servono per mTLS/TLS.
- `PyJWT[crypto]` firma e verifica JWT/JWS; l'extra crypto fornisce il supporto crittografico RSA.
- `jwcrypto` dimostra JWS e JWE.

Gli esempi relativi alle librerie esterne mostrano un messaggio se le dipendenze non sono installate.

## mTLS e truststore

mTLS autentica sia il server sia il client durante TLS. Usa un certificato client di test e una chiave privata ottenuti dalla PKI autorizzata. Non aggiungere certificati/chiavi al repository.

```bash
export ESEMPIO_RETE=1
export MTLS_URL=https://api.sandbox.example.test/health
export TLS_CA_BUNDLE=/percorso/sicuro/ca-bundle.pem
export MTLS_CLIENT_CERT=/percorso/sicuro/client-cert.pem
export MTLS_CLIENT_KEY=/percorso/sicuro/client-key.pem
python esempi/22_tls_jwt/222_truststore_dedicato.py
```

Su PowerShell imposta le stesse variabili con `$env:NOME = "valore"`. L'esempio 221 usa il truststore CA predefinito del sistema; il 222 usa il bundle PEM dedicato. Entrambi mantengono attiva la verifica certificati e hostname. Non usare mai `CERT_NONE`, `check_hostname = False` o workaround analoghi.

## JWT, JWS e JWE

- **JWT** è un formato di claim che può essere protetto con JWS oppure JWE.
- **JWS** fornisce firma e integrità; il payload di un JWS compatto non è cifrato e si può leggere.
- **JWE** fornisce cifratura per riservatezza; in genere usa cifratura ibrida (chiave destinatario + cifratura autenticata dei dati).

Esempi locali: 226–229 JWT con RS256 e validazione claim; 230–234 firma JWS, verifica e chiavi; 235–236 cifratura/decifratura JWE.

In produzione imposta sempre una allowlist di algoritmi, verifica firma, `iss`, `aud`, `exp` e gli altri claim richiesti dal protocollo. Le chiavi reali vanno in KMS/HSM o secret manager, con rotazione e controllo accessi; non generare o conservare chiavi di produzione come negli esempi didattici.

Questi esempi non sono un'implementazione pronta per sistemi bancari: seguire i profili, requisiti PKI, standard e policy di sicurezza dell'organizzazione e farli revisionare.
