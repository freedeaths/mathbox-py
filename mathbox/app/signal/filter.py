from mathbox.statistics.estimator import median
from mathbox.app.signal.transform import dftfreq, rdft, irdft
from mathbox.optimizer.utils import local_minmax

def moving_average(signal, window=3) :
    sum = 0
    result = [0 for _ in signal]
    for i in range(window):
        sum += signal[i]
        result[i] = sum / (i + 1)
    for i in range(window, len(signal)):
        sum += signal[i] - signal[i - window]
        result[i] = sum / window
    return result

def moving_median(signal, window=3):
    result = []
    for i in range(len(signal)):
        if i < window:
            result.append(median(signal[:i + 1]))
        else:
            result.append(median(signal[i - window + 1:i + 1]))
    return result

# fourier lowpass filter
# inputs:
#   timeseries: 1D timeseries signal
#   dt: sample period
#   n: number of the maximum amplitude
#   f_min: minimum frequency
# outputs:
#   freq: the frequencies whose amplitude is maximum
#   f_timeseries: filtered timeseries
def f_lowpass_filter(timeseries, dt, n=10, f_min=0.2):
    sample_num = len(timeseries)
    f = dftfreq(sample_num, dt)
    f_half = f[:((sample_num - 1) // 2) + 1]
    f_sig = rdft(timeseries)
    if f_sig[-1].imag < 1e-10:
        fix_flag = False
    else:
        fix_flag = True

    f_sig_amp = [abs(x) for x in f_sig]

    offset = f_sig_amp[0] / (sample_num)

    amp_max_pos = [i[0] for i in local_minmax(f_sig_amp)[0]]
    amp_max = [e for i, e in enumerate(f_sig_amp) if i in amp_max_pos]
    amp_desc_pos = [i[0] for i in sorted(enumerate(amp_max), key=lambda x:x[1], reverse=True)]
    
    if len(amp_desc_pos) > n:
        amp_desc_pos = amp_desc_pos[:n]
    amp_max_n_pos = [amp_max_pos[i] for i in amp_desc_pos]

    freq = [f_half[x] for x in amp_desc_pos]
    for i in range(len(f_sig)):
        if i not in amp_max_n_pos:
            f_sig[i] = 0

    for i in range(len(f_half)):
        if f_half[i] < f_min:
            f_sig[i] = 0
    
    f_timeseries = irdft(f_sig, fix_flag)
    f_timeseries = [x + offset for x in f_timeseries]
    return (freq, f_timeseries)