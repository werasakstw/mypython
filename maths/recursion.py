
# Iterations:
def iteration():
    for i in range(10):
        print(i, end=',')
# iteration()

## Head Recursion
def head(n):
    print(n, end = ',')
    if n < 10:
        head(n+1)
# head(1)

## Tail Recursion
def tail(n):
    if n < 10:   
        tail(n+1)
    print(n, end = ",")
# tail(1)

## Iterations do not create new environment in each loop.
def iter_test():
    x = 0
    for i in range(10):
        x += 1
        print(x, end=',')
# iter_test()

## Recursions create new environment in each invocation.
def recur_test(n):
    l = 0
    if n < 10:
        l += 1
        print(l, end=',')
        recur_test(n+1)
# recur_test(1)

#####################################################################

## Factorial:
## The iterative definition:
##      n! =  n * (n-1) * (n-2) * ... * 1
def facI(n):
    r = 1;
    for i in range(1, n+1):
        r *= i
    return r

## The Recursive definition: 
##      n! =  1             if n <= 1
##         = n * (n-1)!     otherwise
def facR(n):
    if n <= 1:
        return 1
    return n * facR(n-1)

def fac_test():
    for i in range(1, 10):
        print(i, facI(i), facR(i))
# fac_test()

## Exercises:
##  Find abc a three digits interger, such that
##          abc = a! + b! + c!

#####################################################################

## Fibonacci:
##      fib(n)  = 1			if  n <= 1
##              = fib(n-1) + fib(n-2)	otherwise
def fibI(n):
    a = b = c = 1
    for i in range(2, n+1):
        c = a + b
        a, b = b, c
    return c

def fibR(n):
    if n <= 1:
        return 1
    return fibR(n-1) + fibR(n-2)

def fib_test():
    for i in range(1, 10):
        print(i, fibI(i), fibR(i))
# fib_test()

#####################################################################

## Exponential:
## The iterative definition:
##           expo(a, n) =  a * a * ... * a   (n times)
def expoI(a, n):
    r = 1
    for i in range(n):
        r *= a
    return r

## The Recursive definition:
##          expo(a, n) =  1	            if n == 0
##                     =  a * expo(a, n-1)  otherwise
def expoR(a, n):
    if n == 0:
        return 1
    return a * expoR(a, n-1)

## The Divide and Conquer Exponential:
##       expo(a, n) = 1                      if n == 0
##                  = expo(a*a, n//2)        if n is even
##                  = a * expo(a*a, n//2)    if n is odd
def expoD(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return expoD(a*a, n//2)
    return a*expoD(a*a, n//2)

## Why?
def expoF(a, n):
    r = 1;
    while n > 0:
        if n % 2 == 1:    ## n is even
            r *= a
        a *= a
        n >>= 1	            ## n /= 2;
    return r

def expo_test():
    n = 7
    for a in range(2, 10):
        print('%d, %d:   %d, %d, %d, %d' % (a, n, expoI(a,n), expoR(a,n), expoD(a,n), expoF(a,n)))
# expo_test()


## Exercises:
##  1. Find abcs a four digits interger, such that
##          abcd   =  a**a + b**b + c**c + d**d

##  2. It was believe that there is no even number n that divides 2**n + 2 evenly
##  In 1949, Mr.Lehmer found that there are many such n. Let find the smallest one.

#####################################################################

## Greatest Common Divisor
## Definition:
##      gcd(m,n) = x iff x is the maximun value that divides m and n evenly. 
##   ex.   gcd(162, 234) = 18       162 % 18 == 0  and  234 % 18 == 0

##  A Simple Gcd:
def gcdI(m, n):
    g = m if m < n else n
    while g != 1 and not((m % g == 0) and (n % g == 0)):
        g -= 1
    return g

## Euclid Gcd:
def gcdE(m, n):
    while True:
        r = m % n
        if r == 0:
            break
        m, n = n, r
    return n

## Recursive Euclid Gcd:
def gcdR(m, n):
    if n == 0:
        return m
    return gcdR(n, m % n)

def gcd_test():
    y = 12
    for x in range(11, 100, 7):
        print('%d, %d:   %d, %d, %d' % (x, y, gcdI(x, y), gcdE(x, y), gcdR(x, y)))
# gcd_test()       

#####################################################################

## Homework:
##  What does the following functions compute and explain how it can be done.
def puzzle3(m, n):
    if n == 0:
        return m
    return puzzle3(n, m - n*(m // n))


