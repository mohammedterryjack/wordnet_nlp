# Wordnet NLP

```python
from requests import post

url = "https://glacial-scrubland-43274.herokuapp.com/parse"
example = {"text":"the lady thought she was such a big shot"}
credentials = (<USERNAME>, <PASSWORD>)

response = post(url, auth=credentials, json=example) 
```

 ```python
 response.json()
 >> 
 {
  'text': 'the lady thought she was such a big shot', 
  'tokens': [
   'the', 
   'lady', 
   'thought', 
   'she', 
   'was', 
   'such', 
   'a', 
   'big_shot'
  ], 
  'part_of_speech': [
   'Stopword', 
   'Noun', 
   'Noun', 
   'Stopword', 
   'Stopword', 
   'Stopword', 
   'Stopword', 
   'Noun'
  ], 
  'named_entities': [
     None, 
     'Object.Whole.Entity.Living_Thing.Physical_Entity.Organism.Causal_Agent.Person.Leader.Aristocrat.Female_Aristocrat.Lady', 
     'Entity.Abstraction.Psychological_Feature.Cognition.Content.Belief.Thought', 
     None, 
     None, 
     None, 
     None, 
     'Object.Whole.Entity.Living_Thing.Physical_Entity.Organism.Causal_Agent.Person.Adult.Important_Person.Big_Shot'
  ], 
  'definitions': [
    None, 
    'a woman of the peerage in Britain', 
    'the organized beliefs of a period or group or individual', 
    None, 
    None, 
    None, 
    None, 
    'an important influential person'
  ], 
  'examples': [
    None, 
    '', 
    '19th century thought\nDarwinian thought', 
    None, 
    None, 
    None, 
    None, 
    "he thinks he's a big shot\nshe's a big deal in local politics\nthe Qaeda commander is a very big fish"
  ]
}
```
