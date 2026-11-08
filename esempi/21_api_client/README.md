# Aggiunge esempi pratici su chiamate client HTTP.

Dal progetto esegui:

```bash
python esempi/21_api_client/201_get_header_query_path.py
```

Per autorizzare esplicitamente le richieste di rete (verso un'API di test):

```bash
ESEMPIO_RETE=1 python esempi/21_api_client/201_get_header_query_path.py
```

Su Windows PowerShell:

```powershell
$env:ESEMPIO_RETE = "1"
python esempi/21_api_client/201_get_header_query_path.py
```

Le demo usano `urllib`, incluso in Python; non richiedono `requests` o altri pacchetti. `API_BASE_URL` permette di configurare l'host. Non inviare token o dati reali a servizi pubblici; usa sandbox autorizzate. Il server JSONPlaceholder è una API pubblica dimostrativa: le scritture sono simulate e non persistenti.

Gli esempi illustrano header, query string, path parameter, body JSON/form, metodi HTTP, codici di stato, parsing e validazione delle response, gestione HTTPError/URLError, limiti del body, timeout, retry, paginazione, cache condizionale e autenticazione. Il runner `python main.py` li include; i casi di rete restano disattivati senza opt-in.
