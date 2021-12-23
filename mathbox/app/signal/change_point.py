from mathbox.statistics.estimator import energy_distance
from mathbox.statistics.hypothesis_testing import permutation_test
from mathbox.optimizer.utils import argmax
from mathbox.utils import pairwise

def t_stats(a, b):
    e_distance = energy_distance(a,b)
    return e_distance * len(a) * len(b) / (len(a) + len(b))

def _calculate_t_stats(series, pvalue, permutations):
    t_value = []
    #t_value = [0] # magic
    for i in range(len(series)-1):
        a = series[:i+1]
        b = series[i+1:]
        t = t_stats(a,b)
        t_value.append(t)
    idx = int(argmax(t_value))
    a = series[:idx+1]
    b = series[idx+1:]
    if permutation_test(a, b, t_stats, pvalue, permutations):
        return (idx, t_value[idx])
    else:
        return None

def _get_next_significant_change_point(series, change_points, memo, pvalue: float, permutations: int):
    windows = [0] + sorted(change_points) + [len(series)]
    candidates = []
    for bounds in pairwise(windows):
        if bounds in memo:
            candidates.append(memo[bounds])
        else:
            a, b = bounds
            candidate = _calculate_t_stats(series[a:b], pvalue, permutations)
            if candidate is not None:
                #idx = int(argmax(stats))    # 9,8,7 #idx = int(np.argmax(stats)) # 9,0,0
                new = (candidate[0] + a, candidate[1]) # [a,b)里最大的t和它的位置
                memo[bounds] = new
                return new
            else:
                None

def e_divisive(series, jump = 5, pvalue: float = 0.05, permutations: int = 100):
    if jump != int(jump) or jump < 1:
        raise ValueError("jump must be a positive integer")
    change_points = []
    memo = {}
    while significant_change_point := _get_next_significant_change_point(
        series, change_points, memo, pvalue, permutations
    ):
        if significant_change_point is not None:
            if change_points == []:
                change_points.append(significant_change_point[0])
            else:
                result = sorted([abs(significant_change_point[0] - x) for x in change_points])
                if result[0] > jump and significant_change_point[0] > jump and significant_change_point[0] < len(series) - jump:
                    change_points.append(significant_change_point[0])
    return change_points
