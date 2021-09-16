from flask import Flask,request
from werkzeug.exceptions import Unauthorized

from src.wordnet_nlp import WordnetNLP
from utils.wordnet_json_keys import WordnetJSON
   
app = Flask(__name__)
app.nlp = WordnetNLP()
with open("users.txt") as recognised_users_file:
    app.recognised_users = recognised_users_file.readlines()

@app.route(f"/",methods=["POST"])
def parse():
    if request.authorization.username not in app.recognised_users:
        raise Unauthorized()
    input_json = request.get_json()
    text = input_json.get(WordnetJSON.TEXT.value, "")
    return app.nlp.get_json(text)

app.run(debug=False)