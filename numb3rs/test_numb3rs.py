from numb3rs import validate
import pytest

def main():
    test_validate_1()
    test_validate_2()


def test_validate_1():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False

def test_validate_2():
    assert validate("cat") == False
    assert validate("...") == False
    assert validate("10.10.10.10.10") == False
    assert validate("10.10.10") == False
    assert validate("512.10.10.1") == False
    assert validate("-5.10.10.1") == False
    assert validate("5.512.512.512") == False
    assert validate("5.5.512.512") == False
    assert validate("5.5.5.512") == False


if __name__ == "__main__":
    main()

