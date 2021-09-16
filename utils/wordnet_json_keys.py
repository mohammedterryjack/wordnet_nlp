from enum import Enum

class WordnetJSON(Enum):
    TEXT = "text"
    TOKENS = "tokens"
    POS = "part_of_speech"
    NER = "named_entities"
    DEFINITIONS = "definitions"
    EXAMPLES = "examples"