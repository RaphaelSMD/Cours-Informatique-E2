import random
def unique(liste):
    return len(set(liste))==len(liste)
lst=[]
for i in range(random.randint(2,100)):
    lst.append(random.randint(0,500))
print(unique(lst))

def verifier_tableau():
    n = random.randint(2,100)
    tableau = [random.randint(0,500) for _ in range(n)]
    print(f"Tableau généré ({n} éléments) :", tableau)
    if len(tableau)==len(set(tableau)):
        return "Tous les éléments sont différents."
    else :
        return "Ils ne sont pas tous différents"

print(verifier_tableau())