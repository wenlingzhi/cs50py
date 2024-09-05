import pytest
from working import convert

def test_type1():
    assert convert("8:22 AM to 9:25 PM") == "08:22 to 21:25"
    assert convert("8 AM to 9 PM") == "08:00 to 21:00"
    assert convert("8 PM to 9 PM") == "20:00 to 21:00"
    assert convert("8:22 PM to 9:25 AM") == "20:22 to 09:25"

def test_type2():
    assert convert("8:22 AM to 9 PM") == "08:22 to 21:00"
    assert convert("8 AM to 9:23 PM") == "08:00 to 21:23"

def test_error():
    with pytest.raises(ValueError):
        convert("8:62 PM to 9:25 AM")

    with pytest.raises(ValueError):
        convert("8: PM to 9:25 AM")

    with pytest.raises(ValueError):
        convert("8 PM to 9:100 AM")

    with pytest.raises(ValueError):
        convert("8: PM - 9:25 AM")

if __name__ == "__main__":
    pytest.main()
