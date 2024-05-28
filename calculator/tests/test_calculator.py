# tests/test_calculator.py
import pytest
from src.calculator import Calculator

def test_addition():
    calc = Calculator()
    assert calc.add(1, 2) == 3

def test_subtraction():
    calc = Calculator()
    assert calc.subtract(5, 3) == 2

# tests/test_calculator.py
def test_multiplication():
    calc = Calculator()
    assert calc.multiply(2, 3) == 6

def test_division():
    calc = Calculator()
    assert calc.divide(6, 2) == 3

def test_square_root():
    calc = Calculator()
    assert abs(calc.sqrt(9) - 3) < 0.001
    assert abs(calc.sqrt(2) - 1.414) < 0.001