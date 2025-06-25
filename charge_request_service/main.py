from flask import Flask, request
import requests

app = Flask(__name__)
LOAD_BALANCER_URL = "http://load_balancer:5001/route"

@app.route('/request_charge', methods=['POST'])
def request_charge():
    response = requests.post(LOAD_BALANCER_URL)
    return response.json(), response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
