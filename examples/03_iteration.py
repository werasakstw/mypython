
# Computers never tired of repetitions.
                 
# Try multiplying a specific number with 1 to 9. 
def mul(n):
    for i in range(1, 10):             #   block, range()  (iteration.py)
        print('%6d' % (n * i))
##mul(1099)
# Try: 89, 99, 108, 109, 898, 899, 1089, 1099, 10889, 10899, 108899 

# Mutiply 37 with numbers that are multiple of 3 below 100.
def mul_of3():
    for i in range(3, 100, 3):
        print('37 x %2d = %10d' % (i, 37 * i)) 
##mul_of3()
# Exercises: Multiple 142857 with numbers that are multiple of 7 below 100.

# Ask your friend what is the favarite number from 0 to 9.
# Suppose the answer is n.  Then compute 12345679*n*9
def favarite_number():
    def test(n):
        print('%d  %10d' % (n, 12345679 * 9 * n))

    for n in range(0, 10):      # n is 0 to 9.
        test(n)
##favarite_number()

#--------------------------------------------------------

# Built-in Function:
# Python has a built-in function sum(<seq>).
##print(sum([2, 1, 3]))       # 6
##print(sum(range(10)))       # 45

''' Let define: Summation from 1 to n.
        sum_(n) = 1 + 2 + 3 + ... + n  =  n*(n+1)/2
'''
def sum_(n):
    s = 0
    for i in range(1, n+1):
        s += i
    return s
##print(sum_(9))              # 45

# Test sum_() for a list of numbers.    iterate list (iteration.py)
def sum_test():
    for n in [100, 1_000, 1_000_000]:
        print(sum_(n) == n*(n+1)/2)
##sum_test()
        
''' Exercises:
1. Given sum_pow3(n) = 1**3 + 2**3 + 3**3 + ... + n**3  or n > 0 
    Write a program to show that sum_pow3(n) is equal to sum(n)**2
    for all 0 < n < 100.
        Ex.   1**3                        =  1**2
              1**3 + 2**3                 =  3**2
              1**3 + 2**3 + 3**3          =  6**2
              1**3 + 2**3 + 3**3 + 4**3   =  10**2
2. Write a program to show that:
    The sum of n+1 consecutive numbers is equal to
        the sum of the next n consecutive numbers for all n > 0.
      Ex.    1 + 2                   = 3
             4 + 5 + 6               = 7 + 8  = 15 
             9 + 10 + 11 + 12        = 13 + 14 + 15
             16 + 17 + 18 + 19 + 20  = 21 + 22 + 23 + 24
             ....
'''
#-----------------------------------------------------------

''' Approximation:
There are mathematic formulas that if we compute more terms,
the result is more accurate.

A program cannot compute to the infinity term, but can compute
a lot of terms and we notice the trend.
Let show that   1/2 + 1/4 + 1/8 + 1/16 + ..... = 1
'''
def convolution():
    def _sum(n):
        s = 0
        for x in range(1, n):
            s += 1 / (2**x)
        return s

    for n in [5, 10, 30, 50]:
        print('%2d: %.15f' % (n, _sum(n)))
##convolution()

'''
The Newton's Square Root method is
          sqrt(n) ~ (n/g + g)/2
    where g is a good guess. If the result is not good enough, 
it can be used as g in the next iteration.

Ex. Suppose n is 10.
1. The most likely solution g is halve of n.
                g = 10/2 = 5
2. Compute next g = (10/5 + 5)/2 = 3.5
3. g is not good enough then repeat
                g = (10/3.5 + 3.5)/2  =  3.178571428571429
                .....
4. Stop when satisfied.
'''
def newton_sqrt(n):
    g = n / 2
    for _ in range(4):     # Let try for 4 rounds. 
        g = (n/g + g)/2; 
    return g

def newton_sqrt_test():
    for n in [2, 4, 9, 10, 16, 25]:
        print('%d:\t%.3f' % (n, newton_sqrt(n)))
##newton_sqrt_test()
        
''' Exercises:
1. Compare the Newton square root with Python's math.sqrt() for n < 100.
2. For n up to 1000, how many rounds the newton_sqrt() have to perform
to get results that good to the fourth decimal position.
'''

#-----------------------------------------------------------------

