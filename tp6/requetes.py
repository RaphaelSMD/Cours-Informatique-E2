from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client.bac
collection = db.resultats

print("Exemple de document :")
print(collection.find_one())