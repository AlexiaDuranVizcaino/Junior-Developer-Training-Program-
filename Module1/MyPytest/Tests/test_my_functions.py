import pytest 
from Source import My_functions as my_functions

def test_add():
    result = my_functions.add(1,4)
    assert result == 5

def test_divide():
    result = my_functions.divide(10, 5)
    assert result == 2

def test_divide_by_zero():
    result = my_functions.divide(10/0)
    assert True