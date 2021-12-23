from ..utils import *

def test_local_minmax():
    case_1 = [1, 2, 3, 2, 1]
    print(local_minmax(case_1,True))
    print(local_minmax(case_1))
    case_2 = [0,0,1,2,3,9,9.1,9,9,3,3,3,2,-1,0,0,0]
    print("len_2: ",len(case_2))
    print(local_minmax(case_2,True))
    print(local_minmax(case_2))
    assert local_minmax(case_2) == ([(6, 9.1)], [(13, -1)])
    assert local_minmax(case_2,True) == ([(6, 9.1),(14,0),(15,0),(16,0)], [(0,0),(1,0),(13, -1)])