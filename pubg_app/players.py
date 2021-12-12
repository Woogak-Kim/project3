import requests
import json

match_url = "https://api.pubg.com/shards/steam/matches/9b605fe8-0808-4649-808d-a444fd9f9d4c"
match_header = { 
    "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI2YjdmNGI5MC0zOWYyLTAxM2EtNzE4Yy0wOWQzZTk3ZDU4YzYiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNjM4OTI2MTk5LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6ImRyYW5nZWwifQ.lErH1X1rimCNc1ilTkeZXUTJ_-XTg1QnkMSSOS06LiI", 
    "Accept": "application/vnd.api+json"
    }

req = requests.get(match_url, headers=match_header)

match_data = json.loads(req.text) 

def status(match):
    ai_count = 0
    player_count = 0
    player_list = []

    for data in match['included']:
        if data['type'] == 'participant':
            player = data['attributes']['stats']
            if player['playerId'].startswith('ai') == True :
                ai_count = ai_count + 1 
            else : 
                player_list.append(player['name'])
                player_count = player_count + 1
        else : continue

    print('Ai =',ai_count,'Human =',player_count)
    print('Real Players =',player_list)

print('Map =',match_data['data']['attributes']['mapName'])
print('UTC =',match_data['data']['attributes']['createdAt'])
status(match_data)
