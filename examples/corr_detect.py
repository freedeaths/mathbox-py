import pandas as pd
import matplotlib.pyplot as plt

from mathbox.app.signal.correlation import max_corr

# repeat https://anomaly.io/detect-correlation-time-series/index.html
# TODO：
# interpolation
# TODO:
# Correlation with time shift
# https://anomaly.io/understand-auto-cross-correlation-normalized-shift/index.html#/time_shift


if __name__ == '__main__':
    src_data = pd.read_csv('./data/graphs45.csv')

    plt.subplot(2,1,1)
    n = range(src_data.shape[0])

    dfs = []
    for col in src_data.columns:
        dfs.append((col,src_data[col]))
        plt.plot(n, src_data[col])
    
    similar_7 = max_corr(dfs[3][1].tolist(), [x[1].tolist() for x in dfs], 8)[1:]
    print("most likely 7 line to No.4: ",[x[0] + 1 for x in similar_7], "likelihood: ",[x[1][1] for x in similar_7], "lag: ", [x[1][0] for x in similar_7])

    plt.subplot(2,1,2)
    for item in similar_7:
        plt.plot(n, src_data[src_data.columns[item[0]]])
    plt.show()
