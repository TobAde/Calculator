from src.calculator import Calculator
import pytest

def test_add():
    """tests the Calculator add method"""
    calc = Calculator()
    assert calc.add(10.10) == 10.10

def test_subtract():
    """tests the Calculator subtract method"""
    calc = Calculator(10)
    assert calc.subtract(2) == 8

def test_divide():
    """tests the Calculator divide method"""
    calc = Calculator(8)
    assert calc.divide(2) == 4

def test_memory_value():
    """tests the Calculator memory value"""
    calc = Calculator(4)
    assert calc.memory_value == 4

def test_multiply():
    """tests the Calculator multiply method"""
    calc = Calculator()
    assert calc.multiply(0) == 0

def test_zero_division():
    """tests the Calculator error - zero division"""
    calc = Calculator()
    assert calc.subtract(20) == -20
    assert calc.add(-10) == -30
    assert calc.divide(0) == None
    assert calc.memory_value == -30

def test_modulus():
    """tests the mudulus method"""
    calc = Calculator(5)
    assert calc.modulus(2) == 1
    assert calc.memory_value == 1  

def test_zero__modulo_division():
    """tests the mudulus method"""
    calc = Calculator()
    assert calc.modulus(0) == None

def test_nth_root():
    """tests the Calculator nth_root method"""
    calc = Calculator(16)
    assert calc.nth_root(2) == 4  

def test_root_memory_less_than_zero():
    """tests the Calculator nth_root method error raise for memory value < 0"""
    with pytest.raises(Exception):
        calc = Calculator()
        calc.nth_root(2)

def test_root_value_less_than_zero():
    """tests the Calculator nth_root method error raise for inputed value < 0"""
    with pytest.raises(Exception):
        calc = Calculator(16)
        calc.square_root(-1)

def test_exponent():
    """tests the Calculator exponent method"""
    calc = Calculator(3)
    assert calc.exponent(3) == 27

def test_input_validation():
    """tests the Calculator input validation error """
    with pytest.raises(Exception):
        calc = Calculator('two')

def memory_reset_test():
    """tests the Calculator memory reset method"""
    calc = Calculator(10)
    calc.memory_reset()
    assert calc.memory_value == 0
