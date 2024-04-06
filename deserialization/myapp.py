import requests
import json 

URL="http://127.0.0.1:8000/stucreate/"
data = {
	'name': "Akash",
	'roll': 102,
	'city': "Shiliguri",
	'marks': 102
}

json_data= json.dumps(data)

r = requests.post(url=URL, data=json_data)

data = r.json()
print(data)