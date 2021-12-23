from ..differential import *

def test_diff():
    assert diff([1,2,5,4,6]) == [1,3,-1,2]