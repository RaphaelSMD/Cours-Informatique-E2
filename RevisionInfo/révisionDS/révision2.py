import random
def random_election(liste):
    elus = random.sample(liste, 4)
    return {"délégués":elus[:2], "suppléant":elus[2:]}

candidats = ["Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Lucas"]
resultat = random_election(candidats)
print(resultat)