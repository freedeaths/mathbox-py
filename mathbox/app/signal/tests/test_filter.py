import pytest
from ..filter import *

def test_moving_average():
    assert moving_average([1,3,5,4,4],3) == [1.0,2.0,3.0,4.0,pytest.approx(4.3333,0.001)]
    
def test_moving_median():
    assert moving_median([1,2,5,9,6],3) == [1.0,1.5,2.0,5.0,6.0]