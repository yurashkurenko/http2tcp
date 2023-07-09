from flask import Flask
from flask import request
import random

app = Flask(__name__)

def payload():
    return "<p>Hello, World!"+str(random.randint(5, 125))+"</p>"

@app.route("/", methods=['POST', 'GET'])
def hello_world():
    print(request)
    return payload()

if __name__ == '__main__':
    app.run()