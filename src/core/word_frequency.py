import re
from collections import Counter

class WordFrequency:

    def __init__(self, text: str):
        self.text = text

    def get_frequencies(self) -> dict:
        words = re.findall(r'\b\w+\b', self.text.lower())
        return dict(Counter(words))
    
    def top_n(self, n: int) -> list[tuple[str, int]]:
        words = re.findall(r'\b\w+\b', self.text.lower())
        return Counter(words).most_common(n)
    
    
        