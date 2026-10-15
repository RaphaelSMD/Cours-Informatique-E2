age=int(input("Saisissez votre âge : "))
assert age > 0, "entrer un âge valide"
if age <= 4 :
    print("C'est gratuit !")
elif 5 <= age <= 17:
    print("Le tarif est de 7$")
elif 18 <= age <= 64:
    print("Le tarif est de 12$")
elif age >= 65 :
    print("Le tarif est de 9$")
