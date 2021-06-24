# pip install sympy

from sympy import Symbol
x = Symbol('x')
# print(x*x + 1)        # x**2 + 1

# Define many symbols in one line.
from sympy import symbols
w, y, z = symbols('w,y,z')

''' SymPy simplifies only the most basic of expressions and
leaves it to the users to explicitly simplify as needed.
'''
from sympy import expand, symbols, simplify, factor, together, apart

# expand() expands as a sum of individual terms.
def expand_ex():
    e = (x+y)**3      # Try: (x-y)*(x+y)
    print(e.expand())       # x**3 + 3*x**2*y + 3*x*y**2 + y**3
##expand_ex()

# simplify() simplifies to the lowest number of terms.
def simplify_ex():
    e = (x ** 3 + x ** 2 - x - 1)/(x ** 2 + 2 * x + 1)
    print(e.simplify())     # x - 1
##simplify_ex() 

# factor() decomposes to its factors.
def factor_ex():
    print((x**2 - y**2).factor())   # (x - y)*(x + y)
##factor_ex()

# together() combines into a ratio.
# apart() decomposes to a sum of individual terms, handle one symbol only.
def together_apart():
    print(together(1 + 1/x))        # (x + 1)/x
    print(apart((x + 1)/x))         # 1 + 1/x 
##together_apart()

from sympy import pprint
def pprint_test():
    pprint(3*x**2 + 2*x*y + y**2)
    # pprint((x ** 3 + x ** 2 - x - 1)/(x ** 2 + 2 * x + 1))
##pprint_test()

''' Exerices:
1. Expend the following:
  x*(x+1)
  (x+1)*(x+2)
  (x+y)*(x-y)
  (x+y)**2
  (x+y)**(x+y)
  (x**2 + x*2 + x + 1)*(x**3 + x*3 + x + 2)
'''
##print(expand(  ))

'''
2. Factor the following:
  x**2 + x
  x**2 + 2*x + 1
  x**2 + 2*x*y + y**2
  x**2 - y**2
'''
##print(factor( ))

# Integration:
from sympy import integrate
def integrate_ex():
    print(integrate(x**3 + 2*x**2 + x, x)) # x**4/4 + 2*x**3/3 + x**2/2
    print(integrate(x/(x**2 + 2*x), x))    # log(x + 2)
##integrate_ex()

# Substitution:
def subs_test():
    print((2*x**2 + x + 1).subs({x:1}))             # 4
    print((x**2 - 2*x*y + y**2).subs({x:1, y:2}))   # 1

    # approximate an value into a float no more than 3 positions.
    print((x**2).subs({x:1.13}).evalf(3))           # 1.28
##subs_test()

# Trigonometry:
from sympy import sin, cos
import math
def tri_test():
    print(simplify( sin(x)**2 + cos(x)**2 ))        # 1
##tri_test()

## Solving Equations:
from sympy import solve
def solv_ex():
    # Transform equation to expression that equal to zero.
    #  2*x + 1 = 7    --->   2*x + 1 - 7
    print(solve( 2*x + 1 - 7 ))
    
    # Polynomials:
    print(solve( x**2 + 2*x - 3 ))  # [1]
    print(solve( x**2 + 1 ))        # [-I, I]     I is sqrt(-1)
    print(solve( x**3 - x ))        # [-1, 0, 1]

    # Two variables equation:  The solution is returned as a dict.
    print(solve([x + y - 4, 2*x - y + 1],[x, y])) # {x: 1, y: 3} 
    
    # the solution may be in term of others veriable.
    print(solve( x**2 - 2*y + z, x ))       # [-sqrt(2*y - z), sqrt(2*y - z)]
    print(solve( 2*x + y - 1, dict=True ))  # [{x: 1/2 - y/2}]
##solv_ex()

# Solving Linear Equations: n variables and n equations.
def linear_eq(): 
    exp1 = x + 3*y + z + 1
    exp2 = 3*x + y - z - 1
    exp3 = x + y + 3*z + 1
    print(solve( (exp1, exp2, exp3) )) # {x: 1/3, y: -1/3, z: -1/3}
##linear_eq()

''' Motion with constant acceleration:
       s = u*t + (1/2)*a*t*t
       s = u*t + (1/2)*a*t*t
where a is acceleration
   u is initial velocity
   t is time
   s is distance.
'''
def mot_acc():
    s, u, t, a = symbols('s, u, t, a')
    pprint(solve( u*t + (1/2)*a*t*t - s, t, dict=True))
##mot_acc()

## Quadratic equation:
##          a*x**2 + b*x + c
def parabola():
    a, b, c = symbols('a, b, c')
    pprint(solve( a*x**2 + b*x + c, x ))
##parabola()


