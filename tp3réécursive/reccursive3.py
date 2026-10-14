def inverser_chaine(texte : str) -> str :
    if texte == "" : return ""
    return texte[-1] + inverser_chaine(texte[:-1])

try :
    texte = input("Saisissez votre texte : ")
    if texte == "":
        raise ValueError("Le texte ne peut pas être vide")
    inverse = inverser_chaine(texte)
    print(inverse)
except ValueError :
    print("Il faut saisir au minimum une lettre")