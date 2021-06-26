''' Collatz's Conjecture: Given any positive integer n:
              while n > 1
                  if n is odd
                      n = 3n + 1
                  else
                      n = n/2
The loop always terminate.
'''
def collatz_test():
    def collatz(n):
        while n > 1:
            if n % 2 == 1:
                n = 3*n + 1
            else:
                n //= 2
        return True

    for i in range(1, 1000):
        if collatz(i):
            print(i, end=",")
##collatz_test()
''' It had been tested that collatz loop terminates for all integers up to 1000 digits.
There is no proof that it would terminate for all integers so it is a conjecture.
It looks like increaing n would increae the maximum iterations.
There is no proof that the maximum iterations would be bound by a number.

Exercise: Find the maximum iterations for n = 1,000.
'''
#-------------------------------------------------------------------

''' Nine Loop: Given a two digits positive integer n = ab, where
      'a' is the tenth digit and 'b' be the unit digit. 
          1. Compute   n = n - (a+b)
          2. Repeat step 1 until n is 9.
It had been verified that the loop terminates fot all two digits numbers(10 -> 99).
'''  
def nine_loop_test():
    def nine_loop(n):
        while n != 9:
            a, b = n // 10, n % 10
            n -= (a + b)
        return True

    for i in range(10, 100):
        if nine_loop(i):
            print(i, end=",")
##nine_loop_test()

#----------------------------------------------------------------------

''' Let define sum_sq(n) is the sumation of the sqaure of each digits in n.
    e.x.   sum_sq(123) = 1**2 + 2**2 + 3**2  = 14     '''
def sum_sq(n):
    s = 0
    while n > 0:
        d = n % 10
        s += d*d
        n //= 10
    return s
##print(sum_sq(123))    # 14

''' Square Loop: Given an integer n > 1:
      1. Compute n = sum_sq(n)
      2. Repeat step 1 until the result is 1 or 4.
It had been verified that the loop terminates fot all n up to 100 digits.
'''
def sq_loop_test():
    def sq_loop(n):
        while n == 1 and n == 4:
            n = sum_sq(n)
        return True

    for i in range(1, 100):
        if sq_loop(i):
            print(i, end=",")
##sq_loop_test()

# Exercise: Find the maximum iterations of n belows 1000.

#----------------------------------------------------------------------

''' Digit Multiplication': dmul(n) is the result of multipling all digits
in 'n' a positive integer.
             dmul(abc...n) = a * b * c * ... * n          '''
def dmul(n):
    m = 1
    while n > 0:
        m *= n % 10
        n //= 10
    return m
##print(dmul(12345))          # 120

''' Multiplicative Persistence: mp(n) is the number of steps that apply
dmul(n) repeatedly until the result is one digit, where n is a positive integer.
We do not know whether mp(n) terminates for all n.
It had been tested up to 10**50 digits numbers and never found an mp greeter than 11.
'''
def mp_test():
    def mp(n):
        step = 0
        while n > 9:
            n = dmul(n)
            step += 1
        return step
    for n in range(1, 100):
        print(mp(n), end=',')
##mp_test()

''' Exercises:  Most of n below 1000 have mp less than 5.
Find the smallest n below 100_000 that has the max mp.
'''












