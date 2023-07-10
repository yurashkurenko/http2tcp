from flask import Flask
from flask import request
import random
import json

app = Flask(__name__)

@app.route("/post", methods=['POST'])
def json_post():
    request_data = request.get_json()
    payload1=request_data['payload']
    print(payload1)
    return ''

@app.route("/get", methods=['GET'])
def json_get():
    jsondata='{"payload-out":"Какая-то исходящая информация от сервера к клиенту"}'
    json_object = json.loads(jsondata)  
    payloadout=json_object["payload-out"]
    print(payloadout)
    return json_object


	
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)
