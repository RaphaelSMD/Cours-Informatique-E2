import random
def tableau_pair():
    tab=[]
    n = random.randint(2,100)
    tableau = [random.randint(0,500) for i in range(n)]
    print(f"Le Tableau généré avec {n} éléments", tableau)
    for nombre in tableau :
        if nombre%2 == 0 :
            tab.append(nombre)
    return tab
resultat = tableau_pair()
print("Tableau des pairs", resultat)
print("Nombre d'éléments pairs", len(resultat))