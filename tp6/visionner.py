from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client.bac
collection = db.resultats

print("2 premiers documents liés à l'académie de Normandie : ")
for doc in collection.find({"academie": "NORMANDIE"}).limit(2):
    print(doc)

print("\n2. Liste des académies : ")
academies = collection.distinct("academie")
print(academies)

print("\n3. Top 10 séries garçons : ")
top_garcons = collection.find({"sexe": "MASCULIN"}).sort("nombre_d_inscrits", -1).limit(10)
for doc in top_garcons:
    print(f"{doc['academie']} - {doc['serie']} - {doc['nombre_d_inscrits']}")

print("\n4. Nombre de filles par académie")
pipeline = [
    {"$match": {"sexe": "FEMININ"}},
    {"$group": {"_id": "$academie", "total_filles": {"$sum": "$nombre_d_inscrits"}}}
]
for res in collection.aggregate(pipeline):
    print(f"{res['_id']} : {res['total_filles']}")