from funcs import my_max


def test_func_max():
    assert my_max(2, 5) == 5
    assert my_max(5, 2) == 5
    assert my_max(-4, 4, 0, -5) == 4
    assert my_max(-4, -2, -8, -5) == -2
    assert my_max(4, 4) == 4
    assert my_max(-2.7, 2.5, 3.1, 0, -4.2) == 3.1
