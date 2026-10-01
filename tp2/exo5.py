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
    po.clear()
print(destruction(polynome))

poly2=[5, 9, 6, 2]
def addition(p1, p2):
    p1_rev = p1[::-1]
    p2_rev = p2[::-1]
    
    res = []
    taille_max = max(len(p1), len(p2))
    
    for i in range(taille_max):
        coeff1 = p1_rev[i] if i < len(p1) else 0
        coeff2 = p2_rev[i] if i < len(p2) else 0
        res.append(coeff1 + coeff2)
    res.reverse()
    return res
print("Poly 1 :", poly)
print("Poly 2 :", poly2)
somme = addition(poly, poly2)
print("Somme des polynômes :", affichage(somme))

def multiplication_monome(p, coeff, degre):
    res = []
    for c in p:
        res.append(c * coeff)
    for i in range(degre):
        res.append(0)
    return res
p_multiplie = multiplication_monome(poly, 3, 2)
print("Résultat :", affichage(p_multiplie))