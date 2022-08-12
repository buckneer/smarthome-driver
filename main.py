
from pymongo import MongoClient
from time import sleep

client = MongoClient("mongodb+srv://buckneer:buckneer2002@cluster0.xyfr1os.mongodb.net/?retryWrites=true&w=majority")
db = client.test
collection = db.sources
cursor = collection.find({})

while True:
    cursor = collection.find({})
    for document in cursor:
        print(document)



    sleep(10)



