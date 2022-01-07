from mathbox.statistics.estimator import pcc


def max_corr(obj, set, num=1, lag=20):
    ccfs = []
    for i in range(len(set)):
        pcc_list = pcc(obj, set[i], lag)
        ccfs.append((i, max(pcc_list, key=lambda x: x[1])))
    sorted_res = sorted(ccfs, key=lambda d: d[1][1], reverse=True)
    return sorted_res[:num]
