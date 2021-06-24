# pip install numpy
import numpy as np
'''
Vector: one-dimensional array
Numpy provides homogeneous array, Python lists are generic.
          np.array(<size>)
'''
def np_array():
    # Numpy range:
    nr = np.arange(10)
    print(nr)                 # [0 1 2 3 4 5 6 7 8 9]
    print(nr.dtype, type(nr)) # int32 <class 'numpy.ndarray'>

    # Numpy array: an alternative form of numpy range.
    a = np.array(range(10))
    print(a)                  ## [0 1 2 3 4 5 6 7 8 9]
    print(a.dtype, type(a))   ## int32  <class 'numpy.ndarray'>
    print(a.size, a.itemsize) # 10 4
    
    ## Data Types:   int32 is the default.
    ## bool, inti, int8, int16, int32, int64, uint8, uint16, uint32, uint64
    ## float16, float32, float64, complex64, complex128
    print(np.array(range(3), dtype=np.complex64))    ## [0.+0.j 1.+0.j 2.+0.j]
##np_array()

# Aggregate Operations: Applicative  Programming.
def agg_op():
    a = np.array(range(5))
        ## Aggregate Operations: +, -, *, /, %, **
    print(a+1)      ## [ 1  2  3  4  5 ]
    print(a*2)      ## [ 0  2  4  6  8 ]
    print(a**2)     ## [ 0  1  4  9 16 ]
    print(np.sqrt(a)) # [0.         1.         1.41421356 1.73205081 2.

    # Binary Operator: +, -, *, /, %, **
    b = a+1
    print(b)          # [1 2 3 4 5]
    print(a + b)      # [1 3 5 7 9]
    print(a - b)      # [-1 -1 -1 -1 -1]
    print(a * b)      # [ 0  2  6 12 20]
    print(a / b)      # [0.         0.5        0.66666667 0.75       0.8       ]
    print(a ** b)     # [   0    1    8   81 1024]

    # Comparison Operations:
    print(a == 2)   # [False False  True False False]
    
    # Built-in functions:
    print(a.sum(), a.min(), a.max(), a.mean())  # 10 0 4 2.0

    # Alternatively:
    print(np.sum(a), np.min(a), np.max(a), np.mean(a), np.average(a))
##agg_op()

def filters():
    a = np.array(range(10))
    
    # clip(min, max): clips values into a range.
    print(a.clip(2, 8))  # [2 2 2 3 4 5 6 7 8 8]

    # Aggreagate Selection:
    print(a > 7)  # [False False False False False False False False  True  True]
    print(a[a > 7]) # [8 9]
    
    # Boolean Filter.
    b = np.array([False, True, False, True, False, True, False, True, False, True])
    print(a[b])         # [1 3 5 7 9]

    c = np.array([2, 4, 1, 5, 3, 1, 5, 2])
    print(c.argmin())   # 2  (first index of 1)
    print(c.argmax())   # 3  (first index of 5)

    # Filter Assignement
    a[a>1] = 3
    print(a)            # [0 1 3 3 3 3 3 3 3 3]
##filters()

def slice_test():
    a = np.array(range(10))
    print(a[2:5])   ## [2 3 4]
    print(a[:7:2])  ## [0 2 4 6]
    print(a[::-1])  ## [9 8 7 6 5 4 3 2 1 0]
    
    # Slice Assignment
    a[2:] = [1] * 8
    print(a)                    ## [0 1 1 1 1 1 1 1 1 1]

    a[1:8:2] = 2                ## [0 2 1 2 1 2 1 2 1 1]
    print(a)

    a[a>1] = 3                  ## [0 3 1 3 1 3 1 3 1 1]
    print(a)
slice_test()

