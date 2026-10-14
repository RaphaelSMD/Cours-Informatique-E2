def somme_entiers(n : int)-> int :
    if n == 1 :
        return 1
    if n < 1 :
        raise ValueError
    return n + somme_entiers(n-1)

try :
    valeur = int(input("Saisir la valeur souhaité : "))
    resultat = somme_entiers(valeur)
    print(resultat)
except ValueError :
    print("L'entier ne peut pas être inférieur à 1")