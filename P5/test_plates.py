'''
“All vanity plates must start with at least two letters.”

“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”

“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”

“No periods, spaces, or punctuation marks are allowed.”

'''

from plates import is_valid

def test_correct():
    assert is_valid("AA1234") == True
    assert is_valid("AA") == True
    assert is_valid("AABBCC") == True

def test_allnum():
    assert is_valid("123456") == False

def test_lesstwo():
    assert is_valid("A") == False
    assert is_valid("1") == False

def test_morethan():
    assert is_valid("1234567") == False
    assert is_valid("AA12345") == False

def test_mix():
    assert is_valid("AA10AA") == False

def test_marks():
    assert is_valid("AA1 AA") == False
    assert is_valid("AA1:AA") == False
    assert is_valid("AA1.AA") == False

def test_zero():
    assert is_valid("000000") == False
    assert is_valid("AA0123") == False
