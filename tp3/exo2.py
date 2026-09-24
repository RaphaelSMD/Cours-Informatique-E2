def Syraccus(nombre):
    assert nombre > 0, "Saisissez un entier valide"
    print(nombre)
    if nombre == 1:
        return nombre
    if nombre%2==0 :
        Syraccus(nombre // 2)
    else :
        Syraccus(nombre*3+1)
    return Syraccus

n=int(input("Saisissez un entier strictement positif : "))
print(Syraccus(n))