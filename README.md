# Mathbox

## Overview

A math toolbox without numpy and scipy.

## Usage

1. `pip install mathbox`
2. Download from source code, `export PYTHONPATH='/<path>/<to>/mathbox-py'`. And then get into examples folder `cd examples`, install dependencies from requirements.txt (recommended in virtualenv) and run `python xxx.py`. 

## APIs

### Time-series 1D real data

* Prerequisities

    All the signals must be well interpolated.

* Cross-correlation
  * max_corr(obj, candidates, num, lag_max)
    * obj - input: a list. The objective list whose correlated lists are concerned.
    * cadidates - input: list of lists.
    * num - input: a uint. Default is 1.
    * lag_max - input: a uint. Default is 20. The lag refers to how far the series are offset, and its sign determines which series is shifted.

    The function returns **num** pieces of list from **candidates** that are most correlated to the **obj** list. And the function will calculate the maximum correlation from -lag_max to +lag_max.
* Filters
  * moving_median(signal, window)
    * signal - input: a list.
    * window - input: an int and the odd is recommended.
  * moving_average(signal, window)
    * signal - input: a list.
    * window - input: an int.
  * f_lowpass_filter(signal, T, n=3, f_min)
    * signal - input: a list.
    * T - input: sample period time.
    * n - input: a unit. Get the **n** pieces of frequencies with the maximum amplitude.
    * f_min - input: cut-off frequency.
* Outliers detection
  * noise_outlier(noise, level)
    * noise - input: a list. Signal should obey normal distribution. So it's better to choose a white noise as input.
    * level - input: a unit. Default is 3 which means 3 sigma. Usually, it should be 1, 2, 3 or 6.
* Change points detection
  * e_divisive(signal,jump,pvalue=0.05,permutations=100)
    * signal - input: a list.
    * jump - input: a unit. Jump controls the minimum distance between change points.
    * pvalue - a float from 0~1.
    * permutations - a uint. Default is 100 which means 100 times permutation test will be done to check whether the change point is really a chnage point.

## Utils