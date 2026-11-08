# JWT/JWS 237 — JWE protegge la riservatezza; la firma JWS protegge autenticità/integrità.
concetti = {
    "JWS": "firma e integrità; payload normalmente leggibile",
    "JWE": "cifratura per riservatezza; non sostituisce ogni controllo di autorizzazione",
    "JWT": "formato di claim; può essere firmato (JWS) o cifrato (JWE)",
}
for nome, descrizione in concetti.items():
    print(nome, "->", descrizione)
