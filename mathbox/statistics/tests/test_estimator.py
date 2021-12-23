from pytest import approx
from ..estimator import *
from ..estimator import _ncc


def test_mean():
    assert mean([1,2,3,4,5]) == 3.0
    assert mean([1.0,2.0,3.0,4.0,5.0]) == 3.0
    
def test_std():
    assert std([1,2,3,4,5],ddof=1) == 2.5
    assert std([1,2,3,4,5],ddof=0) == 2.0

def test_median():
    assert median([1,2,4,7,6]) == 4
    assert median([1.0,2.0,3.5,4.0,5.0]) == 3.5

def test__ncc():
    a = [1,2,3,4,0,1,2,3,4,0,1,2,3,4,0,1,2,3,4,0]
    b = [1,2,3,3,0,1,2,3,4,0,1,1,4,4,0,1,2,3,4,0]
    assert _ncc(a,b) == approx(0.964, abs=0.001)

def test_ncc():
    a = [0,1,2,3,4,0,1,2,3,4,0,1,2,3,4,0,1,2,3,4]
    b = [1,2,3,3,0,1,2,3,4,0,1,1,4,4,0,1,2,3,4,0]
    result = ncc(a, b, lag_max=4)
    expected = [
    (-4, approx(0.75709,abs=0.001)),
    (-3, approx(0.013114,abs=0.001)),
    (-2, approx(-0.499392,abs=0.001)),
    (-1, approx(-0.3793792,abs=0.001)),
    (0, approx(0.,abs=0.001)),
    (1, approx(0.96362,abs=0.001)),
    (2, approx(0.11803,abs=0.001)),
    (3, approx(-0.484421,abs=0.001)),
    (4, approx(-0.411908,abs=0.001))]
    assert result == expected
    a = [0,1,2,3,4,0,1,2,3,4,0,1,2,3,4,0,1,2,3]
    b = [1,2,3,3,0,1,2,3,4,0,1,1,4,4,0,1,2,3,4,0]
    result = ncc(a, b, lag_max=20)
    expected = [
    (-4, approx(0.75709,abs=0.001)),
    (-3, approx(0.013114,abs=0.001)),
    (-2, approx(-0.499392,abs=0.001)),
    (-1, approx(-0.3793792,abs=0.001)),
    (0, approx(0.,abs=0.001)),
    (1, approx(0.96362,abs=0.001)),
    (2, approx(0.11803,abs=0.001)),
    (3, approx(-0.484421,abs=0.001)),
    (4, approx(-0.411908,abs=0.001))]
    #assert result == expected