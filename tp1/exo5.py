def conversion():
    nbr_decimal = int(input("Entrer un entier positif : "))
    if nbr_decimal == 0:
        resultat = "0"
    else:
        resultat = ""
        q = nbr_decimal
        while q>0:
            r = q%2
            resultat = (str(r)+resultat)
            q=q//2
    print(f"Le nombre {nbr_decimal} en binaire est : {resultat}")
