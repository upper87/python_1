from Money_result import Money


def test_str():
    money1 = Money(20, 39)
    assert str(money1) == "20руб 39коп"
    money2 = Money(20, 239)
    assert str(money2) == "22руб 39коп"
    money3 = Money(12, 200)
    assert str(money3) == "14руб 0коп"


def test_add():
    money1 = Money(20, 39)
    money2 = Money(12, 49)
    money3 = money1 + money2
    assert str(money1) == "20руб 39коп"
    assert str(money2) == "12руб 49коп"
    assert str(money3) == "32руб 88коп"

    money1 = Money(20, 50)
    money2 = Money(12, 75)
    money3 = money1 + money2
    assert str(money3) == "33руб 25коп"


def test_sub():
    money1 = Money(20, 39)
    money2 = Money(12, 49)
    money3 = money1 - money2
    assert str(money1) == "20руб 39коп"
    assert str(money2) == "12руб 49коп"
    assert str(money3) == "7руб 90коп"

    money1 = Money(10, 39)
    money2 = Money(12, 49)
    money3 = money1 - money2
    assert str(money1) == "10руб 39коп"
    assert str(money2) == "12руб 49коп"
    assert str(money3) == "-2руб 10коп"

    money1 = Money(10, 39)
    money2 = Money(10, 39)
    money3 = money1 - money2
    assert str(money3) == "0руб 0коп"