''' Non-deterministic Loop: A loop that we cannot determine how many
round to iterate in advance.

Let define dsum(n) is the sum of all digits in n, where n > 0.
Suppose n is an integer abc...n then dsum(n) = a + b + c + ... + n.
'''
def dsum(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s
##print(dsum(1234567890))     # 45
      
## Recursive Digit Sum:
def dsumR(n):                                      # (recursion.py)
    if n < 10:
        return n
    return (n % 10) + dsumR(n // 10)
##print(dsumR(1234567890))    # 45

#-----------------------------------------------------------------------

''' Digital Root: of a number is computed by applying dsum() repeatedly
until the result is one digit.
'''
def droot(n):
    while True:         # Infinite Loop
        n = dsum(n)
        if n < 10:      # Terminate Condition
            return n
##print(droot(1234567890))    # 9

# All numbers that are multiple of 9 have digital root equal to 9.
# We can programmatically check the theorem up to a certain number.
def droot_test():
    # Check all multiple of 9 up to 1_000_000.
    for n in range(9, 1_000_000, 9):
        if droot(n) != 9:
            print(n)
##droot_test()                  # Try: replacing 9 with 3.

''' Exercises: Let a, b, and c are consecutive positive integers,
if c is divideable by 3 then the digital root of a+b+c is 6.
  Write program to verify all numbers less than 1_000_000.
''' 
#-----------------------------------------------------------------------

''' Integer Reversal: is the reversed sequence of all digits of the number.
        e.g    rev(123) = 321       '''
def rev(n):
    x, m = 0, n
    while m > 0:
        x *= 10
        x += m % 10
        m //= 10
    return x
##print(rev(123))     # 321

''' Palindrom: A positive interger n is a palindrom if n == rev(n).
Excluded single digit numbers and numbers that contain only one digit.
       e.g. 11, 111, 222....
'''
def is_one_digit(n):
    d = set()    # Sets do not allow duplicate members.     (sets.py)
    while n > 0:
        d.add(n % 10)
        n //= 10
    return len(d) == 1
##print(is_one_digit(2))          # True
##print(is_one_digit(11))         # True
##print(is_one_digit(12))         # False

def is_palindrom(n):
    if n < 10 or is_one_digit(n):
        return False
    return n == rev(n)

# All integer palindrom less than 1000.
##print([ n for n in range(1000) if is_palindrom(n)])
                                         # comprehension (iteration.py)
''' Exercises:
Find a, b, and c that are palindroms below 10_000 where a != b != c such that
      1. a * b = c
      2. a**2 * b**2 = c
'''
##---------------------------------------------------------##

''' Greatest Common Divisor (gcd):
          gcd(m, n) = g
If g is the largest integer such that m % g == 0   and n % g == 0
'''
def gcd(m, n):
    g = m if m < n else n    ## g is the smaller of m and n.
    while g > 1 and not((m % g == 0) and (n % g == 0)):
        g -= 1
    return g
##print(gcd(34, 425))         ## 17

# Euclid propsed an algorithm for finding gcd.
def euclid_gcd(m, n):
    r = m % n
    while r > 0:
        m = n
        n = r
        r = m % n
    return n
##print(euclid_gcd(34, 425))        ## 17

#------------------------------------------------------------------

# Multiplication Tables:
def mul_table(n):
    for i in range(2, 13):
        print('%2d x %d = %4d' % (i, n, i*n))
##mul_table(2)

# 100 Multiplication-Tables.                    nested loop (iteration.py)
def mul_tables(n):
    for i in range(2, n):
        for j in range(2, 13):
            print('%3d x %2d = %4d' % (i, j, i*j))
        print()
##mul_tables(100)
        
''' Exercises
Print 12 multiplication-tables in a single table.
    Ex.         1  2  3  4  5  ........ 12
            1   1  2  3  4  5  ........ 12
            2   2  4  6  8 10 ........
            3   3  6  9 12 15 ........
            4   4  8 12 16 20 ........
            ..........................
            12 12 24 36 48 60 ........
'''
#------------------------------------------------------

# Kumon:
# Randomly generte elementary mathenmatic questions.
import random
def kumon():
    for i in range(10):
        ops = ['+', '-', 'x', '%']
        x = random.randint(2, 99)
        op = random.choice(ops)
        y = random.randint(2, 99)
        print('%2d %s %2d = ___' % (x, op, y))
##kumon()

#---------------------------------------------------------

''' Left Over Bread:
Suppose the price of left over breads is 60% of the previous day
and will throw away after the third day.
If the bread prices are 50, 100, 200, and 300 on the first day,
print the prices on each left over to the third day.
 Ex.        50	30.00	18.00	10.80	
           100	60.00	36.00	21.60	
           200	120.00	72.00	43.20	
           300	180.00	108.00	64.80
'''
def left_over_bread():
    for i in [50, 100, 200, 300]:
        print(i, end='\t')
        for j in range(3):
            i *= 0.6
            print('%.2f' % i, end='\t')
        print()
##left_over_bread()

''' Exercises
Suppose there are 5 products of prices 50, 100, 150, 200 and 500.
Print the prices on each products for 5%, 10%, 20% and 60% discount.
'''
