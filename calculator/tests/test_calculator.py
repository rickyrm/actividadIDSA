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

