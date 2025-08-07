from src.core.spell_checker import SpellCheckerWrapper


def test_find_misspelled():
    checker = SpellCheckerWrapper()
    text = "This is a beautifull day with a misstake in it"

    misspelled = checker.find_misspelled(text)

    assert 'beautifull' in misspelled  # Перевіряємо саме те слово, яке було у тексті
    assert 'misstake' in misspelled
    assert 'this' not in misspelled  # "this" у нижньому регістрі, оскільки метод використовує .lower()