def array_create():
    print(np.zeros(10, dtype=int))   # [0 0 0 0 0 0 0 0 0 0]
    print(np.ones(3, dtype=complex)) # [1.+0.j 1.+0.j 1.+0.j]
    
    # Create from range
    print(np.arange(2, 6))           # [2 3 4 5]
    print(np.arange(0, 1, 0.3))      # [0.  0.3 0.6 0.9]

    # Create from  array
    print(np.array([2, 1, 3]))       # [2 1 3]
    print(np.array([1] * 4))         # [1 1 1 1]
    print(np.array([1, 2] * 2))      # [1 2 1 2]
    
    # Linear Spaces
    print(np.linspace(0, 1))         # 50 points in range [0, 1]
    print(np.linspace(0, 10, 5))     # [ 0.   2.5  5.   7.5 10. ]

    # Deep Copy:
    a = np.array(range(5))
    b = np.array(a)         # Alternatively:  b = a.copy()
    b[0] = 1
    print(a, b, a is b)     # [0 1 2 3 4] [1 1 2 3 4] False

    # Shallow Copy:
    c = a                   # Array assignment is shallow copy.
    # c = a.view()          # Alternatively: create a view to an existing array
    c[0] = 1
    print(a, c, a is c)     # [1 1 2 3 4] [1 1 2 3 4] False
##array_create()

# Ex.
def income():
    # Woking Hours for 3 days
    john = [99, 101, 103]
    jack = [110, 108, 105]
    joe = [90, 88, 85]

    # Rates per hour
    rates = [6, 3, 5]
    incomes = np.array([john, jack, joe]) * rates
    print(incomes)
    
    tax = 0.07
    print(incomes - incomes*tax)
##income()

#--------------------------------------------------------------

# Multi Dimensions Array:
def mul_dim():
    # Create zeros array with dimension defined by a tuple.
    print(np.zeros( (2, 2) ))   # [[0. 0.]
                                #  [0. 0.]]

    # Create two dimensions array from list of lists or ranges.
    #          array([dim1, dim2, dim3, ...])
    m = np.array([ [0, 1], [2, 3] ])
    # m = np.array([np.array(range(2)), np.array(range(2, 4))])
    print(m)        # [[0 1]
                    #  [2 3]]                   
    print(m.shape)  # (2, 2)   tuple of each dimension size
    
    # Indexing
    print(m[0], m[0][0])     # [0 1] 0

    # Three Dimension Array:
    c = np.array([ [[0, 1], [2, 3]],
                   [[4, 5], [6, 7]]])
    # c = np.array([[np.arange(2), np.arange(2,4)],
    #              [np.arange(4,6), np.arange(6,8)]])
    print(c)        # [[[0 1]
                    #   [2 3]]
                    #
                    # [[4 5]
                    #  [6 7]]]
    print(c.shape)  # (2, 2, 2)
    print(c[0], c[0][0], c[0][0][0])  # [[0 1]
                                      #  [2 3]] [0 1] 0
##mul_dim()

def slicing():
    a = np.array(range(10))
    print(a[2:])        # [2 3 4 5 6 7 8 9]
    print(a[:2])        # [0 1]
    print(a[::2])       # [0 2 4 6 8]
    print(a[::-1])      # [9 8 7 6 5 4 3 2 1 0]

    # Slice asignment:
    a[2:] = [1] * 8
    print(a)                    # [0 1 1 1 1 1 1 1 1 1]

    a[1:8:2] = 2                # [0 2 1 2 1 2 1 2 1 1]
    print(a)
##slicing()

def shape_test():
    a = np.array(range(10))
    print(a.shape)          # (10,)
    
    print(a.reshape(2, 5))  # [[0 1 2 3 4]
                            #  [5 6 7 8 9]]

    a.shape = (5, 2)    # alternatively 
    print(a)                # [[0 1]
                            # [2 3]
                            # [4 5]
                            # [6 7]
                            # [8 9]] 
    # Transpose:
    a = np.array(range(9)).reshape(3,3)
    print(a)                # [[0 1 2]
                            #  [3 4 5]
                            #  [6 7 8]]
    
    print(a.transpose())    # [[0 3 6]
                            #  [1 4 7]
                            #  [2 5 8]]
    
    print(a.flatten())      # [0 1 2 3 4 5 6 7 8]
