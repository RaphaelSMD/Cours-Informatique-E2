import random

def verifier_tableau():
    n = random.randint(2, 100)
    tableau = [random.randint(0, 500) for _ in range(n)]
    print(f"Tableau généré ({n} éléments) :", tableau)
    if len(tableau) == len(set(tableau)):
        return "Tous les éléments sont différents."
    else:
        return "Ils ne sont pas tous différents (il y a au moins un doublon)."

print(verifier_tableau())