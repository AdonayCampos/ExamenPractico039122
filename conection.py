import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["sis11a-campos-rene"]
collection = db["movies-campos-melendez"]