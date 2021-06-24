
# pip install numpy
# pip install scipy

# Round off:
##print(round(1.2345, 2))    # 1.23
##print('%.2f' % 1.2345)     # 1.23

import statistics as st
import numpy as np
a = list(range(10))        # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Built-in Python Functions and Numpy:
##print(len(a), sum(a), min(a), max(a))               # 10 45 0 9
##print(np.size(a), np.sum(a), np.min(a), np.max(a))  # 10 45 0 9

#-------------------------------------------------------------

# 'Median' is the middle element in the sorted sequence.
def median_test():
    b = list(range(11)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    def median(d):
        n = len(d)
        d.sort()
        m = n // 2
        if n % 2 == 0:      # n is even
            return (d[m] + d[m - 1])/2
        return d[m]         # n is odd

    print(median(a), median(b))         # 4.5 5  
    print(st.median(a), st.median(b))   # 4.5 5
    print(np.median(a), np.median(b))   # 4.5 5.0
##median_test()

#-------------------------------------------------------------

# 'Mean' is the average of elements in the sequence.
def mean_test():
    def mean(seq):
        return sum(seq)/len(seq)

    print(mean(a), st.mean(a), np.mean(a) )  # 4.5 4.5 4.5

    # st.fmean() is float mean. (runs faster and always returns a float)
    print(st.fmean(a))                      # 4.5

    c = a[1:]  # Exclude 0 position.

    # Geometric Mean:
    print(st.geometric_mean(c))   # 4.147166274396913

    from scipy.stats import gmean
    print(gmean(c))               # 4.147166274396913

    # Harmonic Mean:
    print(st.harmonic_mean(c))    # 3.1813718614111375

    from scipy.stats import hmean
    print(hmean(c))               # 3.1813718614111375
##mean_test()

#-----------------------------------------------------------------------

# 'Variance' is the average of the square of deviations from the mean.
#     variance = sum((value - mean)**2) / len
def variance_test():
    def variance(seq):
        return st.mean([(i - st.mean(seq))**2 for i in seq])

    print(variance(a), np.var(a))       # 8.25 8.25

    # Statistics Population variance:
    print(st.pvariance(a))              # 8.25

    # Statistics Sample variance:
    print(st.variance(a))               # 9.166666666666666
##variance_test()

#-----------------------------------------------------------------------

''' The variance is the square of the value unit.
'Standard Deviation(SD)' is the square root of variance.
            sd = sqrt(variance)
'''
import math
def sd_test():
    def sd(seq):
        return math.sqrt(np.var(seq))

    print(sd(a), np.std(a))  # 2.8722813232690143 2.8722813232690143

    # Statistics Population SD
    print(st.pstdev(a))      # 2.8722813232690143
        
    # Statistics Sample SD
    print(st.stdev(a))       # 3.0276503540974917
##sd_test()

#-----------------------------------------------------------------------

def quantile_test():
    # st.quantiles() divides <seq> into n intervals with equal probability.
    # By default n=4, method='exclusive'.
    print(st.quantiles(a))                          # [1.75, 4.5, 7.25]
    print(st.quantiles(a, method='inclusive'))      # [2.25, 4.5, 6.75]   
    print(st.quantiles(a, n=10)) # [0.1, 1.2, 2.3, 3.4, 4.5, 5.6, 6.7, 7.8, 8.9]

    # np.quantile(<seq>, q) Compute the q-th quantile of the <seq>. 
    print(np.quantile(a, 0.1))   # 0.9
    print(np.quantile(a, 0.5))   # 4.5
    print(np.quantile(a, 1.0))   # 9.0
##quantile_test()

#-----------------------------------------------------------------------

grades = ['C', 'B', 'C', 'D', 'C', 'A', 'B', 'C', 'D']
def mode_test():
    # mode(<seq>) returns the most common element.
    print(st.mode(grades))       # C

    # multimode(<seq>) returns the list of the most common element.
    print(st.multimode(['c', 'b', 'c', 'd', 'a', 'b']))  # ['c', 'b']

    from scipy.stats import mode
    m = mode(scores)
    print(m[0], m[1])       # ['C'] [4]
        # The most common element,  Number of occurrences.
##mode_test()

#-----------------------------------------------------------------------

from collections import Counter
def frequency_count():
    c = Counter(grades)
    print(c.most_common())  # [('C', 4), ('B', 2), ('D', 2), ('A', 1)]
    print(c.most_common(1)) # [('C', 4)]
    print(c.most_common(2)) # [('C', 4), ('B', 2)]

    # Accessing the number of occurrences.
    m = c.most_common(1)
    print(m[0][0], m[0][1]) # C 4
##frequency_count()

#-----------------------------------------------------------------------

scores = [1, 4, 1, 0, 1, 1, 2, 2, 2, 4]  # must be array of int
def bin_count():   
    c = np.bincount(scores)
    print(c)   # [1 4 3 0 2]
    
    # Frequency count
    for i, v in enumerate(c):
        print('(%d: %d)' % (i, v), end=', ')
            # (0: 1), (1: 4), (2: 3), (3: 0), (4: 2),
    print()
    
    value, count = np.unique(scores, return_counts=True)
    print(value, count)  # [0 1 2 4] [1 4 3 2]
##bin_count()

def bin_sort():
    c = np.bincount(scores)
    s = list()
    for i, v in enumerate(c):
        for _ in range(v):
            s.append(i)
    print(s)    # [0, 1, 1, 1, 1, 2, 2, 2, 4, 4]
##bin_sort()
    
#------------------------------------------------------------#

# Different from Mean: A list of different from mean.
def dif_mean(seq):
    m = st.mean(seq)
    return [x - m for x in seq]
##print(dif_mean(a)) # [-4.5, -3.5, -2.5, -1.5, -0.5, 0.5, 1.5, 2.5, 3.5, 4.5]

# dot(a, b) sums up the products of corresponding pairs of a and b.
def dot_test():
    a = [1, 2]
    b = [3, 4]
    print([(x, y) for x, y in zip(a, b)])   # [(1, 3), (2, 4)]
    print(np.dot(a,b))                      # 11
##dot_test()

# Covariance defines how much two sequences resemble.
# High values indicate similar, low values different.
def covariance(x, y):   # 'x' and 'y' must be equal size.
    return np.dot(dif_mean(x), dif_mean(y)) / (len(x) - 1)

import random
def covariance_test():
    print(covariance([1, 2, 3], [5, 8, 9]))     # 2.0
    print(covariance([1, 2, 3], [1, 1, 1]))     # 0.0

    for _ in range(10):
        i, j, k = random.random(), random.random(), random.random()
        print('%.2f, %.2f, %.2f: %.4f' % (i, j, k, covariance([1, 2, 3], [i, j, k])))
##covariance_test()

def correlate(x, y):
    sdx = np.std(x)
    sdy = np.std(y)
    if sdx > 0 and sdy > 0:
        return covariance(x, y) / sdx / sdy 
    return 0
def correlate_test():
    print(correlate([1, 2, 3], [5, 8, 9]))     # 1.441153384245784
    print(correlate([1, 2, 3], [1, 1, 1]))     # 0

    for _ in range(10):
        i, j, k = random.random(), random.random(), random.random()
        print('%.2f, %.2f, %.2f: %.4f' % (i, j, k, correlate([1, 2, 3], [i, j, k])))
##correlate_test()

''' Let define:
      n = size of sequence
      sx = Sum of the numbers in set x
      sy = Sum of the numbers in set y
      sxy = Sum of the products in set x and y
      ssx = Square of sx
      ssy = Square of sy
      sxs = Sum of the squares of the numbers in set x
      sys = Sum of the squares of the numbers in set y
         correlation = (n*sxy - sx*sy)/sqrt((n*sxs - ssx)*(n*sys - ssy))
'''
def correlation(x, y):
    n = len(x)
    sx = sum(x)
    sy = sum(y)
    sxy = sum([xi*yi for xi, yi in zip(x, y)])
    ssx = sx*sx
    ssy = sy*sy
    sxs = sum([i*i for i in x])
    sys = sum([i*i for i in y])
    return (n*sxy - sx*sy)/math.sqrt((n*sxs - ssx)*(n*sys - ssy))

def correlation_test():
    x = range(1000);
    y1 = [i + 10 for i in x]        # y = x + 10
    y2 = [2*i for i in x]           # y = 2*x
    y3 = [i**2 for i in x]          # y = x**2
    y4 = [i**2 + i + 1 for i in x]  # y = x**2 + x + 1
    
    y5 = [random.random() for _ in x] # no relationship
    for y in [y1, y2, y3, y4, y5]:
        print(round(correlation(x, y), 3), round(correlate(x, y), 3))
##correlation_test()

####################################################################

d = list(range(10))
def statistics_module():
    print(st.mean(d))   
    print(st.median(d))
    print(st.median_grouped(d))  ## 50th percentile
    print(st.variance(d))
    print(st.pstdev(d))       ## standard deviation
    print(st.pvariance(d))    ## population variance
    print(st.mode([3, 1, 4, 3, 2])) ## most common element, must be unique
##statistics_module()

import scipy.stats as st
from scipy.stats import scoreatpercentile
def scipy_stats():
    n, min_max, mean, var, skew, kurt = st.describe(d)
    print('Number of elements: %d' % n)
    print('Min: %1.2f  Max: %1.2f' % (min_max[0], min_max[1]))
    print('Mean: %1.2f' % mean)
    print('Variance: %1.2f' % var)
    print('Skewness: %1.2f' % skew)
    print('Kurtosis: %1.2f' % kurt)
    print('Score at percentile 50: ', scoreatpercentile(d, 50))
##scipy_stats()

def numpy_stats():
    d = np.random.rand(10)
    print('Number of elements: %d' % len(d))
    print('sum: %1.2f' % d.sum())
    print('Min: %1.2f  Max: %1.2f' % (d.min(), d.max()))
    print('Mean: %1.2f' % d.mean())
    print('Median: %1.2f' % np.median(d))
    print('Variance: %1.2f' % d.var())
    print('Std: %1.2f' % d.std())
##numpy_stats()

# Numpy Array
import csv
def numpy_array():
    def read(file):
        d = []
        with open(file) as f:
            f_csv = csv.DictReader(f)
            for r in f_csv:
               d.append(r['happy_index'])
        return np.array(d, dtype=np.float32)
        
    a = read('data/happy.csv')
    print('sum: %1.2f' % a.sum())
    print('Min: %1.2f  Max: %1.2f' % (a.min(), a.max()))
    print('Mean: %1.2f' % a.mean())
    print('Median: %1.2f' % np.median(a))
    print('Variance: %1.2f' % a.var())
    print('Std: %1.2f' % a.std())
##numpy_array()
