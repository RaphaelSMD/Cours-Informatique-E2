import random
def assign_team(liste):
    joueurs = random.sample(liste, 6)
    equipe = {"équipe A":joueurs[:3], "équipe B":joueurs[3:]}
    return equipe
noms = ["Radhouane","Arthur","Rudy","Boubou","Yaghmo","Thibault","Benoit","Nico","Otman"]
resultat = assign_team(noms)
print(resultat)

choix = random.sample(noms, 1)
print(choix)