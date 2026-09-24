import random 
from tp3.exo4.exceptions import LettreDejaProposeeError

fichier = open("dic.txt", "r", encoding="utf-8")
mots = fichier.readlines()
fichier.close()

liste_de_mots = []
for m in mots:
    mot_nettoyé = m.strip().upper()
    if mot_nettoyé != "":
        liste_de_mots.append(mot_nettoyé)

mot_mystere = random.choice(liste_de_mots)

lettres_deja_jouees = []
vies = 6

premiere_lettre = mot_mystere[0]
lettres_deja_jouees.append(premiere_lettre)

print("=== JEU DU PENDU ===")

while vies > 0:
    print("\n------------------------------")
    
    affichage = ""
    for lettre in mot_mystere:
        if lettre in lettres_deja_jouees:
            affichage = affichage + lettre + " "
        else:
            affichage = affichage + "_ "
            
    print("Mot à deviner :", affichage)
    print("Vies restantes :", vies)

    if "_" not in affichage:
        print("\nBravo ! Vous avez gagné ! Le mot était :", mot_mystere)
        break

    proposition = input("Proposez une lettre : ")
    proposition = proposition.upper()

    if len(proposition) != 1 or not proposition.isalpha():
        print("Veuillez entrer une seule lettre.")
        continue

    try:
        if proposition in lettres_deja_jouees:
            raise LettreDejaProposeeError()

        lettres_deja_jouees.append(proposition)
        if proposition in mot_mystere:
            print("Bonne réponse ! La lettre est dans le mot.")
        else:
            vies = vies - 1
            print("Raté ! La lettre n'est pas dans le mot.")

    except LettreDejaProposeeError:
        print("Erreur : Vous avez déjà proposé cette lettre !")
if vies == 0:
    print("\nDéfaite ! Vous n'avez plus de vie. Le mot était :", mot_mystere)