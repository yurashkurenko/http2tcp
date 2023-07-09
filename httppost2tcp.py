from flask import Flask
from flask import request
import random

app = Flask(__name__)

@app.route("/", methods=['POST'])
def json_example():
    request_data = request.get_json()
    payload1=request_data['payload']
    print(payload1)
    return ''
	
if __name__ == '__main__':
    app.run()