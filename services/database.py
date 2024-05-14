import pymongo

client      = pymongo.MongoClient("mongodb://localhost:27017/")
db          = client["plataforma_colaborativa"]

user_collection = db["usuario"]
user_collection.create_index([('cpf', pymongo.ASCENDING)], unique=True)
