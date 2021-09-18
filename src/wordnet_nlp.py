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
        self.separator = "; "

    def get_json(self, text:str) -> str:
        tokens,pos,ner,definitions,examples = text,[],[],[],[]
        if any(text):
            tokens,pos,ner,definitions,examples,synonyms,antonyms,related_topics =  zip(*self.parse(text))
        json_package = {
            WordnetJSON.TEXT.value:text,
            WordnetJSON.TOKENS.value:tokens,
            WordnetJSON.POS.value:pos,
            WordnetJSON.NER.value:ner,
            WordnetJSON.DEFINITIONS.value:definitions,
            WordnetJSON.EXAMPLES.value:examples,
            WordnetJSON.SYNONYMS.value:synonyms,
            WordnetJSON.ANTONYMS.value:antonyms,
            WordnetJSON.RELATED.value:related_topics,
        }
        return dumps(json_package,indent=3)


    def parse(self, text:str) -> List[Tuple[str,str,Optional[str],str,str,str,str,str]]:
        tokens = self.tokeniser.tokenise(text)
        for token in tokens:
            pos_label,ner_label,definition,example,synonym,antonym,relative = self.tokeniser.STOPWORD,None,"","","","",""

            if token in self.tokeniser.stopwords:
               yield (token,pos_label,ner_label,definition,example,synonym,antonym,relative)
               continue 

            token_meaning = self.get_meaning(token,tokens)
            if token_meaning is None:
                pos_label = WordnetPOS.NOUN.value
                ner_label = self.tokeniser.OOV
            else:
                pos_label = self.tokeniser.part_of_speech_labels.get(token_meaning.pos())
                token_features = self.get_lineage(token_meaning)
                ner_label = self.get_label(token_features)
                synonymous_words = list(self.remove_duplicates(values=self.get_synonyms(token_meaning),duplicates=[token]))
                related_words = self.remove_duplicates(values=self.get_related_topics(token_meaning),duplicates=[token]+synonymous_words)
                synonym = self.separator.join(synonymous_words)
                antonym = self.separator.join(self.get_antonyms(token_meaning))
                relative = self.separator.join(related_words)
                definition = token_meaning.definition()
                example = self.separator.join(token_meaning.examples())
            
            yield (token,pos_label,ner_label,definition,example,synonym,antonym,relative )
        

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
    
    @staticmethod
    def get_synonyms(meaning:Synset) -> List[str]:
        return meaning.lemma_names()
        
    @staticmethod
    def get_antonyms(meaning:Synset) -> List[str]:
        for lemma in meaning.lemmas():
            for antonym in lemma.antonyms():
                yield antonym.name()
    
    @staticmethod
    def get_related_topics(meaning:Synset) -> List[str]:
        for relative in meaning.hyponyms() \
            + meaning.part_meronyms() \
            + meaning.substance_meronyms() \
            + meaning.member_meronyms() \
            + meaning.part_holonyms() \
            + meaning.substance_holonyms() \
            + meaning.member_holonyms() \
            + meaning.topic_domains() \
            + meaning.region_domains() \
            + meaning.usage_domains() \
            + meaning.entailments() \
            + meaning.causes() \
            + meaning.also_sees() \
            + meaning.verb_groups() \
            + meaning.similar_tos():
            for word in WordnetNLP.get_synonyms(relative):
                yield word
    
    @staticmethod
    def remove_duplicates(values:List[str],duplicates:List[str]) -> List[str]:
        for value in set(values):
            if value not in duplicates:
                yield value