# tests/test_calculator.py
import pytest
from src.calculator import Calculadora

def test_suma():
    calc = Calculadora()
    assert calc.sumar(1, 2) == 3

def test_resta():
    calc = Calculadora()
    assert calc.restar(5, 3) == 2

# tests/test_calculator.py
def test_multiplicacion():
    calc = Calculadora()
    assert calc.multiplicar(2, 3) == 6