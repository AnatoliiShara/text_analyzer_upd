from src.core.pipeline import TextAnalyzer

def test_text_analyzer_basic_analysis():
    # Тестовий текст
    text = """
    Python is a popular programming language. 
    It is used for web development, data analysis, and machine learning.
    Some people prefer JavaScript for frontend development.
    Python has many powerful libraries like NumPy and Pandas.
    """
    
    analyzer = TextAnalyzer(text)
    analysis = analyzer.get_analysis(top_n=3)
    
    # Базові перевірки
    assert isinstance(analysis, dict)
    assert analysis["word_count"] > 0
    assert analysis["char_count"] > 0
    assert analysis["sentence_count"] == 4
    
    # Перевірка топ-слів
    assert len(analysis["top_words"]) == 3
    assert any(word[0].lower() in ["python", "development", "and"] for word in analysis["top_words"])
    
    # Перевірка підсумку
    assert len(analysis["summary"]) > 0
    assert any("Python" in sentence for sentence in analysis["summary"])
    
    # Перевірка помилкових слів (припускаємо, що в цьому тексті їх немає)
    assert isinstance(analysis["misspelled"], list)

def test_text_analyzer_with_misspelled_words():
    # Текст з помилками
    text = "Thiss text containss some misspelled wordss."
    analyzer = TextAnalyzer(text)
    analysis = analyzer.get_analysis()
    
    assert len(analysis["misspelled"]) >= 3  # Очікуємо знайти помилки
    assert all(word in ["thiss", "containss", "wordss"] for word in analysis["misspelled"])