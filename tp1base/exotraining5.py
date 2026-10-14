liste=[]
notes=float(input("Saisissez la note : "))
while notes >= 0 :
    liste.append(notes)
    notes =float(input("Saisissez la note supplémentaire : "))
print(len(liste))
print(max(liste))
print(min(liste))
print(sum(liste)/len(liste))