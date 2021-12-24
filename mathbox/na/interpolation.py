def point_linear_interp(x, x_1, y_1, x_2, y_2):
    return (y_2 - y_1) / (x_2 - x_1) * (x - x_1) + y_1

"""
extrapolation methods:
    saturation
"""
def series_linear_interp(orig_time, orig_signal, desired_time, exterp="saturation"):
    result = []
    for item in desired_time:
        if item < orig_time[0]:
            if exterp == "saturation":
                result.append(orig_signal[0])
            elif exterp == "linear":
                result.append(point_linear_interp(item, orig_time[0], orig_signal[0], orig_time[1], orig_signal[1]))
        if item > orig_time[-1]:
            if exterp == "saturation":
                result.append(orig_signal[-1])
            elif exterp == "linear":
                result.append(point_linear_interp(item, orig_time[-2], orig_signal[-2], orig_time[-1], orig_signal[-1]))
        for i in range(len(orig_time) - 1):
            if orig_time[i] <= item and item <= orig_time[i + 1]:
                result.append(point_linear_interp(item, orig_time[i], orig_signal[i], orig_time[i + 1], orig_signal[i + 1]))
                break
    return result

def fill_null(time, signal):
    pass