##shape_test()

def stacking():
    a = np.arange(9).reshape(3,3); print(a)
                             # [[0 1 2]
                             # [3 4 5]
                             # [6 7 8]]
    
    b = 2*a; print(b)        # [[ 0  2  4]
                             # [ 6  8 10]
                             # [12 14 16]]
    
    # Hlorizontal stacking    
    print(np.hstack((a, b)))    # concatenate((a, b), axis=1)
        # [[ 0  1  2  0  2  4]
        # [ 3  4  5  6  8 10]
        # [ 6  7  8 12 14 16]]
    
    # Vertical stacking
    print(np.vstack((a, b)))    # concatenate((a, b), axis=0)
        # [[ 0  1  2]
        # [ 3  4  5]
        # [ 6  7  8]
        # [ 0  2  4]
        # [ 6  8 10]
        # [12 14 16]]
 
    # Depth stacking
    print(np.dstack((a, b)))
        # [[[ 0  0]
        #  [ 1  2]
        #  [ 2  4]]

        # [[ 3  6]
        #  [ 4  8]
        #  [ 5 10]]

        # [[ 6 12]
        #  [ 7 14]
        #  [ 8 16]]]

    # Column stacking  (For stacking one dimension arrays.)
    x = np.arange(3); print(x)  # [0 1 2]
    y = 2*x; print(y)           # [0 2 4]
    z = 3*x; print(z)           # [0 3 6]
    
    print(np.column_stack((x, y, z)))
        # [[0 0 0]
        # [1 2 3]
        # [2 4 6]]
    
    # Row stacking
    print(np.row_stack((x, y, z)))
        # [[0 1 2]
        # [0 2 4]
        # [0 3 6]]
##stacking()

def splitting():
    a = np.arange(9).reshape(3,3);
    print(a)                    # [[0 1 2]
                                # [3 4 5]
                                # [6 7 8]]
    # Horizontal splitting    
    a1, a2, a3 = np.hsplit(a, 3)
    print(a1)   # [[0]
                #  [3]
                #  [6]]
    
    print(a2)   # [[1]
                #  [4]
                #  [7]]

    print(a3)   # [[2]
                #  [5]
                #  [8]]

    # Vertical splitting
    a1, a2, a3 = np.vsplit(a, 3)
    print(a1, a2, a3) # [[0 1 2]] [[3 4 5]] [[6 7 8]]


    x = np.arange(27).reshape(3, 3, 3)
    print(x)    # [[[ 0  1  2]
                #  [ 3  4  5]
                #  [ 6  7  8]]

                # [[ 9 10 11]
                #  [12 13 14]
                #  [15 16 17]]

                # [[18 19 20]
                #  [21 22 23]
                #  [24 25 26]]]
    
    # Depth-wise splitting
    x1, x2, x3 = np.dsplit(x, 3)
    print(x1)   # [[[ 0]
                #   [ 3]
                #   [ 6]]

                #  [[ 9]
                #   [12]
                #   [15]]

                #  [[18]
                #   [21]
                #   [24]]]

    # print(x2); print(x3) 
# splitting()

##-----------------------------------------------------

# Matrix:           mat(<value>)
def matrix_test():
    # Create from array.
    m = np.mat(np.arange(9))
    print(m)
            # [[0 1 2 3 4 5 6 7 8]]
    print(m.reshape(3, 3))
            # [[0 1 2]
            #  [3 4 5]
            #  [6 7 8]]

    # Create from tuple of ranges.
    print(np.mat((np.arange(3), np.arange(3, 6), np.arange(6, 9))))
            # [[0 1 2]
            #  [3 4 5]
            #  [6 7 8]]

    # Create from a str with ; as separator.
    print(np.mat('0, 0, 0; 1, 1, 1; 2, 2, 2'))
            # [[0 0 0]
            #  [1 1 1]
            #  [2 2 2]]

    # Identity matrix (of float)
    i = np.eye(3)
    print(i)    # [[1. 0. 0.]
                #  [0. 1. 0.]
                #  [0. 0. 1.]]

    # Save matrix as txt file.
    np.savetxt('m.txt', i)

    # Load matrix from txt file.
    j = np.loadtxt('m.txt')
    print(j)
