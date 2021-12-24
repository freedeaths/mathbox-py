from pytest import approx

from ..interpolation import *


def test_point_linear_interp():
    sig_1 = (0, 1)
    sig_2 = (1, 2)
    assert point_linear_interp(1.5, sig_1[0], sig_1[1], sig_2[0], sig_2[1]) == 2.5
    assert point_linear_interp(.5, sig_1[0], sig_1[1], sig_2[0], sig_2[1]) == 1.5

def test_series_linear_interp():
    orig_time = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    orig_signal = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    desired_time = [-2, -1, 0, 1, 2, 3, 5, 6, 8, 9, 10]
    assert series_linear_interp(orig_time, orig_signal, desired_time, "linear") == desired_time
    assert series_linear_interp(orig_time, orig_signal, desired_time) == [0, 0, 0, 1, 2, 3, 5, 6, 8, 9, 9]