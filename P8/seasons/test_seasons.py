from P8.seasons.seasons import get_time
from datetime import date
import pytest

def test_valid():
    expected_date = date(2003,7,7)
    result = get_time("2003-07-07")
    assert result == expected_date

def test_invalid():
    with pytest.raises (ValueError):
        get_time("2003-07-88")
