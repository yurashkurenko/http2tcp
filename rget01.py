import requests
import json
#jsondata='{"payload":"Какая-то входящая информация"}'
#json_object = json.loads(jsondata)
r=requests.get("http://127.0.0.1:5000/get")

print(r.text)