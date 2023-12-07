from flask import Flask, jsonify,request
import requests
from flask_cors import CORS
from simple_salesforce import Salesforce

app = Flask(__name__)
CORS(app)

UserName = 'ramu@nevoori.com'
Password = 'R@mureddy555'
grant_type = 'password'
CONSUMER_KEY = '3MVG9fe4g9fhX0E5tUUwFRxQxiFup.V3wRXdZRojZYSurdjcV6VglYKzYiTc9GOHMykNeDnVtXE0pKyBUIGin'
CONSUMER_SECRET = '25A56C8A385020435BA7B17FEB683E420FE02856D601B35BCDD11B2BB9D667A4'
REDIRECT_URI = 'https://testcompany-2e6-dev-ed.my.salesforce.com'
SALESFORCE_INSTANCE_URL = 'https://testcompany-2e6-dev-ed.my.salesforce.com'

params = {
    "grant_type": "password",
    "client_id": CONSUMER_KEY,
    "client_secret": CONSUMER_SECRET,
    "username": UserName,
    "password": Password
}
r = requests.post("https://login.salesforce.com/services/oauth2/token", params=params)
SALESFORCE_ACCESS_TOKEN = r.json().get("access_token")

@app.route('/api/data', methods=['POST','GET'])
def get_data():
    sf = Salesforce(instance_url=SALESFORCE_INSTANCE_URL, session_id=SALESFORCE_ACCESS_TOKEN)
    contacts = sf.query("SELECT Id,Name,Email,Phone from Contact WHERE PHONE != null AND Email != null LIMIT 10")
    return jsonify(contacts)

if __name__ == '__main__':
    app.run(debug=True)