##matrix_test()

# Array VS Matrix:
def array_matrix():
    a = np.array(range(4)).reshape(2, 2)
    print(a)             # [[0 1]
                         #  [2 3]]
    
    m = np.mat('0 1; 2 3')
    print(m)             # [[0 1]
                         #  [2 3]]
    
    # Array Multiplication
    print(a*a)      # [[0 1]
                    #  [4 9]]
    # Matrix Multiplication    
    print(m*m)      # [[ 2  3]
                    #  [ 6 11]]
    # print(m@m)    # Python 3.5 has @ for matrix multiplication.

    # m.transpost()
    # print(m.transpose())      # Alternatively
    print(m.T)      # [[0 2]
                    #  [1 3]]

    # Matrix Inverse
    print(m.I)      # [[-1.5  0.5]
                    #  [ 1.   0. ]]

    # Identity matrix
    print(m * m.I)  # [[1. 0.]
                    #  [0. 1.]]
    # Determinant:
    # e.g. M = [[0, 1], [2, 3]]   det(M) = 0*3 - 1*2 = -2
    from numpy import linalg as la
    M = np.mat('0 1; 2 3')
    print(la.det(M))        # -2.0
##array_matrix()

##-----------------------------------------------------

# Numpy Linear Algebra:  numpy.linalg
# Solving Linear Equations
# ex.      2x + 3y = 8
#          4x + 5y = 10
def solv_eq():
    m = np.mat("2 3; 4 5")
    a = np.array([8, 10])
    print(np.linalg.solve(m, a))    # [-5.  6.]
##solv_eq()

#--------------------------------------------------------

# Performance Test:
# Numpy aggreagation performs faster than Python loop operations.

import time
# time.perf_counter() returns highest precision possible system clock in nano seconds.
def sum_sq():
    n = 1000
    a = list(range(n))  # Python list
    b = np.arange(n)    # Numpy array
    
    print('For Loop:')
    start = time.perf_counter()
    s = 0
    for x in a:
        s += x*x
    stop = time.perf_counter()
    print('a: %d, %.6f' % (s, stop - start))

    start = time.perf_counter()
    s = 0
    for x in b:
        s += x*x
    stop = time.perf_counter()
    print('b: %d, %.6f' % (s, stop - start))
    
    #---------------------------------------------#
    
    print('\nComprehension:')
    # sum() is a built-in Python function.
    start = time.perf_counter()
    s = sum([x*x for x in a])
    stop = time.perf_counter()
    print('a: %d, %.6f' % (s, stop - start))

    start = time.perf_counter()
    s = sum([x*x for x in b])
    stop = time.perf_counter()
    print('b: %d, %.6f' % (s, stop - start))

    #---------------------------------------------#
    
    print('\nAggreagate:')
    start = time.perf_counter()
    s = sum(b*b)
    stop = time.perf_counter()
    print('b: %d, %.6f' % (s, stop - start))
    
    print('\nDot:')
    start = time.perf_counter()
    s = b.dot(b)
    stop = time.perf_counter()
    print('b: %d, %.6f' % (s, stop - start))
##sum_sq()   
    
import timeit
def timeit_test():
    print('%.4f' % timeit.timeit('sum([x*x for x in range(1000)])',
                        number=10000))
        
    print('%.4f' % timeit.timeit('sum(a*a)',
                        setup='import numpy as np;a=np.arange(1000)',
                        number=10000))
    print('%.4f' % timeit.timeit('a.dot(a)',
                        setup='import numpy as np;a=np.arange(1000)',
                        number=10000))
