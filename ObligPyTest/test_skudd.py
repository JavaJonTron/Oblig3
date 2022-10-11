from src.leap import main


def test_leapyear_divisible_by_4_but_not_by_100():
    assert main.isLeapYear(2012) is True
    assert main.isLeapYear(1964) is True

def test_leapyear_divisible_by_400():
    assert main.isLeapYear(1600) is True
    assert main.isLeapYear(2800) is True

def test_leapyear_not_divisible_by_4():
    assert main.isLeapYear(2003) is False
    assert main.isLeapYear(2005) is False


def test_leapyear_divisible_by_100_but_not_by_400():
    assert main.isLeapYear(1900) is False
    assert main.isLeapYear(2100) is False