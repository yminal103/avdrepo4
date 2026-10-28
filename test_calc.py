import pytest
from calc import add, sub, mul, div

def test_add(a,b):
    assert add(20,10) == 30

def test_sub(a,b):
    assert sub(20,10) == 10

def test_mul(a,b):
    assert mul(20,10) == 200

def test_div(a,b):
    assert div(20,10) == 2