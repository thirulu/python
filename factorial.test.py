# test_factorial.py

import pytest
from factorial import factorial

def test_factorial_zero():
    assert factorial(0) == 1

def test_factorial_one():
    assert factorial(1) == 1

def test_factorial_positive():
    assert factorial(5) == 120
    assert factorial(7) == 5040
    assert factorial(10) == 3628800

def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-5)

def test_factorial_float():
    with pytest.raises(ValueError):
        factorial(5.5)
