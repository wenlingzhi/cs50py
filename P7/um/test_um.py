from um import count
import pytest

def test1():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("me,um,hello") == 1

def test2():
    assert count("yummy") == 0
    assert count("yum?hello") == 0

def test3():
    assert count("Um, thanks for the album") == 1
    assert count("Um, thanks, um...") == 2

def test4():
    assert count("") == 0
    assert count("totally wrong") == 0

if __name__ == "__main__":
    pytest.main()
