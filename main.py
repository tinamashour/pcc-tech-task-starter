import http.client
import json
import pprint

conn = http.client.HTTPSConnection("raw.githubusercontent.com")
conn.request("GET", "/openfootball/football.json/master/2016-17/en.1.json")

res = conn.getresponse()
data = res.read().decode("utf-8")

json = json.loads(data)

pprint.pprint(data)

ranked_teams = {}

pprint.pprint(ranked_teams)
