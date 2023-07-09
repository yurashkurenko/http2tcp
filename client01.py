import requests
import json
#jsondata='{"payload":"Какая-то входящая информация"}'
#json_object = json.loads(jsondata)
def getinfo():
    r=requests.get("http://127.0.0.1:5000/get")
    return r.text
def sendinfo(rout):
    jsondata='{"payload":"'+str(rout)+'"}'
    json_object = json.loads(jsondata)
    r=requests.post("http://127.0.0.1:5000/post",json=json_object)
    print(r.text)
    return
strout="Что-то уходит от клиента к серверу..."
getinfo()
sendinfo(strout)
getinfo()