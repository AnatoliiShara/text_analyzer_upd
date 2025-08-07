from src.core.text_stats import TextStats
from src.core.word_frequency import WordFrequency
from src.core.spell_checker import SpellCheckerWrapper  # Використовуємо наш обгортку
from src.core.summarizer import SimpleSummarizer


class TextAnalyzer:
    def __init__(self, text: str):
        self.text = text
        self.stats = TextStats(text)
        self.freq = WordFrequency(text)
        self.spell = SpellCheckerWrapper()  # Ініціалізуємо без тексту
        self.summarizer = SimpleSummarizer(text)

    def get_analysis(self, top_n: int = 5) -> dict:
        return {
            "word_count": self.stats.count_words(),
            "char_count": self.stats.count_characters(),
            "sentence_count": self.stats.count_sentences(),
            "top_words": self.freq.top_n(top_n),
            "misspelled": self.spell.find_misspelled(self.text),  # Виправлено typo (misspelles -> misspelled)
            "summary": self.summarizer.summarize()
        }