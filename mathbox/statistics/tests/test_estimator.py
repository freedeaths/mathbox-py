from ..estimator import *


def test_mean():
    assert mean([1,2,3,4,5]) == 3.0
    assert mean([1.0,2.0,3.0,4.0,5.0]) == 3.0
    
def test_std():
    assert std([1,2,3,4,5],ddof=1) == 2.5
    assert std([1,2,3,4,5],ddof=0) == 2.0

def test_median():
    assert median([1,2,4,7,6]) == 4
    assert median([1.0,2.0,3.5,4.0,5.0]) == 3.5