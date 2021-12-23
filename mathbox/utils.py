def pairwise(alist):
    pair = []
    for i in range(len(alist)-1):
        pair.append((alist[i], alist[i+1]))
    return pair