import pytest
from challenge4 import wash_hands

def test_wash_hands():
    assert wash_hands(6, 2) == "126 minutes and 0 seconds."