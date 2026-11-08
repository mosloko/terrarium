# JWT/JWS 238 — Non accettare algoritmo scelto liberamente dal token.
# La verifica deve imporre una lista corta e configurata di algoritmi attesi.
algoritmi_ammessi = ["RS256"]
header_non_fidato = {"alg": "none"}
if header_non_fidato.get("alg") not in algoritmi_ammessi:
    print("Algoritmo rifiutato prima della verifica")
# Con PyJWT passare sempre algorithms=[...]; mai derivarlo dall'header non fidato.
