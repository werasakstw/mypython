import random
import statistics as st

xr = range(1000)
standard = [random.random() for _ in xr]        # 0.0 -> 1.0
uniform = [random.uniform(0, 2.0) for _ in xr]  # 0.0 -> 2.0
gaussian = [random.gauss(0.5, 0.1) for _ in xr] # mean = 0.5, sd = 0.1

# NumPy Distribution
import numpy as np
np_normal = np.random.standard_normal(size=1000)  # mean=0, sd=1
np_uniform = np.random.uniform(low=0, high=2.0, size=1000)
np_gaussian = np.random.normal(loc=0.5, scale=0.1, size=1000)

# Dispersion: max - min    is the range between min and max.
# Large value means spread. Small value means condense.
def dispersion():
    def dis(d):
        return max(d) - min(d)
    print(dis(standard), dis(np_normal))   # 0.9981800157380463 5.9513317093990015
    print(dis(uniform), dis(np_uniform))   # 1.9994439094662921 1.9919422080679758
    print(dis(gaussian), dis(np_gaussian)) # 0.6113863030664262 0.5955687755045911
##dispersion()

def dist_test():
    print('\t\tstandard', '\tuniform', '\tgaussian')
    print('min/max: \t(%.2f/%.2f)\t(%.2f/%.2f)\t(%.2f/%.2f)' %
          (min(standard), max(standard),
           min(uniform), max(uniform),
           min(gaussian), max(gaussian)))
    print('Mean: \t\t%.2f\t\t%.2f\t\t%.2f' %
          (st.mean(standard), st.mean(uniform), st.mean(gaussian)))
    print('Sd: \t\t%.2f\t\t%.2f\t\t%.2f' %
          (st.pstdev(standard), st.pstdev(uniform), st.pstdev(gaussian)))
##dist_test()

#------------------------------------------------------------------

# Visualizing Random Distributions
import matplotlib.pyplot as pl
def scatter_test():
    pl.figure(1)
    pl.scatter(xr, standard, color='r')
    pl.scatter(xr, uniform, color='g')
    pl.scatter(xr, gaussian, color='b')
    pl.figure(2)
    pl.scatter(xr, np_normal, color='tab:orange')
    pl.scatter(xr, np_uniform, color='tab:purple')
    pl.scatter(xr, np_gaussian, color='tab:pink')
    pl.show()
##scatter_test()

# Histogram
def hist_test():
    pl.figure()
    pl.subplot(231)
    pl.hist(standard)
    pl.title('standard')

    pl.subplot(232)
    pl.hist(uniform)
    pl.title('uniform')

    pl.subplot(233)
    pl.hist(gaussian)
    pl.title('gaussian')
    
    pl.subplot(234)
    t1 = [ random.triangular(-1.0, 1.0, 0.5) for _ in xr] # min, max, peak
    pl.hist(t1)
    pl.title('triangular 1')

    pl.subplot(235)
    t2 = [ random.triangular(0.0, 10.0, 2.0) for _ in xr]
    pl.hist(t2)
    pl.title('triangular 2')

    pl.subplot(236)
    t3 = [ random.triangular() for _ in xr] # Default: min = 0, max = 1, peak = 0.5
    pl.hist(t3)
    pl.title('triangular 3')
    
    pl.tight_layout()
    pl.show()
##hist_test()

# Uniform distribution in ranges
# random.random() is random.uniform(0, 1.0)
def uniform_range():
    u1 = [random.uniform(-1.0, 1.0) for _ in xr] ## -1 -> 1
    u2 = [random.uniform(0, 1.0) for _ in xr]    ## 0 -> 1
    u3 = [random.uniform(0, 2.0) for _ in xr]    ## 0 -> 2
    pl.scatter(xr, u1, color='r')
    pl.scatter(xr, u2, color='g')
    pl.scatter(xr, u3, color='b')
    pl.show()
##uniform_range()

# Uniform distribution with steps
# random.randrange(<start>, <stop>, <step>)
def uniform_step():
    u1 = [random.randrange(0, 100) for _ in xr]
    u2 = [random.randrange(0, 100, 10) for _ in xr]
    u3 = [random.randrange(0, 100, 30) for _ in xr]
    pl.scatter(xr, u1, color='r')
    pl.scatter(xr, u2, color='g')
    pl.scatter(xr, u3, color='b')
    pl.show()  
##uniform_step()

## Gaussian (Normal) with vary means
def gauss_mean():
    g1 = [random.gauss(1.0, 0.1) for _ in xr] ## mean = 1.0, sd = 0.1
    g2 = [random.gauss(2.0, 0.1) for _ in xr] ## mean = 2.0, sd = 0.1
    g3 = [random.gauss(3.0, 0.1) for _ in xr] ## mean = 3.0, sd = 0.1
    pl.scatter(xr, g3, color='b')
    pl.scatter(xr, g2, color='g')
    pl.scatter(xr, g1, color='r')
    pl.show()
##gauss_mean()

## Gaussian (Normal) with vary SD
def gauss_sd():
    g1 = [random.gauss(1.0, 0.1) for _ in xr] ## mean = 1.0, sd = 0.1
    g2 = [random.gauss(1.0, 0.2) for _ in xr] ## mean = 1.0, sd = 0.2
    g3 = [random.gauss(1.0, 0.3) for _ in xr] ## mean = 1.0, sd = 0.3
    pl.scatter(xr, g3, color='b')
    pl.scatter(xr, g2, color='g')
    pl.scatter(xr, g1, color='r')
    pl.show()
##gauss_sd()

#--------------------------------------------------------------------------

# A scatter plot is often used to visual the correlation or a potential association between two variables.
def correlate():
    # The controlled x values
    x = np.random.rand(1000)

    # random measurements, no correlation
    y1 = np.random.rand(len(x))
    
    # some (unknow function) correlation
    y2 = np.exp(x) - x/1.3

    pl.subplot(121)
    pl.scatter(x, y1)

    pl.subplot(122)
    pl.scatter(x, y2)
    pl.show()
##correlate()

''' Logarithmic Plots
semilgox() and semilogy() plot the x-axis and y-axis in logarithmic scale.
loglog() plot both the x-axis and y-axis in logarithmic scale.

np.logspace() generates logarithmically spaced values between 10**start
and 10**stop which 'num' specifies how many values in the range. '''
##print(np.logspace(1, 5, num=3))

def log_plot():
    def db(x):  
        return 20*np.log10(abs(x))  ## decibels

    energy = np.logspace(1, 5, num=10)
    loudness = range(1, 1000, 100)
    decibels = [ db(x) for x in energy ]
    
    pl.semilogx(energy, loudness)
    pl.semilogx(energy, decibels)
    pl.show()
##log_plot()



