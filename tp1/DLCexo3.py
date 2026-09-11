import random
import itertools

def carte():
    VALEURS = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "V", "C", "D", "R", "A"]
    ENSEIGNES = ["♠", "♥", "♦", "♣"] 
    jeu_de_cartes = [f"{valeur}{enseigne}" for valeur, enseigne in itertools.product(VALEURS, ENSEIGNES)]
    return(jeu_de_cartes[:])

def point():
    VALEURS = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "V", "C", "D", "R", "A"]
    jeu = carte()
    random.shuffle(jeu)
    p = 0
    mp = 0
    for t in range(10):
        c1 = jeu[t]
        c2 = jeu[t+1]
        print(c1)
        choix = input("La prochaine carte est supérieur ou inférieur ? : ")
        print(f"La carte était : {c2}")
        val1 = VALEURS.index(c1[:-1])
        val2 = VALEURS.index(c2[:-1])
        if choix == "supérieur" and val2 > val1:
            print("Vous avez gagné un point !")
            p = p + 1
        elif choix == "inférieur" and val2 < val1:
            print("Vous avez gagné un point !")
            p = p + 1
        else:
            print("Je gagne un point !")
            mp = mp + 1
    print(f"Vous avez {p} points !")
    print(f"Moi j'ai {mp} points !")
    if input("Rejouer ? (oui/non) : ") == "oui":
        point()
point()