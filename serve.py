from os import environ

from flask import Flask,request
from werkzeug.exceptions import Unauthorized

from src.wordnet_nlp import WordnetNLP
from utils.wordnet_json_keys import WordnetJSON
   
app = Flask(__name__)
app.nlp = WordnetNLP()
with open("users.txt") as recognised_users_file:
    app.recognised_users = recognised_users_file.readlines()

@app.route("/")
def home():
    return "Wordnet NLP"

@app.route(f"/parse",methods=["POST"])
def parse():
    
    authentication = request.authorization
    if authentication is None or authentication.username not in app.recognised_users:
        raise Unauthorized()

    input_json = request.get_json()
    text = "" if input_json is None else input_json.get(WordnetJSON.TEXT.value, "")
    return app.nlp.get_json(text)

if __name__ == '__main__':
    app.run(threaded=True, port=environ.get('PORT'), debug=True)