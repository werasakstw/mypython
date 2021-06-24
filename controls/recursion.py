
# A recursive function is function that calls itself.
# Recursive Function may be head or tail.
def count(n):
    # print(n, end = ',')       # Head Recursion
    if n < 10:
        count(n+1)
    print(n, end = ',')     # Tail Recursion
##count(1)

# The result may be passed down or up the recursion.
# Summation is not order-oriented.
def sum_down(min, max, sum):
    if min < max:
        return sum_down(min+1, max, min+sum) # Head
    return sum
# print(sum_down(1, 10, 0))

def sum_up(min, max, result):
    if min < max:
        return min + sum_up(min+1, max, result) # Tail
    return result
# print(sum_up(1, 10, 0))

# List appending is order-oriented.
# Head recursion needs to pass the result down.
def to_list(min, max, r):
    if min < max:
        r.append(min)
        return to_list(min+1, max, r)
    return r
##print(to_list(1, 10, []))

# The environment stack may hold states in each invocations.
# Tail recursion pass the result up.
def rev_list(min, max):
    if min < max:
        r = rev_list(min+1, max)
        r.append(min)
        return r
    return []
##print(rev_list(1, 10))

#----------------------------------------------------------------

# Iterations do not create new environment in each loop.
def iter_env():
    c = 0
    for i in range(10):
        c += 1
        print(c, end=',')
##iter_env()

# Recursions create new environment in each invocation.
def recur_env(n):
    c = 0
    if n < 10:
        c += 1
        print(c, end=',')
        recur_env(n+1)
##recur_env(1)

#-----------------------------------------------------

'''
The benefit of recurions is a lot of mathematic functions and
  algorithms can be defined by calling its self. So they are
  easier to present as programs.
'''
# Iterative Factorial: 
#      n! = fac(n) = n * (n-1) * (n-2) .... * 1
def facI(n):
    r = 1;
    for i in range(1, n+1):
        r *= i
    return r
# print(facI(5))            # 120

# Recursive Factorial: 
#      n! = fac(n) = 1              if n <= 1
#                  = n * fac(n-1)   otherwise
def facR(n):
    if n <= 1:
        return 1
    return n * facR(n-1)
##print(facR(5))            # 120

# Exercises: What does the following function computes?
def p1(m, n):   # m > 0
    if m == 0:
        return 0
    return m + n - 1 + p1(m-1, n-1)

#--------------------------------------------------------

# Exponential:
#	a**n = exp(a, n) = a * a * ......   n times
# Iterative Exponential
def expI(a, n):
    r = 1
    for i in range(n):
        r *= a
    return r
# print(expI(2, 10))

# Recursive Exponential
def expR(a, n):
    if n == 0:
        return 1
    return expR(a, n-1) * a
# print(expR(2, 10))

