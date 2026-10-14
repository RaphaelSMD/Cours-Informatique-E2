liste = []
n = int(input("Saisissez un nombre entier : "))
while (n>= 0):
    liste.append(n)
    n=int(input("Ajouter un nombre : "))

print(sorted(liste))
print(min(liste))
print(max(liste))
print(sum(liste)/len(liste))