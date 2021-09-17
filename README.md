# Wordnet NLP

```python
from requests import post

url = "https://glacial-scrubland-43274.herokuapp.com/parse"
example = {"text":"this is a test"}
credentials = (<username>,<password>)

response = post(url, auth=credentials, json=example) 
```

 ```python
 response.json()
 >> 
 {
   'text': 'this is a test', 
   'tokens': ['this', 'is', 'a', 'test'], 
   'part_of_speech': ['Stopword', 'Stopword', 'Stopword', 'Verb'], 
   'named_entities': [None, None, None, 'Change.Undergo.Take.Test'], 
   'definitions': [None, None, None, 'undergo a test'], 
   'examples': [None, None, None, "She doesn't test well"]
 }
 ```
