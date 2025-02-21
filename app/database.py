import os
import pymongo

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = pymongo.MongoClient(MONGO_URI)
db = client["agente_ai"]
logs_collection = db["logs"]

def salvar_log(acao, detalhes):
    logs_collection.insert_one({"acao": acao, "detalhes": detalhes})
