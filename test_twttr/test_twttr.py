from twttr import shorten


def main():
    test_twttr_upper()



def test_twttr_upper():
    assert shorten("HOLA") == "HL"
    assert shorten("MI MUNDO") == "M MND"


def test_twttr_lower():
    assert shorten("hola") == "hl"
    assert shorten("mi mundo") == "m mnd"

def test_twttr_number():
    assert shorten("11 11") == "11 11"
    assert shorten("STAR PLUS ;; Q") == "STR PLS ;; Q"


if __name__ == "__main__":
    main()
