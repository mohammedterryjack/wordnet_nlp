# Wordnet NLP

```python
from requests import post

response = post(
  "https://glacial-scrubland-43274.herokuapp.com/parse", 
  auth=("your_username","your_password"),
  json={"text":"this is a test"} 
)
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
