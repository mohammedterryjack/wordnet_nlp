from enum import Enum

class WordnetJSON(Enum):
    TEXT = "text"
    TOKENS = "tokens"
    POS = "part_of_speech"
    NER = "named_entities"
    DEFINITIONS = "definitions"
    EXAMPLES = "examples"
    SYNONYMS = "synonyms"
    ANTONYMS = "antonyms"
    RELATED = "related_to"