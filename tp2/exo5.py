def ajouter_coefficient(poly: list, coeff: int) -> list:
    poly.insert(0, coeff)
    return poly
poly=[10, 5, 3]
poly=ajouter_coefficient(poly,4)
print(poly)

def pol(n):
    pol=[]
    for i in range(n+1):
        pol=pol+[int(input("Valeur : "))]
    return pol
print(pol(int(input("Degré du polynôme : "))))

polynome=pol(int(input("Degré du polynôme : ")))
def affichage(pol):
    polyn=""
    o=len(pol)-1
    for i in range(len(pol)-1):
        polyn=polyn+str(pol[i])+"x^"+str(o)+"+"
        o -=1
    polyn=polyn+str(pol[len(pol)-1])
    return polyn
print(affichage(polynome))

def destruction(po):
    p=[]
    return p
print(destruction(polynome))

def addition(pol1, pol2):
    somme=sum(pol1,pol2)
    return somme
print(addition(poly, polynome))