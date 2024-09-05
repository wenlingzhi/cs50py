from calculator import square
import pytest

def test_negative():
    assert square(-4) == 16

def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("cat")

'''
from calculator import square

def main():
    test_square()

def test_square():
    try:
        assert square(2) == 4
    except AdsertionError:
        print("2 square was not 4")

    try:
        assert square(4) == 16
    except AssertionError:
        print("4 square was not 16")

    try:
        assert square(0) == 0
    except AssertionError:
        print("0 square was not 0")

    try:
        assert square(-3) == 9
    except AssertionError:
        print("-3 square was not 9")

if __name__ == "__main__":
    main()
'''
