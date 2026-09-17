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
print(nom)