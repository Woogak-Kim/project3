from pymongo import MongoClient

HOST = 'cluster0.oszyb.mongodb.net'
USER = 'Woogak'
PASSWORD = 'kim1234'
DATABASE_NAME = 'PUBG_Data'
COLLECTION_NAME = 'ANew_Anna_matches'

URI = f"mongodb+srv://{USER}:{PASSWORD}@{HOST}/{DATABASE_NAME}?retryWrites=true&w=majority"

import certifi

client = MongoClient(URI, tlsCAFile=certifi.where())
database = client[DATABASE_NAME]
collection = database[COLLECTION_NAME]
doc = collection.find({})

count = 0
data_list = []
for i in doc:
    count = count + 1
    data_list.append(i)
#    print(i['data']['type'])

