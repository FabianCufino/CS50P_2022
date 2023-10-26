from fuel import convert, gauge
import pytest

def main():
    test_convert_1()
    test_convert_2()
    test_zero_division()
    test_value_error()

#“All vanity plates must start with at least two letters.”
def test_convert_1():
    assert convert("50/100") == 50 and gauge(50) == "50%"

#“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
def test_convert_2():
    assert convert("1/100") == 1 and gauge(1) == "E"
    assert convert("99/100") == 99 and gauge(99) == "F"

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("100/0")
def test_value_error():
    with pytest.raises(ValueError):
        convert("100/20")

if __name__ == "__main__":
    main()