from pytest import raises

from calc import add
from calc import divide


def test_add():
    assert add(2, 3) == 5


def test_add_wrong_type():
    with raises(TypeError):
        add(2, "4")


def test_zero_division():
    with raises(ZeroDivisionError):
        divide(3/0)
    