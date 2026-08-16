import sys
import os
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from calculator import add, subtract, multiply, divide


def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-1, -4) == -5

def test_add_mixed_signs():
    assert add(-3, 7) == 4

def test_subtract_basic():
    assert subtract(10, 4) == 6

def test_subtract_negative_result():
    assert subtract(3, 8) == -5

def test_multiply_basic():
    assert multiply(3, 4) == 12

def test_multiply_by_zero():
    assert multiply(99, 0) == 0

def test_multiply_negatives():
    assert multiply(-2, -5) == 10

def test_divide_basic():
    assert divide(10, 2) == 5.0

def test_divide_fractional_result():
    assert divide(7, 2) == 3.5

def test_divide_by_zero_raises():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(5, 0)

def test_divide_negative_dividend():
    assert divide(-10, 2) == -5.0

def test_add_floats():
    assert add(1.5, 2.5) == 4.0

def test_subtract_floats():
    assert subtract(5.5, 2.2) == pytest.approx(3.3)

def test_multiply_floats():
    assert multiply(2.5, 4.0) == 10.0
