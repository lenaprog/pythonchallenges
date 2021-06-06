import pytest
from challenge3 import isPalindrome

def test_isPalindrome():
    assert isPalindrome('Anna') == True
    assert isPalindrome('123') == False
    assert isPalindrome('112211') == True