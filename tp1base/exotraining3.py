
age =int(input("Saisissez l'âge de l'humain : "))
if age > 0 :
    if age > 2 :
        age_canin = 21+((age -2)*4)
    else :
        age_canin = age * 10.5
    print(f"Votre âge canin est de {age_canin}")
else :
    print("l'age doit être positif")