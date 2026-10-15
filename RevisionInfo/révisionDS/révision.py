def decalage_cesar(cle : str, phrase : str):
    cle = cle.upper()
    phrase=phrase.upper()
    resultat = ""
    for i in range(len(phrase)):
        c=cle[i%len(cle)]
        decalage = ord(c) - ord("A")+1
        code = ord(phrase[i])-ord("A")
        nouveau_code = (code + decalage) % 26
        resultat += chr(nouveau_code + ord("A"))
    return resultat

cle_test = "AB"
phrase_test = "BONJOUR"

message_code = decalage_cesar(cle_test, phrase_test)
print(message_code)