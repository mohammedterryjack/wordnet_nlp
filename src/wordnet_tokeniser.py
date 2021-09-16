from typing import Optional, List

from nltk.corpus import wordnet
from nltk.corpus.reader.wordnet import ADJ, ADJ_SAT, ADV, NOUN, VERB
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.util import ngrams

from utils.wordnet_pos import WordnetPOS


class WordnetTokeniser:
    def __init__(self) -> None:
        self.STOPWORD = "Stopword"
        self.IGNORE = "IgnoreToken"
        self.OOV = "OutOfVocab"
        self.stopwords = stopwords.words('english')
        self.part_of_speech_labels = {
            NOUN:WordnetPOS.NOUN.value,
            VERB:WordnetPOS.VERB.value,
            ADV:WordnetPOS.ADVERB.value,
            ADJ:WordnetPOS.ADJECTIVE.value,
            ADJ_SAT:WordnetPOS.ADJECTIVE.value
        }
        self.lemmatiser = WordNetLemmatizer()
        self.wordnet_vocabulary = {
            self.normalise_phrase(phrase):phrase for phrase in wordnet.all_lemma_names()
        }

    def normalise_phrase(self,phrase:str) -> str:
        """
        normalises the various ways to join tokens with ""
        and lowers all characters
        to simplify comparisons

        e.g. Al-Masri's_5th_xray -> almasris5thxray
        e.g. going_away -> goaway
        """
        tokens = phrase.lower().replace("'","").replace(".","").replace('-',' ').replace('_',' ').split()
        return tokens[0] if len(tokens)==1 else ''.join(map(self.stem,tokens))

    def stem(self, word:str) -> str:
        return self.lemmatiser.lemmatize(word)

    def convert_into_wordnet_token(self, phrase:str) -> Optional[str]:
        return self.wordnet_vocabulary.get(self.normalise_phrase(phrase))

    def tokenise(self, text:str) -> List[str]:
        """
        start with entire span
            get all ngrams of that span size
            convert any to wordnet tokens
            remove those words from text 
        then decrease span size and iterate
        stop when all words converted
        """
        tokens = text.split()
        max_span = len(tokens)
        wordnet_tokens = [""]*max_span
        for span_length in range(max_span+1,0,-1):
            chunks = list(ngrams(tokens, span_length))
            for token_start_index,chunk in enumerate(chunks):
                token_end_index = token_start_index + span_length
                if any(wordnet_tokens[index] for index in range(token_start_index,token_end_index)):
                    continue
                
                phrase = ' '.join(chunk)
                wordnet_phrase = self.convert_into_wordnet_token(phrase)
                if wordnet_phrase is not None:                    
                    wordnet_tokens[token_start_index] = wordnet_phrase
                    for index in range(token_start_index+1,token_end_index):
                        wordnet_tokens[index] = self.IGNORE
                elif span_length==1:
                    wordnet_tokens[token_start_index] = phrase

        return list(filter(lambda token:token!=self.IGNORE,wordnet_tokens))