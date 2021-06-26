
# Leap Years:
# The Earth takes 365(1/4) days and a little bit to orbit the Sun.
# So February 29, is included in some years to correct the extra times.
# Such the years are called leap years.

# To determine whether a year is a leap year:
#    If the year is divisible by 400 it is a leap year.
#    Else if it is divisible by 100 it is not a leap year.
#    Else if it is divisible by 4 it is a leap year.
#    All the remains are not leap years.  
def is_leap_year(year):
    if year % 400 == 0:                   # if, else, elif (decision.py)
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    return False

# 2000 is a leap year but 1000 is not. 
##print(is_leap_year(2000), is_leap_year(1000))

# All Leap years from 2020 to 2112.
##print([y for y in range(2020, 2112) if is_leap_year(y)])

# All years from 2020 to 2112 that divisible by 4 but not a leap year.
##print([y for y in range(2020, 2112) if y % 4 == 0 and not is_leap_year(y)])

# All years from 2020 to 3000 that divisible by 100 but is a leap year.
##print([y for y in range(2020, 3000) if y % 100 == 0 and is_leap_year(y)])

#-------------------------------------------------------------------

# Check whether a date (day, month, year) is valid, for years 1754 to 2200.
def is_valid_date(d, m, y=2021):        # default parameter (functions.py)
    if d < 1 or d > 31 or m < 1 or m > 12 or y < 1753 or y > 2199:
        return False
    if m == 2:      # February
        if is_leap_year(y) and d <= 29:
            return True
        if d > 28:
            return False
    if (m == 4 or m == 6 or m == 9 or m == 11) and d == 31:
        return False
    return True
##print(is_valid_date(31, 1, 2020))
##print(is_valid_date(31, 1))

#-------------------------------------------------------------------

# Beginning of Seasons:
# In the old days, the beginning of seasons were fixed by high priests.
# Now there is the following suggestion:
#              Season                Beginning
#            Spring                March 20
#            Summer                June 21
#            Fall                  September 22
#            Winter                December 21
# To map <month, date> to <season>.
def season(month, date):
    if month == 'January' or month == 'February':
        return 'Winter'
    elif month == 'March':
        if date < 20:
            return 'Winter'
        else:
            return 'Spring'
    elif month == 'April' or month == 'May':
        return 'Spring'
    elif month == 'June':
        if date < 21:
            return 'Spring'
        else:
            return 'Summer'
    elif month == 'July' or month == 'August':
        return 'Summer'
    elif month == 'September':
        if date < 22:
            return 'Summer'
        else:
            return 'Fall'
    # No return is returning None by default.
##print(season('September', 20))
##print(season(date=20, month='September'))   # named arguments (functions.py)
    
#------------------------------------------------------------------

# Body Mass Index: a simple health indicator.
#              bmi = weight / (height**2)
#    where weight is in kilograms and height in meters.
# BMI interpretation:
#             status                     bmi              
#          Underweight              bmi  < 18.5
#          Normal                   18.5 <= bmi < 25.0
#          Overweight               25.0 <= bmi < 30.0
#          Obesity class I          30.0 <= bmi < 35.0
#          Obesity class II         35.0 <= bmi < 40.0
#          Obesity class III        40.0 <= bmi
def bmi(weight, height):
    _bmi = weight / (height**2)
    return 'Underweight'       if _bmi < 18.5 else \
           'Normal'            if 18.5 <= _bmi < 25.0 else \
           'Overweight'        if 25.0 <= _bmi < 30.0 else \
           'Obesity class I'   if 30.0 <= _bmi < 35.0 else \
           'Obesity class II'  if 35.0 <= _bmi < 40.0 else \
           'Obesity class III'
##print(bmi(weight=75, height= 1.65))

