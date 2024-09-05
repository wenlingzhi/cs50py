from bank import value

def test_hello():
    assert value('hello') == 0
    assert value('hello, world') == 0

def test_h():
    assert value('hey') == 20
    assert value('hahahahah') == 20
    assert value('hey,hey,hey') == 20

def test_noH():
    assert value('why?') == 100
    assert value('I dont know') == 100

def test_capital():
    assert value('HELLO') == 0
    assert value('Hey') == 20
