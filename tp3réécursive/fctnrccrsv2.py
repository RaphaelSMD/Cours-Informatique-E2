def puissance(base : int, exposant : int) -> int :
    if exposant == 0 : return 1
    if exposant == 1 : return base
    if exposant < 0 : raise ValueError
    return base*puissance(base, exposant-1)

try :
    valeur_base = int(input("Quel est la valeur de la base : "))
    valeur_exposant = int(input("Quel est la valeur de l'exposant : "))
    resultat=puissance(valeur_base,valeur_exposant)
    print(resultat)
except ValueError :
    print("L'exposant ne peut pas être négatif")