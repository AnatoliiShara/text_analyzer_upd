from src.core.text_stats import TextStats

def test_text_stats_counts():
    text = "Hello world! How you are doing? I'm fine, thanks"
    stats = TextStats(text)  # Тепер передаємо текст
    assert stats.count_words() == 9  # Увага: "I'm" = 1 слово, всього 9
    assert stats.count_characters() == len(text)
    assert stats.count_sentences() == 2  # "!" та "?" — 2 речення