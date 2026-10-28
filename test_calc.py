# RULE1: Functions should not take any parameters

import pytest
from calc import add, sub, mul, div

def test_add():
    assert add(20,10) == 30

def test_sub():
    assert sub(20,10) == 10

def test_mul():
    assert mul(20,10) == 200

def test_div():
    assert div(20,10) == 2