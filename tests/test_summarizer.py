from src.core.summarizer import SimpleSummarizer

def test_summarizer_with_key_sentences():
    text = """
    Python is a beautiful language.
    It is used for machine learning and web development.
    Some people prefer JavaScript for frontend work.
    Python has many libraries for data analysis.
    """
    
    summarizer = SimpleSummarizer(text)
    summary = summarizer.summarize(max_sentences=2)
    
    assert len(summary) == 2
    # Знаходимо індекси речень, що містять ключові слова
    python_sents = [i for i, s in enumerate(summary) if "Python" in s]
    assert len(python_sents) >= 1  # Принаймні одне речення про Python
    
    # Перевіряємо, що в підсумку є або "language", або "libraries"
    assert any("language" in s or "libraries" in s for s in summary)