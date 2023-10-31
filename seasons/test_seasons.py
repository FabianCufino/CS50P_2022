from seasons import check_date
from datetime import datetime
import pytest

def main():
    test_season_1()


#“All vanity plates must start with at least two letters.”
def test_season_1():
    assert check_date("1993-09-08") == datetime(1993, 9, 8, 0, 0)
    assert check_date("1993X09-08") == None

if __name__ == "__main__":
    main()

