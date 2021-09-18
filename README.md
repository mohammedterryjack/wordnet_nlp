# Wordnet NLP
```python
curl -X POST -H 'Accept: */*' -H 'Accept-Encoding: gzip, deflate' -H 'Authorization: Basic <YOUR_CREDENTIALS>' -H 'Connection: keep-alive' -H 'Content-Length: 38' -H 'Content-Type: application/json' -H 'User-Agent: python-requests/2.23.0' -d '{"text": <YOUR_TEXT>}' https://glacial-scrubland-43274.herokuapp.com/parse
```


```python
from requests import post

url = "https://glacial-scrubland-43274.herokuapp.com/parse"
example = {"text":"the big fish said good bye"}
credentials = (<USERNAME>, <PASSWORD>)

response = post(url, auth=credentials, json=example) 
```

 ```python
 response.json()
 >> 
{
   "text": "the big fish said good bye",
   "tokens": [
      "the",
      "big_fish",
      "said",
      "goodbye"
   ],
   "part_of_speech": [
      "Stopword",
      "Noun",
      "Adjective",
      "Noun"
   ],
   "named_entities": [
      null,
      "Object.Whole.Entity.Living_Thing.Physical_Entity.Organism.Causal_Agent.Person.Adult.Important_Person.Big_Shot",
      "Aforesaid",
      "Entity.Abstraction.Communication.Message.Acknowledgment.Farewell.Adieu"
   ],
   "definitions": [
      "",
      "an important influential person",
      "being the one previously mentioned or spoken of",
      "a farewell remark"
   ],
   "examples": [
      "",
      "he thinks he's a big shot; she's a big deal in local politics; the Qaeda commander is a very big fish",
      "works of all the aforementioned authors; said party has denied the charges",
      "they said their good-byes"
   ],
   "synonyms": [
      "",
      "big_deal; big_wheel; head_honcho; big_shot; big_cheese; big_enchilada; big_gun",
      "aforesaid; aforementioned",
      "goodby; good-by; adieu; au_revoir; sayonara; so_long; arrivederci; good_day; adios; cheerio; auf_wiedersehen; bye-bye; bye; good-bye"
   ],
   "antonyms": [
      "",
      "",
      "",
      ""
   ],
   "related_to": [
      "",
      "colloquialism; influential_person; supremo; important_person; knocker; personage",
      "same",
      "word_of_farewell; farewell"
   ]
}
```
