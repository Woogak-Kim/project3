import requests
import json

url = "https://api.pubg.com/shards/steam/players?filter[playerNames]=kimblue"

header = { 
    "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI2YjdmNGI5MC0zOWYyLTAxM2EtNzE4Yy0wOWQzZTk3ZDU4YzYiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNjM4OTI2MTk5LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6ImRyYW5nZWwifQ.lErH1X1rimCNc1ilTkeZXUTJ_-XTg1QnkMSSOS06LiI", 
    "Accept": "application/vnd.api+json"
    }

req = requests.get(url, headers=header)

player_data = json.loads(req.text) 



def player_id(data):
    account_id = player_data['data'][0]['id']
    name = player_data['data'][0]['attributes']['name']
    match_list = []
    count = 0
    for r in data['data'][0]['relationships']['matches']['data']:
        match_list.append(r['id'])
        count = count + 1
    return account_id, name, match_list, count

account_id, name, match_list, count = player_id(player_data)

print(count)