from mathbox.statistics.estimator import ncc


def max_corr(obj, set, num, lag=20):
    ccfs = []
    for i in range(len(set)):
        ncc_list = ncc(obj, set[i])
        ccfs.append((i, max(ncc_list, key=lambda x: x[1])))
    sorted_res = sorted(ccfs, key=lambda d: d[1][1], reverse=True)
    return sorted_res[:num]
