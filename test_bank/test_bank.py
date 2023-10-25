from bank import value

def main():
    test_bank_hi()
    test_bank_hello()
    test_bank_no()
    test_bank_how()

def test_bank_hi():
    assert value("HI 4523;") == 20
    assert value("mr hi") == 100

def test_bank_hello():
    assert value("Hello mr addams") == 0

def test_bank_no():
    assert value("ser") == 100
    assert value("hola") == 20

def test_bank_how():
    assert value("how you doing sr alex") == 20
    assert value("how you doing 11") == 20


if __name__ == "__main__":
    main()

