from pymongo import MongoClient
database = MongoClient ('mongodb://localhost:27017')
db = database.test
print(db.test)

infoclient = {
 "nom" : "Martin",
 "adresse" : "252 rue des Pyrénées",
 "cp" : "75020",
 "ville" : "Paris"
}
iid = db.test.insert_one(infoclient).inserted_id
print(iid)
infos2 = [
 {
 "nom" : "Richard",
 "adresse" : "27 rue de la Rotonde",
 "cp" : "13001",
 "ville" : "Marseille"
 },
 {
 "nom" : "Picard",
 "adresse" : "18 rue Victor Hugo",
 "cp" : "69002",
 "ville" : "Lyon"
 }
]
print(db.test.insert_many(infos2).inserted_ids)
