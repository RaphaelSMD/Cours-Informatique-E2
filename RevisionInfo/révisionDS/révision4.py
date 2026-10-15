def chiffre_rotatif(cle, phrase):
    cle = cle.upper()
    phrase = phrase.upper()
    r=""
    for i in range(len(phrase)):
        c=cle[i%len(cle)]
        d=(ord(c)-ord("A"))+1
        code=(ord(phrase[i])-ord("A"))
        n=(code - d) % 26
        r += chr(n+ord("A"))
    return r
cle_test = "AB"
phrase_test = "BONJOUR"
resultat=chiffre_rotatif(cle_test, phrase_test)
print(resultat)