##timeit_test()

#--------------------------------------------------------------------

# Numpy Random:
def np_random():
    # Set seed to repeatedly generate random sequences.
    # np.random.seed(7)

    # Random Integer:
    # np.random.randint(low, high=None, size=None, dtype='l')
    #   returns int from uniform distribution over [low, high).
    print(np.random.randint(10))    # [0, 10)
    print(np.random.randint(1,10))  # [1, 10)

    # The default 'size' is 1. A multiple dimensions is defined by a tuple.
    print(np.random.randint(2, size=3))      # [1 0 1]
    print(np.random.randint(2, size=(2, 3))) # [[1 0 0]
                                             #  [0 1 1]]

    # Random Float:                                       
    # random.rand(d0, d1, ..., dn)
    #   return float from the uniform distribution over [0, 1).
    print(np.random.rand())     # 0.41772999795359256
    print(np.random.rand(3))
        # [0.72022296 0.23785529 0.93429886]
    print(np.random.rand(2, 3))
        # [[0.16884633 0.13424048 0.4027179 ]
        #  [0.63217362 0.79884034 0.86651362]]


    # random.randn(d0, d1, ..., dn)
    #   return float from the standard normal (Gaussian)
    #   distribution of mean 0 and variance 1
    print(np.random.randn())    # -0.0858682371549792
    print(np.random.randn(3))
        # [1.27851834 0.45183377 2.04319656]
    print(np.random.randn(2, 3))
        # [[-0.36302654 -0.46213283 -0.62346416]
        #  [ 0.34446909 -1.77580635  0.52074036]]

    # np.random.ranf(size=None)
    # np.random.random_sample(size=None)
    # np.random.random(size=None)
    #   random floats in the half-open 'continuous uniform' over [0, 1).
    # If [a, b) and b > a then (b - a) * random_sample() + a.
    print(np.random.ranf())     # 0.9397708371846202
    print(np.random.ranf(3))
        # [0.31138894 0.61913668 0.73544064]
    print(np.random.ranf((2,3)))
        # [[0.7788366  0.48567877 0.90236792]
        #  [0.19938053 0.0513662  0.6145177 ]]
    
    # Random Bytes:
    # random.bytes(length)
    print(np.random.bytes(8))   # b'\xa2\xc9\x7f\x8csVk\xf3'
##np_random()

def simpling_test():
    # random.choice(a, size=None, replace=True, p=None)
    # 'a' is a list.
    print(np.random.choice([2, 1, 5, 2, 4], 3)) # [2 1 2]
    # If 'a' is an int the list is from np.arange(a).
    print(np.random.choice(5, 4)) # [2 4 4 1]

    # Without replacement:
    print(np.random.choice(5, 4, replace=False)) # [4 3 0 1]

    # With probabilities associated with each entry in a
    print(np.random.choice(5, 3, replace=False,
                           p=[0.4, 0.0, 0.3, 0.2, 0.1])) # sum to 1.0
                        # [0 3 2]

    # random.shuffle(array)
    a = np.arange(10)
    np.random.shuffle(a)    #  inplace
    print(a)        # [6 5 8 7 1 0 3 4 2 9]

    a = np.arange(9).reshape((3, 3))
    np.random.shuffle(a)
    print(a)        # [[3 4 5]
                    #  [6 7 8]
                    #  [0 1 2]]

    # random.permutation(int|array)
    print(np.random.permutation(5))            # [0 4 3 2 1]
    print(np.random.permutation(np.arange(5))) # [2 0 1 3 4]
    print(np.random.permutation(np.arange(9).reshape((3, 3))))
                               # [[6 7 8]
                               #  [3 4 5]
                               #  [0 1 2]]
    a = np.random.permutation(np.arange(9))
    print(a.reshape((3, 3)))
                               # [[8 7 3]
                               #  [2 6 0]
                               #  [1 5 4]]
##simpling_test()