'''  Exercises
1.Visible light wavelength(w) are in ranges from 380 to 750 nano meters,
     which is divided into 6 colors:
           Violet     380 <= w < 450
           Blue       450 <= w < 495
           Green      495 <= w < 570  
           Yellow     570 <= w < 590
           Orange     590 <= w < 620
           Red        620 <= w <= 750
           Invisible    otherwise
    Write functions to map from wavelengths to colors.

3. Electromagnetic frequency(f) can be classified into 7 categories:
           Radio Waves                  f <=  3.0e+09
           Microwaves         3.0e+09 < f <= 3.0e+12
           Infrared           3.0e+12 < f <= 4.3e+14
           Visible Light      4.3e+14 < f <= 7.5e+14 
           Ultraviolet        7.5e+14 < f <= 3.0e+17 
           X-Rays             3.0e+17 < f <= 3.0e+19
           Gamma Rays         3.0e+19 < f                 
     Write functions to map from frequency to categories.
'''
#---------------------------------------------------------------

# Generate and Test
# Find 4 consecutive odd integers whose sum is exactly 80.
def odd80():
    max = 80 // 4   # would not excess 1/4 of 80.
    for x in range(1, max, 2):
        if (x + (x+2) + (x+4) + (x+6) == 80):
            print(x, x+2, x+4, x+6)     # 17 19 21 23
##odd80()

# Find the smallest integer which is dividable by all integers from 2 to 10.
def smallest_dividable():
    def is_div_by_2_to_10(n):
        for i in range(2, 10+1):
            if n % i != 0:
                return False
        return True

    n = 100  # The value is not less than 100.
    while True:
        if is_div_by_2_to_10(n):
            print(n)
            break
        n += 1
##smallest_dividable()        # 2520

''' Exercises
1. If a rectangle whose area is equal to the sum of the 4 sides.
        e.g.   width*height = 2*width + 2*height
    Find the smallest width and height.

2. The price of three chickens and a duck is equal to two gooses
and a chicken. Two duck and three gooses cost $25. Find the prices
of each chicken, duck and goose.

3. John bought a number of shirts for 265 Bath each and a number
of pants for 344 Bath each. The cost of pants is greater than
shirts, 33 Bath. How many pants did he buy?

4. A piece of burger costs 50 Bath. A can of pepsi costs 10 Bath.
A piece of candy costs 0.50 Bath. John bought all three together
which cost 1000 Bath and got exactly 100 pieces. How much each of
the burger, pepsi and candy costs?

5. In an examination there are 26 questions. A right answer gets 8 points
wrong answer minus 5 points. John answered every questions and got exactly
zero points. How many right answers does he make?

6. On the archer target, there are places for 16, 17, 23, 24, 39, 40
score points. The king ordered Robin Hood to score exactly 100 points
with the lowest number of arrows. How many arrows must he need?
'''

#---------------------------------------------------------------

''' Equation Solving 
In school, finding a solution of n variables requires n equations.
Not anymore for generate and test.

Find all solutions for the equation:
      x(x+1) = y(y+1)(y+2)    where 0 < x, y < 100
'''
def solve_eq():
    for x in range(1, 100):
        for y in range(1, 100):
            if x*(x+1) == y*(y+1)*(y+2):
                print(f'{x}({x}+1) = {y}({y}+1)({y}+2)')
##solve_eq()
                
''' Exercises
For 0 < x < y < z < 10, find solutions for the following equations:
      1.1.    x + y + z = x * y * z
      1.2.    x**3 + y**3 + z**3 == 6**2
      1.3.    x**3 + y**3 + z**3 == 6*x*y*z
   .
'''
#---------------------------------------------------------

'''            Some Kinds of Math Pproblems
Find all positive 2 digits numbers less than 100 (let's say ab)
such that:     (a*10) + b = 4(a+b)
       e.g.    (1*10) + 2 = 4*(1+2) = 12     '''
def ab4():
    for a in range(1, 10):
        for b in range(1, 10):
            if a*10 + b == 4*(a+b):
                print('%d%d = 4*(%d+%d)' % (a, b, a, b))
##ab4()
# Try: 2, 3 or 5 times the sum of its digits.

''' Let a, b, c, and d are successive numbers less than 10.
    Find all of them such that:
                  ab = c * d
      Hint:       12 = 3 * 4     '''
