from requests import post

from utils.wordnet_json_keys import WordnetJSON

endpoint = 'http://localhost:5000/'
username = "your_username"
password = "your_password"
example = {WordnetJSON.TEXT.value:"george is a doctor"}

response = post(endpoint, json=example, auth=(username,password))
print(response)
if response.ok:
    print(response.json())