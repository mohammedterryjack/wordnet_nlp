# Wordnet NLP

from requests import post

post(
  https://glacial-scrubland-43274.herokuapp.com/, 
  auth=("your_username","your_password"),
  json={"text":"this is a test"} 
)
