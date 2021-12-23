from mathbox.statistics.estimator import mean, std

def noise_outlier(noise, bias=3):
    noise_mean = mean(noise)
    noise_std = std(noise)
    return [(i,x) for i,x in enumerate(noise) if abs(x - noise_mean) > bias * noise_std]

def simple_outlier(series, bias=3):
    sorted_series = sorted(series)
    length = len(series)
    q3 = sorted_series[int(length * 0.75)]
    q1 = sorted_series[int(length * 0.25)]
    outlier_lo = [(i,x) for i,x in enumerate(series) if x < q1 - bias * (q3 - q1)]
    outlier_hi = [(i,x) for i,x in enumerate(series) if x > q3 + bias * (q3 - q1)]
    return outlier_lo, outlier_hi

# Generalized ESD Test for Outliers
# https://www.itl.nist.gov/div898/handbook/eda/section3/eda35h3.htm
def gesd():
    pass