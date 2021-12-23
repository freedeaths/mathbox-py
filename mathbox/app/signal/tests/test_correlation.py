from pytest import approx
from ..correlation import *

def test_max_corr():
    a = [0,1,2,3,4,0,1,2,3,4,0,1,2,3,4,0,1,2,3,4]
    b = [1,2,3,3,0,1,2,3,4,0,1,1,4,4,0,1,2,3,4,0]
    c = [2,3,4,0,1,2,3,4,0,1,2,3,4,0,1,2,3,4,0,1]
    result = max_corr(a, [b, c], 2)
    assert result[0][0] == 1
    assert result[0][1] == approx((2, 0.98917305),abs=0.001)
    assert result[1][0] == 0
    assert result[1][1] == approx((1, 0.96362),abs=0.001)

    