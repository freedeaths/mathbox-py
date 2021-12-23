import random


def permutation_test(alist, blist, estimator, p_value=0.05, times=100):
    total = alist + blist
    len_a = len(alist)
    t_stats = estimator(alist, blist)
    better_num = 0
    for _ in range(times):
        random.shuffle(total)
        new_a = total[:len_a]
        new_b = total[len_a:]
        new_t_stats = estimator(new_a, new_b)
        if new_t_stats >= t_stats:
            better_num += 1
    probability = better_num / (times + 1)
    return True if probability <= p_value else False # false means reject H0