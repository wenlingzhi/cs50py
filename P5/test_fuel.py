from fuel import convert
from fuel import gauge
import pytest

def test_normal():
    assert convert("3/4") == 75
    assert convert("1/1") == 100
    assert convert("1/2") == 50

def test_gauge():
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"

def test_str():
    with pytest.raises(ValueError):
        convert("cat/dog")

def test_error():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("3/2")
