import requests
import json

url = "https://api.pubg.com/shards/kakao/players?filter[playerNames]=ANew_Anna"

header = { 
    "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI2YjdmNGI5MC0zOWYyLTAxM2EtNzE4Yy0wOWQzZTk3ZDU4YzYiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNjM4OTI2MTk5LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6ImRyYW5nZWwifQ.lErH1X1rimCNc1ilTkeZXUTJ_-XTg1QnkMSSOS06LiI", 
    "Accept": "application/vnd.api+json"
    }

req = requests.get(url, headers=header)

data = json.loads(req.text) 

from pymongo import MongoClient

HOST = 'cluster0.oszyb.mongodb.net'
USER = 'Woogak'
PASSWORD = 'kim1234'
DATABASE_NAME = 'PUBG_Data'
COLLECTION_NAME = 'Player_data'
MONGO_URI = f"mongodb+srv://{USER}:{PASSWORD}@{HOST}/{DATABASE_NAME}?retryWrites=true&w=majority"

import certifi

client = MongoClient(MONGO_URI, tlsCAFile=certifi.where())
database = client[DATABASE_NAME]
collection = database[COLLECTION_NAME]
collection.insert_one(document=data)