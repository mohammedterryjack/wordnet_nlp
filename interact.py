from src.wordnet_nlp import WordnetNLP

nlp = WordnetNLP()
while True:
   sentence = input(">")
   results = nlp.get_json(sentence)
   print(results)