bibliotheque = {
    "section_romans": {
        "livre_1": {
            "titre": "Les Misérables",
            "auteur": "Victor Hugo",
            "details": {
                "annee": 1862,
                "prix": 15.50
            }
        }
    }
}

bibliotheque['section_romans']['livre_1']['details']['annee']=1864
bibliotheque['section_romans']['livre_1']['stock'] = 12
bibliotheque['section_romans']['livre_2']={"titre" : "Le Petit Prince", "auteur" : "Antoine de Saint-Exupery", "details" : { "annee" : 1943, "prix" : 9.90}}
bibliotheque['total_livres'] = len(bibliotheque['section_romans'])
print(bibliotheque)