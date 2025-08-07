import re

class TextStats:
    def __init__(self, text: str):
        self.text = text

    def count_words(self) -> int:
        words = re.findall(r"\b[\w']+\b", self.text)  # Додаємо ' до \w
        return len(words)

    def count_characters(self) -> int:
        return len(self.text)

    def count_sentences(self) -> int:
        sentences = re.findall(r'[.!?]', self.text)
        return len(sentences)
