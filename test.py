# test.py

import pytest
from Suma import adder
from sustraction import sustraction
from Multiplier import multiplier
from dividedanger import dividedanger

def test_adder():
    assert adder(1, 2) == 3
    assert adder(-1, 1) == 0
    assert adder(-1, -1) == -2

def test_sustraction():
    assert sustraction(10, 5) == 5
    assert sustraction(0, 0) == 0
    assert sustraction(-5, -5) == 0

def test_multiplier():
    assert multiplier(3, 4) == 12
    assert multiplier(-1, 1) == -1
    assert multiplier(0, 10) == 0

def test_dividedanger():
    assert dividedanger(10, 2) == 5
    assert dividedanger(-6, 3) == -2
    with pytest.raises(ValueError):
        dividedanger(1, 0)
