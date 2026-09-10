def plaque_immatriculation():
    nombre =int(input("Saisissez le nombre de plaque d'immatriculation que vous voulez générer : "))
    import random
    lettres = "ABCDEFGHJKLMNPQRSTVWXYZ"
    chiffres = "0123456789"
    for i in range(nombre):
        plaque = "SS"
        while "SS" in plaque:
            plaque=""
            for j in range(2):
                plaque += random.choice(lettres)
            plaque += "-"
            for j in range(3):
                plaque += random.choice(chiffres)
            plaque += "-"
            for j in range(2):
                plaque += random.choice(lettres)
        print(plaque)
plaque_immatriculation()