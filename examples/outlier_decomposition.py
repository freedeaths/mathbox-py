import pandas as pd
import matplotlib.pyplot as plt

from mathbox.app.signal.filter import moving_median, f_lowpass_filter
from mathbox.app.signal.outlier import noise_outlier

if __name__ == '__main__':
    src_data = pd.read_csv('./data/webTraffic.csv')

    timeseries = src_data['Visite']

    med_filtered = moving_median(timeseries, window=7)
    #ave_filtered = moving_average(timeseries, window=5)

    moved_trend = [x / y for x, y in zip(timeseries, med_filtered)]

    f, seasonality = f_lowpass_filter(moved_trend, 86400, n=3, f_min=0.015/86400)

    moved_seasonality = [x / y for x, y in zip(moved_trend, seasonality)]

    outlier_lo, outlier_hi = noise_outlier(moved_seasonality, 3)
    outlier = outlier_lo + outlier_hi

    fig, axs = plt.subplots(4, 1)
    axs[0].plot(timeseries, 'b')
    axs[0].set_title('Original')
    fig.suptitle('Decomposition of Web traffic data', fontsize=16)

    axs[1].plot(med_filtered, 'g')
    axs[1].set_title('Trend')

    axs[2].plot(seasonality, 'cyan')
    axs[2].set_title('Seasonality')

    axs[3].plot(moved_seasonality, 'r')
    axs[3].plot([x[0] for x in outlier],[x[1] for x in outlier], 'bo')
    axs[3].set_title('Noise')

    plt.show()

    print("Frequency: ", f)