import pytest
from challenge5 import valid

def test_valid():
    assert valid(1234) == True
    assert valid("") == False
    assert valid('dfjklsd') == False
    assert valid (12345) == False