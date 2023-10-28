from um import count
def main():
    test_um_1()
    test_um_2()
    test_um_3()


def test_um_1():
    assert count("um um") == 2
    assert count("um") == 1
    assert count("um?") == 1


def test_um_2():
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2

def test_um_2():
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2
def test_um_3():
    assert count("Um, thanks for the album.") == 1
    assert count("yummi") == 0

if __name__ == "__main__":
    main()
