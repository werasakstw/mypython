

# The Babylonian knew that Pi is about 3(1/8).
##print(3+(1/8))                # 3.125

# The Egyptian Pi is (16/9)**2.
##print((16/9)**2)              # 3.1604938271604937

# Archimedes found that Pi is about 211875/67441.
##print(211875/67441)           # 3.1416349105143757

# But he believed, no one needs a Pi that's good more than two decimal point digits.
# So 22/7 would be enough for the next two thousand years.
##print(22/7)                   # 3.142857142857143

# The Python 'math' module has a Pi value that is accurate up to 15 positions.
import math
##print(math.pi)                        # 3.141592653589793

# Ramanujan's Pi 
##print(math.sqrt(2) * 9801 / 4412)     # 3.141592730013306

# Someone Pi:
##print(2**(9217/5581))                 # 3.1415926931597395

''' Exercises:
The diameter of the earth is 12,742 km.
What the different of the earth circumferences, computing with
    pi = 22/7 and 3.141592563589793 (15 positions). 
'''
#-------------------------------------------------------------------

# The best Pi approximation using a two digits fraction.
def pi_app():
    x, y, c = 0, 0, 1
    for a in range(1, 100):
        for b in range(1, 100):
            d = a/b - math.pi       # compare with Python's Pi
            d = d if d > 0 else -d
            if d < c:
                x, y, c = a, b, d
    print("%d / %d" % (x , y))
##pi_app()
# Try: Find the best Pi approximation using a three digits fraction.

'''
A chinese guy, Tsu-ching Chih(480 AD) found 355/113 which is the best Pi up until the 15th century.

Biblical value of pi:
      https://www.purplemath.com/modules/bibleval.htm

Ludolph van Ceulen:
      https://en.wikipedia.org/wiki/Ludolph_van_Ceulen

Indiana Pi Bill, Edwin J. Goodwin:
      https://en.wikipedia.org/wiki/Indiana_Pi_Bill

Francois Viete(1592) proposed an infinite series for Pi value.
      https://en.wikipedia.org/wiki/Vi%C3%A8te%27s_formula
 Pi = 2 * (2/sqrt(2)) * (2/sqrt(2+sqrt(2))) * (2/sqrt(2+sqrt(2+sqrt(2)))) * ...

John Wallis(1616):
      https://en.wikipedia.org/wiki/Wallis_product
  Pi/2 = (2*2)/(1*3) * (4*4)/(3*5) * (6*6)/(5*7) * ....

Leibniz(1646):
      https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80
  pi = 4(1 - 1/3 + 1/5 - 1/7 ....)
'''
def leibniz(n):
    s = 0
    for i in range(1, n+1):
        t = 1 / (2*i - 1)
        if i % 2 == 0:
            s += -t
        else:
            s += t
    return 4*s
# print(leibniz(1000))

# Euler(1707):  pi**2 = 6(1 + 1/2**2 + 1/3**2 + 1/4**2 +...)
def euler(n):
    s = 0
    for i in range(1, n+1):
        s += 1/(i*i)
    return math.sqrt(6*s)
##print(euler(1000)); print(math.pi)

#-------------------------------------------------------------#

# Quick Pi 
def quick_pi(n):
    a = 1
    b = 1 / math.sqrt(2)
    c = 1 / 4
    x = 1
    for i in range(n):
        y = a
        a = (a + b) / 2
        b = math.sqrt(b*y)
        c -= x * ((a-y) ** 2)
        x *= 2
    return ((a+b)**2) / (4*c)
##print(quick_pi(3)); print(math.pi)

# David Bailey, Peter Borwein and Simon Plouffe:
#    Pi = sum(n=0,inf)( 4/(8*n+1) - 2/(8*n+4) - 1/(8*n+5) - 1/(8*n+6) ) / 16**n
# Python represents a float value using 8 bytes so the decimal points is valid up to approximately the 15 position.
def dps(n):
    s = 0.0
    for i in range(n):      # increasing n would increase the precision.
        i8 = 8*i
        s += (4.0/(i8+1) - 2.0/(i8 +4) - 1.0/(i8+5) - 1.0/(i8+6)) / 16**i
    return s
##print(dps(10)); print(math.pi)

# Python provides the 'decimal' module to perform operations on decimal of arbitrary precision.
from decimal import Decimal, getcontext 
def dps_decimal(n):
    getcontext().prec = 1000
    s = decimal.Decimal(0.0)
    for i in range(n):
        i8 = Decimal(8*i)
        s += (Decimal(4.0)/(i8+1) - \
              Decimal(2.0)/(i8+4) - \
              Decimal(1.0)/(i8+5) - \
              Decimal(1.0)/(i8+6)) / 16**i 
    return s
##print(dps_decimal(825))




