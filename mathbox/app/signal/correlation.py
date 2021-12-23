from mathbox.statistics.estimator import ncc


def max_corr(obj, set, num):
    ccfs = []
    for i in range(len(set)):
        ccfs.append((set[i][0],ncc(obj[1], set[i][1])))
    sorted_res = sorted(ccfs, key=lambda d: d[1], reverse=True)
    return sorted_res[1 : num + 1]