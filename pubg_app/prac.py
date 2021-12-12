import requests
import json

url = "https://api.pubg.com/shards/kakao/players?filter[playerNames]=WOOGI_WOOGI"

header = { 
    "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI2YjdmNGI5MC0zOWYyLTAxM2EtNzE4Yy0wOWQzZTk3ZDU4YzYiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNjM4OTI2MTk5LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6ImRyYW5nZWwifQ.lErH1X1rimCNc1ilTkeZXUTJ_-XTg1QnkMSSOS06LiI", 
    "Accept": "application/vnd.api+json"
    }


#req = requests.get(url, headers=header)
#
#player_data = json.loads(req.text) 
#
#print(player_data)

match_url = "https://api.pubg.com/shards/kakao/matches/ee21cf35-9877-4de2-8c92-0992df9b3647"
# 21.12.10 3369c5db-3635-4fde-b957-daa5b515d686
# 21.12.08 296ae615-fdef-4e8e-b33d-476b6b33cf25

match_header = { 
    "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI2YjdmNGI5MC0zOWYyLTAxM2EtNzE4Yy0wOWQzZTk3ZDU4YzYiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNjM4OTI2MTk5LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6ImRyYW5nZWwifQ.lErH1X1rimCNc1ilTkeZXUTJ_-XTg1QnkMSSOS06LiI", 
    "Accept": "application/vnd.api+json"
    }

req = requests.get(match_url, headers=match_header)

match_data = json.loads(req.text) 

print(match_data)

#for data in match_data['included'] :
#    if data['type'] == 'participant' :
#        print(data['attributes']['stats']['playerId'])
#    else : continue