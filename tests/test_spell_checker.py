from src.core.spell_checker import SpellCheckerWrapper


def test_find_misspelled():
    checker = SpellCheckerWrapper()
    text = "This is a beautifull day with a misstake in it"
    
    misspelled = checker.find_misspelled(text)
    
    # Перевіряємо хоча б одну з помилок
    assert any(word in misspelled for word in ["beautifull", "misstake"])