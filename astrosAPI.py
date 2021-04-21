import requests
import json
from datetime import datetime

def pPrint(obj):
	text = json.dumps(obj, sort_keys=True, indent=4)
	print(text)


response = requests.get("http://api.open-notify.org/astros.json")

print(response.status_code)

print(response.json())

pPrint(response.json())

parameters = {
	"lat": 30,
	"lon": 20
}

response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

pPrint(response.json())

pass_times = response.json()['response']

pPrint(pass_times)

risetimes = []

for d in pass_times:
	time = d['risetime']
	risetimes.append(time)

print(risetimes)

times = []

for rt in risetimes:
	time = datetime.fromtimestamp(rt)
	times.append(time)
	print(time)