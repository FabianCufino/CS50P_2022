from working import convert
import pytest

def main():
    test_hours_am()
    test_hours_pm()
    test_hours_value()


def test_hours_am():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"


def test_hours_pm():
    assert convert("12:30 AM to 8:50 AM") == "00:30 to 08:50"

def test_hours_value():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("9AM to 5PM")
    with pytest.raises(ValueError):
        convert("9AM - 5PM")

if __name__ == "__main__":
    main()
