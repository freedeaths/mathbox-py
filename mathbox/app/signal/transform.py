from math import pi, cos, sin

# >> Discrete Fourier transform for sampled signals
# x [in]: sampled signals, a list of magnitudes (real numbers)
# y [out]: a list of complex numbers
def dft(x):
    N, y = len(x), []
    for k in range(N):
        real, imag = 0, 0
        for n in range(N):
            theta = -k * (2 * pi) * (float(n) / N)
            real += x[n] * cos(theta)
            imag += x[n] * sin(theta)
        y.append(complex(real, imag))
    return y # 第一个是直流分量

def rdft(x):
    return dft(x)[:(len(x)//2)+1]


# >> Inverse discrete Fourier transform
# yr [in]: real parts of the sinusoids
# yi [in]: imaginary parts of the sinusoids
# x [out]: sampled signals (real parts only), a list of magnitude
def idft(yr, yi):
    N, x = len(yr), []
    for n in range(N):
        real, imag = 0, 0
        for k in range(N):
            theta = k * (2 * pi) * (float(n) / N)
            real += (yr[k] * cos(theta)) - (yi[k] * sin(theta))
            # imag += (yr[k] * math.sin(theta)) + (yi[k] * math.cos(theta))
        x.append(real / N)
    return x

def irdft(fourier, fix=False):
    ext_f = []
    if abs(fourier[-1].imag) and not fix < 1e-10:
        for i in range(len(fourier)-2):
            ext_f.append(fourier[-i-2].conjugate())
    else:
        for i in range(len(fourier)-1):
            ext_f.append(fourier[-i-1].conjugate())
    fourier.extend(ext_f)
    N, x = len(fourier), []
    for n in range(N):
        real, imag = 0, 0
        for k in range(N):
            theta = k * (2 * pi) * (float(n) / N)
            real += (fourier[k].real * cos(theta)) - (fourier[k].imag * sin(theta))
            # imag += (fourier[k].real * math.sin(theta)) + (fourier[k].imag * math.cos(theta))
        x.append(real / N)
    return x

def dftfreq(n, dt = 1.0):
    if not isinstance(n, int):
        raise ValueError("n should be an integer")
    val = 1.0 / (n * dt)
    results = []
    N = (n-1)//2 + 1
    p1 = [x for x in range(0, N)]
    results[:N] = p1
    p2 = [x for x in range(-(n//2), 0)]
    results[N:] = p2
    return [x * val for x in results]