nombres = []
while True :
    valeur = int(input("Entrer un nombre entier : "))
    if valeur < 0 :
        break
    nombres.append(valeur)

if nombres :
    nombres.sort()

    minimum = nombres[0]
    maximum = nombres[-1]
    moyenne = sum(nombres) / len(nombres)

    print("\n--- Résultats ---")
    print(f"Nombres triés : {nombres}")
    print(f"Minimum : {minimum}")
    print(f"Maximum : {maximum}")
    print(f"Moyenne : {moyenne}")
else :
    print("Aucun nombre valide n'a été saisi.")