def four_successive():
    for a in range(1, 6):  # They are less than 10.
        b, c, d = a+1, a+2, a+3        # multiple assignment
        if a*10 + b == c * d:
            print('%d%d = %d * %d' % (a, b, c, d))
##four_successive()

''' Show your friends that you can simplify a fraction by canceling
the tenth digit with the unit digit. ex. 16/64 = 1/4
The result is correct by chance, so we call it is a howler. 
Find all the howlers that are fractions with number less than 100.
'''
def howlers():
    for a in range(1, 10):
        for b in range(1, 10):
            if a != b:
                for x in range(0, 10):
                    if (10.0*a + x)/(10.0*x + b) == a/b:
                        print('%d/%d' % (10*a+x, 10*x+b))
##howlers()
                        
''' Exercises: There are many kinds of howlers, for example.
        Let a, b and c are single digit numbers.
             abc * xyz  = ax * by * cz
      e.g.   126 * 110  = 11 * 21 * 60  =  13860
    Write a program to find all of them.  '''

#---------------------------------------------------------------

'''          Characters Digits Mapping Puzzles
Find the correspond digits for each characters.
              S E N D
            + M O R E
            ---------
            M O N E Y
'''
def send_money():
    [(s, e, n, d, m, o, r, y)] = [(s, e, n, d, m, o, r, y)
        for s in range(1, 10)
        for e in range(0, 10) if (s != e)
        for n in range(0, 10) if (n not in [s, e])
        for d in range(0, 10) if (d not in [s, e, n])
        for m in range(1, 10) if (m not in [s, e, n, d])
        for o in range(0, 10) if (o not in [s, e, n, d, m])
        for r in range(0, 10) if (r not in [s, e, n, d, m, o])
        for y in range(0, 10) if (y not in [s, e, n, d, m, o, r]) and
                (s*1000 + e*100 + n*10 + d) +
                (m*1000 + o*100 + r*10 + e) ==
                (m*10000 + o*1000 + n*100 + e*10 + y)
    ]
    a = str(s) + str(e) + str(n) + str(d)
    b = str(m) + str(o) + str(r) + str(e)
    c = str(m) + str(o) + str(n) + str(e) + str(y)
    print(a, '/' , b, '=',  c)
##send_money()

''' Exercises: Find the correspond numbers for each characters.
            SANTA
          - CLAUS
          -------
             XMAS
'''
#------------------------------------------------------------------

'''                      Magic Squares
Fill numbers 1 to 9 in a 3x3 square such that the sum in rows, columns,
and diagonals are equal.
'''
import itertools
def magic_square():   
    def test(a):
        if sum(a[0:3]) == sum(a[3:6]) == sum(a[6:10]) == \
           sum(a[0:10:3]) == sum(a[1:10:3]) == sum(a[2:10:3]) == \
           sum(a[0:10:4]) == sum(a[2:8:2]):
               return True
        return False
    
    def print_square(a):
        print(a[0:3]); print(a[3:6]); print(a[6:9], end='\n\n')
        
    for a in itertools.permutations(range(1, 10)):
        if test(a):
            print_square(a)
##magic_square()

''' Homework:
The magic_square() produces similar squares which are the results
of flipping or rotating. Write a program that eliminates such the cases.

Exercises: Find digit for each letter to fill a 3x3 square so that:
          a b c               x d a
        + d e f             + y e b
          x y z               z f c
The second square is the result of rotating the first square 90 degree.
'''

## Magic Squares Generator:
from pylab import zeros
def magic_sq(n):
    if n % 2 == 0:  
        return 'Parameter must be odd number.'
    m, row, col = zeros([n, n]), 0, n//2
    for num in range(1, n**2+1):
        m[row, col] = num       # fill the cell
        col = (col+1) % n
        row = (row-1) % n
        if m[row, col]:
            col = (col-1) % n
            row = (row+2) % n
    return m
##print(magic_sq(3))
##print(magic_sq(5))
