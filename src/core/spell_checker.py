import re 
from spellchecker import SpellChecker 

class SpellCheckerWrapper:

    def __init__(self, language: str="en"):
        self.spell = SpellChecker(language=language)

    def find_misspelled(self, text: str) -> list[str]:
        words = re.findall(r'\b\w+\b', text.lower())
        return list(self.spell.unknown(words))
    

        