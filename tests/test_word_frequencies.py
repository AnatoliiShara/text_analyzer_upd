from src.core.word_frequency import WordFrequency

def test_get_frequencies():
    text = "apple banana apple orange banana banana"
    freq = WordFrequency(text)
    res = freq.get_frequencies()

    assert res['apple'] == 2
    assert res['banana'] == 3
    assert res['orange'] == 1

def test_top_n():
    text = "dog cat cat dog dog bird"
    freq = WordFrequency(text)

    top_2 = freq.top_n(2)
    assert top_2[0] == ("dog", 3)
    assert top_2[1] == ("cat", 2)