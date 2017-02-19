import requests
import json

data = 	{
	"title": "places",
	"author": 2,
	"list_type": "fucking awesome2",
}

r = requests.post('http://localhost:8000/lists/', data=data)
print r.status_code
print r.text
