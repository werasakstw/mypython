import matplotlib.pyplot as pl
import math
def math_plot():
    x = range(1, 10)
    pl.plot(x, [i+1 for i in x])
    pl.plot(x, [i+i for i in x])
    pl.plot(x, [i*i for i in x])
##    pl.plot(x, [i**3 for i in x])
    pl.show()
##math_plot()

# NumPy arrays support aggregations and high density ranges.
import numpy as np
def numpy_plot():
    x = np.array(range(10))
##    x = np.arange(0, 10)
    pl.plot(x, x+1)
    pl.plot(x, x+x)
    pl.plot(x, x*x)
    pl.show()
##numpy_plot()

# NumPy linear spaces provides more points and smoother graphs.
def np_range():  
    # Python range() is a sequence of int.
    xr = range(1, 10)       # print(len(xr))   # 9
    pl.plot(xr, [1 - (1/x) for x in xr])
    
    # Numpy array is a list of float.
    xa = np.arange(1, 10)    # print(len(xa)) # 9
    pl.plot(xr, 1 - (2/xa)) 
    
    # Numpy's linspace() is a list of many floats.
    xs= np.linspace(1, 10)   # print(len(xs)) # 50
    pl.plot(xs, 1 - (3/xs))
    pl.show()
##np_range()

# Math plots for different frames.
def eq_plots():
    pl.figure()
    x = np.linspace(-100, 100)
    
    pl.subplot(221)
    pl.title('Linear')
    pl.plot(x, 2*x + 1)

    pl.subplot(222)
    pl.title('Parabola')
    pl.plot(x, x**2 + x + 1)

    pl.subplot(223)
    pl.title('Polynomial')
    pl.plot(x, x**3 + x**2 + x + 1)

    pl.subplot(224)
    pl.title('Square')
    pl.plot(x, x**2)
    
    pl.tight_layout() 
    pl.show()
##eq_plots()

def trigonometry():
    x = np.linspace(0, 4*np.pi)
    pl.plot(x, np.sin(x))
    pl.plot(x, np.cos(x))
##    pl.plot(x, np.tan(x))
    pl.show()
##trigonometry()

def log_power():
    pl.figure()
    x= np.linspace(1, 100);
    
    pl.subplot(211)
    pl.title('Log')
    pl.plot(x, np.log(x))
    pl.plot(x, np.log2(x))
    pl.plot(x, np.log10(x))

    pl.subplot(212)
    pl.title('Power')
    pl.plot(x, np.power(x, 2))
    pl.plot(x, np.power(x, 2.2))
    pl.plot(x, np.power(x, 2.5))
    
    pl.tight_layout()
    pl.show()
##log_power()

def parabola():
    # Limit x and y axis ranges.
    pl.xlim([-5, 5])
    pl.ylim([-10, 10])

    x = np.linspace(-4, 4)     # k  is black
    pl.plot(x, [0 for _ in x], 'k')   # x-axis
    pl.plot([0 for _ in x], 2*x, 'k') # y-axis
    
    # b**2 < 4*a*c   there are no solutions.
    b, a, c = 1, 1, 1
    y = a*x**2 + b*x + c
    pl.plot(x, y)

    # b**2 = 4*a*c   there is one solution.
    b, a, c = 2, 1, 1
    y = a*x**2 + b*x + c
    pl.plot(x, y)

    # b**2 > 4*a*c   there are two solutions.
    b, a, c = 3, 1, 1
    y = a*x**2 + b*x + c
    pl.plot(x, y)
    pl.show()   
##parabola()
