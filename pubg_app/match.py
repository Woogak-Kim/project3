import requests
import json

url = "https://api.pubg.com/shards/steam/players?filter[playerNames]=YY3676--YuanBao"

header = { 
    "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI2YjdmNGI5MC0zOWYyLTAxM2EtNzE4Yy0wOWQzZTk3ZDU4YzYiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNjM4OTI2MTk5LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6ImRyYW5nZWwifQ.lErH1X1rimCNc1ilTkeZXUTJ_-XTg1QnkMSSOS06LiI", 
    "Accept": "application/vnd.api+json"
    }


req = requests.get(url, headers=header)

player_data = json.loads(req.text) 

match_list = player_data['data'][0]['relationships']['matches']['data']

list_id = []
for match in match_list :
    list_id.append(match['id'])

print(list_id)