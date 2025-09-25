import pytest 
from Source import shapes as shapes 

def test_area():
    rectangle = shapes.Rectangle(10, 20)
    assert rectangle.area() == 10 * 20

def test_perimeter():
    rectangle = shapes.Rectangle (10, 20)
    assert rectangle.perimeter() == (10 * 2) + (20 * 2)