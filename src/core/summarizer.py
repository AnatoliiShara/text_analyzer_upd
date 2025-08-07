import re
from collections import Counter
from typing import List

class SimpleSummarizer:
    def __init__(self, text: str):
        self.text = text

    def _split_sentences(self) -> List[str]:
        sentences = re.split(r'(?<=[.!?])\s+', self.text)
        return [s.strip() for s in sentences if s.strip()]
    
    def _get_keywords(self, top_n: int = 5) -> set[str]:
        # Розширений список стоп-слів
        stopwords = {'is', 'it', 'for', 'and', 'the', 'a', 'has', 'many', 'some', 'are', 'used'}
        
        words = [word.lower() for word in re.findall(r'\b\w+\b', self.text) 
                if word.lower() not in stopwords and len(word) > 3]
        
        # Додаємо вагу для унікальних слів (які зустрічаються в 1-2 реченнях)
        word_counts = Counter(words)
        unique_words = [word for word, count in word_counts.items() if 1 <= count <= 2]
        common = word_counts.most_common(top_n + len(unique_words))
        
        return set(word for word, _ in common if word in unique_words or word_counts[word] > 1)
    
    def summarize(self, max_sentences: int = 2) -> List[str]:
        sentences = self._split_sentences()
        keywords = self._get_keywords(top_n=3)
        
        scored = []
        for sent in sentences:
            words = set(re.findall(r'\b\w+\b', sent.lower()))
            # Нова система оцінки: більше балів за унікальні ключові слова
            score = sum(3 if word in keywords else 0 for word in words)
            scored.append((score, len(sent), sent))  # Додаємо довжину для додаткової сортування
        
        # Сортуємо за рахунком (спадання), потім за довжиною (зростання)
        scored.sort(reverse=True, key=lambda x: (x[0], -x[1]))
        
        return [s for _, _, s in scored[:max_sentences]]