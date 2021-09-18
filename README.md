# Wordnet NLP

```python
from requests import post

url = "https://glacial-scrubland-43274.herokuapp.com/parse"
example = {"text":"ciao"}
credentials = (<USERNAME>, <PASSWORD>)

response = post(url, auth=credentials, json=example) 
```

 ```python
 response.json()
 >> 
ciao
{
   "text": "ciao",
   "tokens": [
      "ciao"
   ],
   "part_of_speech": [
      "Noun"
   ],
   "named_entities": [
      "Entity.Abstraction.Communication.Message.Acknowledgment.Aloha"
   ],
   "definitions": [
      "an acknowledgment that can be used to say hello or goodbye (aloha is Hawaiian and ciao is Italian)"
   ],
   "examples": [
      ""
   ],
   "synonyms": [
      "aloha"
   ],
   "antonyms": [
      ""
   ],
   "related": [
      "Italy; Italian_Republic; Italia"
   ]
}
```