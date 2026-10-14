import copy
classDict = {
    "class" : {
        "student" : {
            "name" : "Mike" ,
            "marks" : {
                "physics" : 70,
                "history" : 80
            }
        }
    }
}
nom=copy.deepcopy(classDict["class"]["student"]["name"])
#print(nom)

classDict["class"]["student"]["marks"]["physics"] = 89
#print(classDict["class"]["student"])

moy = sum(classDict["class"]["student"]["marks"].values()) / len(classDict["class"]["student"]["marks"])
classDict["class"]["student"]["marks"]["average"] = moy
#print(classDict["class"]["student"]["marks"])

classDict["class"]["student"]=[classDict["class"]["student"]]
#print(classDict["class"]["student"])

Ted = {"name" : "Ted" ,
            "marks" : {
                "physics" : 34,
                "history" : 99
            }
}

moyenneTed=sum(Ted["marks"].values()) / len(Ted["marks"])
#print(moyenneTed)
Ted["marks"]["average"]=moyenneTed
classDict["class"]["student"].append(Ted)
#print(classDict["class"]["student"])

moyennes_eleves = [eleve["marks"]["average"] for eleve in classDict["class"]["student"]]
average_grade = sum(moyennes_eleves) / len(moyennes_eleves)
#print(average_grade)
classDict["class"]["class_average"] = average_grade

print(classDict)
