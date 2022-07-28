import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://marktran:Hau772001@cluster0.cfll8.mongodb.net/?retryWrites=true&w=majority")

db = cluster["game_cards"]
collection = db["customers"]

post = {
    "_id":5,
    "name":"HAU"
}

results = collection.find({})

for result in results:
    print(result["_id"])

# collection.insert_one(post)

