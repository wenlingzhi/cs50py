from twttr import shorten

def test_mix():
    assert shorten("twitter") == "twttr"

def test_capital():
    assert shorten("TWITTER") == "TWTTR"

def test_empty():
    assert shorten("") == ""

def test_vowel():
    assert shorten("aoeiu") == ""

def test_consonants():
    assert shorten("lgbtq") == "lgbtq"

def test_numbers():
    assert shorten("12345") == "12345"

def test_punctuation():
    assert shorten(":::") == ":::"
