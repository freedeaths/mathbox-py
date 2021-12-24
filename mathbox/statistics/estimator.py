

def mean(samples):
    return sum(samples) / len(samples)

"""
ddof == 1 provides an unbiased estimator of the variance of the infinite population.
ddof == 0 provides a maximum likelihood estimate of the variance for normally distributed variables.
"""
def var(samples, ddof=1):
    if ddof != 1 and ddof != 0:
        raise ValueError("ddof must be 0 or 1")
    x_bar = mean(samples)
    return sum([(x - x_bar) ** 2 for x in samples]) / (len(samples) - ddof)

def std(samples, ddof=1):
    if ddof != 1 and ddof != 0:
        raise ValueError("ddof must be 0 or 1")
    return var(samples, ddof=ddof) ** 0.5


def median(samples) :
    samples = sorted(samples)
    if len(samples) % 2 == 0:
        return (samples[len(samples) // 2 - 1] + samples[len(samples) // 2]) / 2
    else:
        return samples[len(samples) // 2]

# TODO:
# Correlation with time shift
# https://anomaly.io/understand-auto-cross-correlation-normalized-shift/index.html#/time_shift
def _ncc(x,y):
    x_mean = mean(x)
    y_mean = mean(y)
    x_qsum  = 0
    y_qsum  = 0
    xy_sum  = 0
    for i in range(len(x)):
        x_qsum += (x[i] - x_mean) ** 2 + 1e-10
        y_qsum += (y[i] - y_mean) ** 2 + 1e-10
        xy_sum += (x[i] - x_mean) * (y[i] - y_mean)
    return xy_sum / (x_qsum * y_qsum) ** 0.5

def ncc(x,y,lag_max=20):
    i = len(x)
    j = len(y)
    if lag_max >= min(i,j):
        lag_max = min(i,j) - 1
    ncc_list = []
    result = []
    # can be optimized by i > j or i < j
    new_x = [0 for _ in range(j - 1)] + x + [0 for _ in range(j - 1)]
    for lag in range(i + j -1):
        ncc_list.append((lag + 1 - i, _ncc(y, new_x[lag:lag+j])))
    for lag in range(i - lag_max - 1, i + lag_max):
        result.append(ncc_list[lag])
    return result
    

def _operator_4_e_dist(a,b):
    # distance[i * len_a + j(0~len_b)]
    len_a = len(a)
    len_b = len(b)
    distance = []
    sum = 0
    for i in range(len_a):
        row_distance = []
        for j in range(len_b):
            row_distance.append(abs(a[i]-b[j]))
            sum += abs(a[i]-b[j])
        distance.append(row_distance)
    return distance, sum / (len_a * len_b)

def energy_distance(a, b, normalize=False):
    _,A = _operator_4_e_dist(a,b)
    _,B = _operator_4_e_dist(a,a)
    _,C = _operator_4_e_dist(b,b)
    e_distance = (2* A - B - C)
    normailized_e_distance = e_distance / (2 * A + 1e-10)
    if normalize:
        return normailized_e_distance
    else:
        return e_distance

