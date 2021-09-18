from requests import post

from utils.wordnet_json_keys import WordnetJSON

endpoint = 'https://glacial-scrubland-43274.herokuapp.com/parse'
username = "your_username"
password = "your_password"
example = {WordnetJSON.TEXT.value:"this is a test"}

response = post(endpoint, json=example, auth=(username,password))
print(response)
if response.ok:
    print(response.json())
