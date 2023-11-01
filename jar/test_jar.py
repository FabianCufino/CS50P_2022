from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert str(jar) == ""


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(10)
    assert jar.deposit(1) == 1

    with pytest.raises(ValueError):
        jar.deposit(15)


def test_withdraw():
    jar = Jar(10)
    jar.deposit(4)
    assert jar.withdraw(1) == 3

    with pytest.raises(ValueError):
        jar.withdraw(20)
