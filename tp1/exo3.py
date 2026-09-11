def âge():
    humain = int(input("Entrer l'âge de l'humain : "))
    if humain < 0:
        print("l'âge ne peut pas être négatif.")
    else:
        if humain <= 2:
            canin = humain * 10.5
        else:
            canin = 21 + (humain - 2) * 4
    print(f"L'équivalent en âge canine est : {canin}")
âge()