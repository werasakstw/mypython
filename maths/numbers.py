
## Fraction:
## Python provides 'fractions' package for mainpulating fractions.
from fractions import Fraction

def fraction_test():
    x = Fraction(1, 2)
    y = Fraction(0.25)
    print(x)        ## 1/2
    print(y)        ## 1/4
   
    ## Mathematic operations
    print(x + y, x - y, x * y, x / y)

    ## Comparision operations
    print(x < y, x <= y, x > y, x >= y, x == y)

    ## Fraction Simplification
    def simplify(f): 
        a, b = f.as_integer_ratio()
        return '%d+(%d/%d)' % (a/b, a%b, b)
        
    print(simplify(Fraction(3, 2)))         ## 1+(1/2)

    ## Area of a rectangle with 1+(1/5) width and 2+(3/4) height.
    area = 1+Fraction(1, 5) * 2+Fraction(3, 4)                     
    print(area, simplify(area))             ## 43/20 2+(3/20)

    ## Volume of a cube of 1+(2/3) on each sides.
    volume = (1 + Fraction(2, 3)) ** 3
    print(simplify(volume))                 ## 4+(17/27)
# fraction_test()

##----------------------------------------------------------------##

## Decimal:
## 'decimal' module to perform floating point operations of arbitrary precision.

from decimal import Decimal
from decimal import getcontext

def dec_test():
    print(1/3)
    print(Decimal(1) / Decimal(3))
    
    print(getcontext().prec)    ## default precision

    ## set precision to 100 positions
    getcontext().prec = 100  
    print(Decimal(1) / Decimal(3))
##dec_test()

## David Bailey, Peter Borwein and Simon Plouffe proposed a formula for pi,
##      pi = sum(n=0,inf)( 4/(8*n+1) - 2/(8*n+4) - 1/(8*n+5) - 1/(8*n+6) ) / 16**n
## Increasing n would increase the precision.

## Python float values are 8 bytes, the precision is approximately 15 position.
def dps_pi(n):
    s = 0.0
    for i in range(n):      
        i8 = 8*i
        s += (4.0/(i8+1) - 2.0/(i8+4) - 1.0/(i8+5) - 1.0/(i8+6)) / 16**i
    return s
# print(dps_pi(10)); print(math.pi)

## 1000 decimal points Pi:
def dps_1000pi():
    getcontext().prec = 1000
    d4 = Decimal(4.0)
    d2 = Decimal(2.0)
    d1 = Decimal(1.0)
    s = Decimal(0.0)
    for i in range(1000):
        i8 = Decimal(8*i)
        s += (d4/(i8+1) - d2/(i8 +4) - d1/(i8+5) - d1/(i8+6)) / 16**i 
    return s
# print(dps_1000pi())

##----------------------------------------------------------------##

## Complex Number:
## A Complex Number has two parts,
##      - the real part is a number (may be integer or float).
##      - the imaginary part is a number multiplies with sqrt(-1).
## Python represents the sqrt(-1) with j.
def complex_test():
    m = 1 + 2j              ## 1 + 2*sqrt(-1)
    n = complex(3, 4)       ## 3 + 4*sqrt(-1)

    print(m, m.real, m.imag)
    print(n, n.real, n.imag)
    
    ## Operations on complex numbers.
    print(m+n, m-n, m*n, m/n, m**2)

    ## Built-in functions.
    print(abs(n), pow(m, 3))

    ## Standard library
    import cmath
    print(cmath.sqrt(m))
    print(cmath.sin(m))
    print(cmath.log10(m))
# complex_test()





