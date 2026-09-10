def operation():
    choix = input("Choisissez une opération (a)ddition, (s)oustraction, (m)ultiplication, (d)ivision : ")
    nbr1 = int(input("Saisissez le premier nombre : "))
    nbr2 = int(input("Saisissez le deuxième nombre : "))
    if choix == 'a':
        print("Tu as choisi l'addition.")
        choix = '+'
        result = nbr1 + nbr2
    elif choix == 's':
        print("Tu as choisi la soustraction.")
        choix = '-'
        result = nbr1 - nbr2
    elif choix == 'm':
        print("Tu as choisi la multiplication.")
        choix = '*'
        result = nbr1 * nbr2
    elif choix == 'd':
        print("Tu as choisi la division.")
        choix = '/'
        result = nbr1 / nbr2
        if choix == 'd' and nbr2 == 0:
            print("Erreur : Division par zéro.")
    else:
        print("Choix invalide. Veuillez choisir parmis a,s,m,d.")

    print(f"Le résultat de l'opération est : {nbr1} {choix} {nbr2} = {result}")
operation()