# Divide and Conquer Exponential:
def expD(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return expD(a*a, n//2) 	# n is even
    return expD(a*a, n//2) * a	# n is odd
# print(expD(2, 10))

#--------------------------------------------------------------

# Fibonacci:
#      fib(n)  =   1			if  n = 1, 2
#              =  fib(n-1) + fib(n-2)	otherwise

# Suppose a newborn rabbit pair will give birth a new pair on the 
#     second month then a new pair every months and so on.
# Given a pair of newborn rabbit on a New Year day,
#     there will be how many pairs at the end of the year?

# Iterative Fibonacci:
def fibI(n):
    a, b, c, i = 1, 1, 1, 3
    while i <= n: 
        c = a + b
        a = b  # Remember the last two values.
        b = c
        i += 1
    return c;

# Recursive Fibonacci:
def fibR(n):
    if n <= 2:
        return 1
    return fibR(n-1) + fibR(n-2)

# Fibonacci with Memoization:
# Python functions are objects with its own namespace.
# A function may have its state.
def fibM(n):
    fibM.f = [0, 1, 1]
    if n > len(fibM.f)-1:
        for i in range(len(fibM.f), n+1):
            fibM.f.append(fibM.f[i-1] + fibM.f[i-2])
    return fibM.f[n]

# @lru_cache, Python’s built-in moization/caching.
from functools import lru_cache
@lru_cache( )
def fibC(n):
    if n <= 1:
        return n
    return fibC(n-1) + fibC(n-2)

##print([fibI(i) for i in range(15)])
##print([fibR(i) for i in range(15)])
##print([fibM(i) for i in range(15)])
##print([fibC(i) for i in range(15)])

# Performance Test:
# Recursive Fibonacci performs a lot of repeated tasks.
from time import perf_counter as pc
def fib_perf():
    start = pc()
    r = fibI(36)
    print('%d : %1.6f' % (r, pc() - start))

    start = pc()
    r = fibR(36)
    print('%d : %1.6f' % (r, pc() - start))

    start = pc()
    r = fibM(36)
    print('%d : %1.6f' % (r, pc() - start))

    start = pc()
    r = fibC(36)
    print('%d : %1.6f' % (r, pc() - start))
##fib_perf()

''' Try: Write programs to check for all numbers less than 1,000,000.
 1. There is no Fibonacci numbers that is a product of two others Fibonacci numbers.
 2. There can be no more than two Fibonacci numbers bewteen n and 2n.
 3. If m is divideable by n then fib(m) is divideable by fib(n).
'''

#-------------------------------------------------------

# Exponent Modulo: allows exponent to a big number in the range of m.
#	expM(a, n, m) = (a ** n) % m
# A recursive method can be presented as iterative.
def expM(a, n, m):
    r = 1
    while n > 0:
        if (n & 1) == 1:
            r = (r * a) % m
        a = (a * a) % m
        n >>= 1
    return r
##print(expM(123, 12345, 13), (123**12345) % 13)

# Encryption:
# Given e is an encoder, d is a decoder (for mod m)
#        y = expM(x, e, m)
#        x = expM(y, d, m)
# e.g. e = 23, d = 167, and m = 221
def encrypt():
    secret = 123   # The secret value must less than m.
    encoded = expM(secret, 23, 221)
    print(encoded)
    print(expM(encoded, 167, 221))
#$encrypt()

#--------------------------------------------------------------

# Greatest Common Divisor:
#  gcd(m, n) is the largest integer that divides both m and n evenly.
def gcd(m, n):
    g = m if m < n else n   # g is the larger between m and n.
    while g > 1 and not((m % g == 0) and (n % g == 0)):
        g -= 1
    return g

# Euclid Recursive Gcd:
def gcdER(m, n):
    if m == 0:
        return n
    if n == 0:
        return m
    return gcdER(n, m % n)

# Euclid Iterative Gcd:
def gcdEI(m, n):
    while True:
        r = m % n
        if r == 0:
            break
        m, n = n, r
    return n

# Try: What does the follwing functions compute?
def p2(m, n):
    if n == 0:
        return m
    return p2(n, m - n*(m // n))

#-------------------------------------------------------------------

# Problem Reduction: Partition the problem into sub-problems
#   then recurively solve each sub-problems.

# Towers of Hanoi:
# To move n discs from source to target using tmp for temporary.
def toh(n, src = 'A', target = 'B', tmp = 'C'):
    if n == 1:
        print('Move from %s to %s' % (src, target))
    else:
        toh(n-1, src, tmp, target)
        print('Move from %s to %s' % (src, target))
        toh(n-1, tmp, target, src)
# toh(3)

#--------------------------------------------------------------

# Divide and Conquer: Partition the problem and then solve separately.
# Solving smaller problems cost less than bigger problem with the same size.

# Binary Search:
# To search an element in a sorted list.
def bsearchI(x, a):
    while a:
        mid = len(a) // 2
        if a[mid] == x:
            return True
        elif a[mid] > x:
            a = a[:mid]
        elif a[mid] < x:
            a = a[mid + 1:]
    return False

def bsearchR(x, a):
    if a:
        mid = len(a) // 2
        if a[mid] == x:
            return True
        elif a[mid] > x:
            return bsearchR(x, a[:mid])
        else:
            return bsearchR(x, a[mid + 1:])
    else:
        return -1
    
def bsearch_test():
    import random
    a = [ random.randrange(1, 100) for _ in range(10) ]
    a.sort()
    print(a)
    for i in a:
        print(i, bsearchI(i, a), bsearchR(i, a))
##bsearch_test()
