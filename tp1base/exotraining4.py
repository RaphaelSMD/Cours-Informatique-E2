try :
    prixHT=float(input("Saisissez le prix hors taxe du produit : "))
    if prixHT <= 0 :
        raise ValueError
    prixTTC = prixHT * 1.20
    print(prixTTC)
except ValueError :
    print("Le prix ne peut être ni négatif ni égal à zéro")


