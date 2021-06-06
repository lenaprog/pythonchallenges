import pytest
from testing_strings import convert

def test_convert():
    assert convert('small') == 'SMALL'
    assert convert('Lena') =='LENA'
