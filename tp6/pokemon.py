from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017")
db = client.pokemon
dresseurs = db.dresseurs

sandra = {
    "nom" : "Sandra",
    "titre" : "Championne Arène Ebènelle",
    "spécialité" : "Dragon",
    "badge" : "Badge Lever",
    "ligue" : "Johto",
    "récompense" : " 4000",
    "équipe" : [{"nom" : "Draco", "niveau":38, "type" : ["Dragon"]},
                {"nom" : "Léviator", "niveau":38, "type" : ["Eau","Vol"]},
                {"nom" : "Hyporoi", "niveau":41, "type" : ["Eau", "Dragon"]}
    ]
}   

sacha = {
    "nom": "Sacha",
    "titre" : "Maître Pokémon",
    "spécialité" : "Eclair",
    "badge" : "Badge Baisser",
    "ligue" : "Loto",
    "récompense" : " 10 000",
    "équipe" : [{"nom" : "Pikachu", "niveau":65, "type" : ["Eclair"]},
                {"nom" : "Dracauloss", "niveau":45, "type" : ["Dragon"]},
                {"nom" : "Riolu", "niveau":28, "type" : ["Combat"]}
    ]
}   

dresseurs.insert_many([sandra,sacha])
print("Les dresseurs sont ajoutés !")

print("\nListe des dresseurs")
for d in dresseurs.find().limit(2):
    print(f"- {d["nom"]}({d["ligue"]} - Badge : {d["badge"]})")