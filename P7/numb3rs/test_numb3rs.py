from P7.numb3rs.numb3rs import validate

def test_out_of_range():
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("127.444.444.444") == False

def test_omit():
    assert validate("2.128.2") == False
    assert validate("1.1") == False

def test_correct():
    assert validate("255.255.255.255") == True
    assert validate("1.123.2.3") == True

def test_invalid():
    assert validate("1.127.3.cat") == False
    assert validate("a.b.c.d") == False
    assert validate("..,,") == False
