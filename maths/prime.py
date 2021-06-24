
## Prime is a positive integer such that it is not divideable by all
##  integers less than itself except 1.

## By our definition:
##      1 is not a prime
##      2 is the first prime.

import math
## Brute Force Prime Testing:
## The values to be tested can be reduced to the square root of n plus one.
def is_prime(n):
    if n < 2:
        return False
    # for i in range(2, n):
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:      ## if n can be divided by i evenly
            return False
    return True

## Show all primes below 100.
# print([x for x in range(100) if is_prime(x)])

## Pruning is the process of reducing the number of operations.
def is_prime_prune(n):
    if  n <= 1:         ## negative numbers and 1 are not prime.
        return False
    if n <= 3:          ## 2 and 3 are prime.
        return True
    ## even numbers and mutiple of 3 are not prime.
    if (n & 1 == 0) or (n % 3 == 0):   ## & is bit-wise and operation
        return False
    i = 5           
    while i*i <= n:     
        if (n % i == 0) or (n % (i+2) == 0):
            return False
        i += 6          ## jump by 6
    return True

## Python has built-in len(<arg>) which returns the size of <arg>.
# print(len([x for x in range(100) if is_prime(x)]))
# print(len([x for x in range(100) if is_prime_prune(x)]))

## Comparing the time.
from time import perf_counter as pc
## pc() return the time at that point in nsec.
def prime_perf():
    n = 10000000000
    start = pc()        
    print(is_prime(n))
    print(pc() - start)

    start = pc()
    print(is_prime_prune(n))
    print(pc() - start)
# prime_perf()

## Exercise:
##  Write a program to show that:
##      If p is a prime and greater than 6 then p % 6 is 1 or 5.

#--------------------------------------------------------------#

## Sieve of Eratosthenes(เอราทอสเทนีส):  is good for creating a list of primes less than a numbers.
def sieve(n):
    ## create a list of boolean, filled with True except the first two.
    ## 0 and 1 are not prime 
    s = [False if i < 2 else True for i in range(n+1)]
        
    ## Iterate from 2 to half n.    
    for i in range(2, n // 2):
        if s[i]:        ## start from a prime.
            ## Jump by i to n.
            for j in range(i+i, n+1, i):   
                s[j] = False    ## Multiple of i is not a prime
    return [i for i in range(n+1) if s[i]]  ## create the list of prime from the boolean list.
# print(sieve(100))
# print([i for i in range(100) if is_prime(i)])
    
## Optimized Sieve
def opt_sieve(n):
    s = [False if i < 2 else True for i in range(n+1)]    
    h = (n+1) >> 1	## half n
    i = 2;		## start from 2 the first prime
    while i < h:
        c = i << 1	    ## double i
        while c <= n:
            s[c] = False    ## mark as not prime
            c += i	    ## jump by i
        i += 1
        while (i < h) and (not s[i]):  ## find next i that is prime
            i += 1
    return [i for i in range(n+1) if s[i]]
# print(opt_sieve(100))

#-------------------------------------------------------------#

## Prime Generator Function: are functions that generates primes.

##  31 is a prime, and 331, 3331, 33331, ... are also primes.
def p31_test():
    def gen31():       ## This is a coroutine.
        r = '1'
        while True:
            r = '3'+r
            yield int(r)
            
    x = gen31()
    for _ in range(10):
        p = next(x)
        print(p, is_prime(p))  ## But it fails miserably after seven 3s.
# p31_test()

## The impressive formula n**2 - n + 41 generates a lot of primes.
def prime_gen():
    for n in range(45):
        print(n, is_prime(n**2 - n + 41))  ## But it fails when n is 41.
# prime_gen()

## It had been shown that there is no polynomials (of any order) that generates
##   primes for all values of input n.

## Exercise:
## 1. Find the smallest n that n**2 - (79*n) + 1601 fails to be prime.

## An interesting: 6*n +/- 1 generates both primes and no-primes.
def gen_6n():
    for n in range(10):
        print(n, 6*n+1, is_prime(6*n+1), 6*n-1, is_prime(6*n-1))
# gen_6n()
##  But it has been tested that all primes (except 2 and 3) can be expressed in this form.
def is_6n(p):
    if ((p+1) % 6 == 0) or ((p-1) % 6 == 0):
       return True
    return False
def is_6n_test():
    for p in sieve(1000000):
        if not is_6n(p):
            print(p, end=',')
# is_6n_test()

## Fermat wrongfully proposed that numbers of the form 2**(2**n) + 1 are primes.
## It is true for n up to 4 but Euler show that it is not true when n = 5.
def fermat():
    for n in range(10):
        p = 2**(2**n) + 1
        print(n, p, is_prime(p))
# fermat()

#-------------------------------------------------------------------#

## Mersenne Prime:
## For an integer n > 0, Mersenne number of n, denoted m(n) is 2**n - 1.
def m(n):
    return 2**n - 1
# print(m(10))

## It was known for a long time that:
## If p is a prime then m(p) is likely to be primes but not all.
##                 else m(p) is not a prime.

## The Greeks knew that m(2), m(3), m(5) and m(7) are primes and m(11) is not a prime.
## And in the middle age, m(13), m(17) and m(19) were known to be primes.
def mp_test():
    for i in range(20):
        mi = m(i)
        if is_prime(i) and is_prime(mi):
            print('m(%d) = %d' %(i, mi))
# mp_test()

## In 1644, Marin Mersenne claimed that m(2), m(3), m(5), m(7), m(13), m(17), m(19),
##  and his owned found: m(31), m(67), m(127), and m(257) are primes.
## That was a big surprise since no one can compute such large numbers at that time.

## Euler proved that m(31) is indeed a prime.
# print(is_prime(m(31)))

## In 1883, Pervusin shown that m(61) which is not in the Mersenne's list is a prime.
# print(is_prime_prune(m(61)))      ## This would take a long long time. 

## In 1903, Frank Nelson Cole gave a silent presentation at the American Mathematical
##  Meeting by calculating 
##	2**67 - 1 = 193,707,721 x 761,838,257,287
# print(is_prime_prune(m(67)))      ## Don'y try this at home.

## Edouard Lucas developed a method to prove that m(127) is actually a prime.
## In 1911, Ralph Ernest Powers showed that m(89) is a prime.
## In 1914 Powers and Fauquembergue added m(107) to the list.
## m(257) is a prime but its factor is unknown.
## In 2001, with a super computer m(13,466,917) is showed to be a prime.


