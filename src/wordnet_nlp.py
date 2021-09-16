from typing import List, Tuple, Optional
from json import dumps 

from nltk.corpus import wordnet
from nltk.corpus.reader.wordnet import Synset
from nltk.wsd import lesk

from src.wordnet_tokeniser import WordnetTokeniser
from utils.wordnet_pos import WordnetPOS
from utils.wordnet_json_keys import WordnetJSON

class WordnetNLP:
    """
    Wordnet Natural Language Processing (NLP)
    """
    def __init__(self) -> None:
        self.tokeniser = WordnetTokeniser()

    def get_json(self, text:str) -> str:
        tokens,pos,ner,definitions,examples = text,[],[],[],[]
        if any(text):
            tokens,pos,ner,definitions,examples =  zip(*self.parse(text))
        json_package = {
            WordnetJSON.TEXT.value:text,
            WordnetJSON.TOKENS.value:tokens,
            WordnetJSON.POS.value:pos,
            WordnetJSON.NER.value:ner,
            WordnetJSON.DEFINITIONS.value:definitions,
            WordnetJSON.EXAMPLES.value:examples,
        }
        return dumps(json_package,indent=3)


    def parse(self, text:str) -> List[Tuple[str,str,Optional[str],Optional[str],Optional[str]]]:
        tokens = self.tokeniser.tokenise(text)
        for token in tokens:
            pos_label,ner_label,definition,example = self.tokeniser.STOPWORD,None,None,None

            if token in self.tokeniser.stopwords:
               yield (token,pos_label,ner_label,definition,example)
               continue 

            token_meaning = self.get_meaning(token,tokens)
            if token_meaning is None:
                pos_label = WordnetPOS.NOUN.value
                ner_label = self.tokeniser.OOV
            else:
                pos_label = self.tokeniser.part_of_speech_labels.get(token_meaning.pos())
                definition = token_meaning.definition()
                example = '\n'.join(token_meaning.examples())

            if ner_label == self.tokeniser.OOV: #pos_label not in (WordnetPOS.NOUN.value, WordnetPOS.VERB.value) or
                yield (token,pos_label,ner_label,definition,example)
                continue
                
            token_features = self.get_lineage(token_meaning)
            ner_label = self.get_label(token_features)
                                        
            yield (token,pos_label,ner_label,definition,example)
        

    @staticmethod
    def get_meaning(token:str,context_tokens:List[str]) -> Synset:
        return lesk(context_tokens, token)
        
    @staticmethod
    def get_label(meanings:List[Synset]) -> Optional[str]:
        return WordnetNLP.format_synsets_as_title(meanings[::-1])

    @staticmethod
    def get_lineage(meaning:Synset) -> List[Synset]:
        return [meaning] + list(meaning.closure(WordnetNLP.get_parent))

    @staticmethod
    def get_parent(meaning:Synset) -> Synset:
        return meaning.hypernyms()
    
    @staticmethod
    def format_synsets_as_title(meanings:List[Synset]) -> str:
        return '.'.join(map(WordnetNLP.format_synset_as_title,meanings))

    @staticmethod
    def format_synset_as_title(meaning:Synset) -> str:
        return meaning.name().split(".")[0].title()
    

#TODO: get wordnet label for adjectives and adverbs