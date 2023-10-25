from plates import is_valid

def main():
    test_plates_1()
    test_plates_2()
    test_plates_3()
    test_plates_4()

#“All vanity plates must start with at least two letters.”
def test_plates_1():
    assert is_valid("C1HI;") == False
    assert is_valid(" CJHL") == False
    assert is_valid("00CJHL") == False
    assert is_valid("AA") == True
    assert is_valid("A1") == False

#“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
def test_plates_2():
    assert is_valid("C;") == False
    assert is_valid(".C;") == False
    assert is_valid("1CGH") == False
    assert is_valid(" CGH") == False
    assert is_valid(".CGH") == False
    assert is_valid("CJHLMKAS") == False
    assert is_valid("huiklo") == True

#“Numbers cannot be used in the middle of a plate; they must come at the end.
# For example, AAA222 would be an acceptable … vanity plate;
# AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
def test_plates_3():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False
    assert is_valid("AAA02A") == False
    assert is_valid("AAA000") == False
    assert is_valid("AAA300") == True
#“No periods, spaces, or punctuation marks are allowed.”
def test_plates_4():
    assert is_valid("AAA.22") == False
    assert is_valid(" AA22A") == False
    assert is_valid("AAABCD") == True


if __name__ == "__main__":
    main()

