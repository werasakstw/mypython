
# Let define a function for converting Celsius to Fahrenheit:
#             F = C * (9/5) + 32
def to_fahrenheit(c):       # definition, indentation  (functions.py)
    return c*(9/5) + 32
##print(to_fahrenheit(0), to_fahrenheit(100))     # 32.0 212.0

''' Exercises: Write functions for the following conversions.
      a.  1 degree = 0.0174532925 radians
      b.  1 mile = 1.609344 km
      c.  1 kg   = 2.20462262 pounds
      d.  12 inches = 2.54 centimeters
      e.  celsius = (fahrenheit - 32) * 5 // 9
'''
#------------------------------------------------------------------
         
import math                                      #       (imports.py)
##print(dir(math))      # dir(<nsp>) returns a list of names in <nsp>.

''' Python 'math' module has factorial function.
                   n! = n*(n-1)*(n-2)*...*1.        '''
##print(math.factorial(5))             # 120
# Try: Compare the value of (5!)! and a googol, which is bigger?

# A circle area is pi*(r**2) where r is the radius of the circle.
def circle_area(r):
    return math.pi*(r**2)
##print('%.2f' % circle_area(10))      # 314.16

''' Exercises: Write functions to compute the following:
    a. A triangle area is 0.5 * base * height.

    b. A triangle area is sqrt(s * (s - s1) * (s - s2) * (s - s3))
           where  s is (s1 + s2 + s3) / 2
                  s1, s2, and s3 are lengths of each sides.
           
    c. A polygon area is (n * s**2) / (4 * tan(pi / n))
           where s is the length of each side
                 n is the number of sides.
           Hint:  math.tan(<radian>)
        
    d. A sphere volume is (4/3) * pi * (radius**3).

    e. Volume of a Cylinder is pi * <height> * (radius**2).
'''
#----------------------------------------------------------------

''' Let's compute the following expression: Given an integer n,
          ((((n * 2) - 16) * 4) / 8) + 15 - n       '''
def seven_up1(n):      
    a = n * 2                              #     (variables.py)
    b = a - 16
    c = b * 4
    d = c // 8                             # //  (operators.py)
    e = d + 15
    return e - n
##print(seven_up1(12345))
                                      
##n = int(input('Enter a number: '))       #   (print_input.py)
##print(seven_up1(n))

# If a variable value is not needed anymore, it should be reused.
def seven_up2(n):
    a = n * 2
    a = a - 16
    a = a * 4
    a = a // 8
    a = a + 15
    return a - n
##print(seven_up2(12))

''' Python allows inplace operator:
       x <op>= y     <-->    x = x <op> y
  e.g. x += 1        <-->    x = x + 1          
'''
def seven_up3(n):
    a = n * 2
    a -= 16                             #  in-place    (operators.py)
    a *= 4
    a //= 8
    a += 15
    a -= n
    return a
##print(seven_up3(123))

''' Python supports bit shift operations.
      x << n     shifted left n bits.
              ==  x * 2**n        multuplied by 2 to the power of n
      x >> n     shifted right n bits.
              ==  x / 2**n        divided by 2 to the power of n
Bit shift allows multiply and divide integers by multiple of 2.          
'''
def seven_up4(n):
    a = n * 2
    a -= 16                         # bit-shift    (operators.py)
    a <<= 2             # a *= 4
    a >>= 3                 # a //= 8
    a += 15
    a -= n
    return a
##print(seven_up4(1234))

'''                                                (variables.py)
Expressions can be evaluated with precedence and associative rules.
e.g.      x + y + z      -->    (x + y) + z
          x + y * z      -->    x + (y * z)
'''
##print(1 + 2 * 3)        # 7

# Parentheses override the precedence and associative rules.
def seven_up5(n):
##    return n * 2 - 16 * 4 // 8 + 15 - n
    return ((((n * 2) - 16) * 4) // 8) + 15 - n
##print(seven_up5(12345))

#-----------------------------------------------------------------

''' How old are you?:
Suppose the age of your friend is a two digits interger ab.
     Let compution:  x = ((((a * 2) + 5) * 5) + b) - 25 
Then a and b can be computed from x by:
          a = x // 10     ## the tenths place digit
          b = x % 10      ## the unit place digit
'''
def age(a, b):
    x = ((((a * 2) + 5) * 5) + b) - 25
    return (x//10, x %10)
##print(age(2, 5))

''' Exercises
1. Ask your friend the month of birthday, counting January as 1 etc.
Let's say it is m, and let his age be a. Then computes:
          x = (((((m*2)+5)*50)+a)-356)+115
    Write a program to show that a and m can be computed from x by:
          a = x / 100
          m = x % 100

2. Ask your friend to think of any three single digits.
Let's say they are a, b and c. Then computes:
          x = ((((((a*2) + 5)*5) + b)*10) + c) - 250
    Write a program to show that a, b and c can be computed from x by:
          a = x / 100
          b = (x / 10) % 10
          c = x % 10
'''
#-----------------------------------------------------------------

''' Multiplication of two numbers: Suppose a and b are two integers.
    To compute a * b
              Let x = 10-a
                  y = 10-b
        The high digits of the result is a-y (or b-x).
        The low digits of the result is x*y
            e.g.   a = 7    b = 8
        then  x = 10 - 7 = 3     y = 10 - 8 = 2
            [a-y][x*y]  = [7-2][3*2]  = 56
A program to verify the method:
'''
def mul_test():
    def mul(a, b):
        x = 10-a
        y = 10-b
        return 10*(a-y) + x*y
    
    for a, b in zip([7, 41, 123], [23, 78, 4567]):
        print('%d * %d = %d = %d' % (a, b, a*b, mul(a,b)))
                #  7 * 23 = 161 = 161
                # 41 * 78 = 3198 = 3198
                # 123 * 4567 = 561741 = 561741
##mul_test()

#######################################################################

''' Droppin an object with initial speed 'u' meters/sec from the height
'h' meters, assume the earth gravity is 9.8 meters/(sec**2) the object
will hit the ground at speed v = sqrt(u**2 + 2*g*h).
'''
def speed(u, h):
    return math.sqrt(u**2 + 2 * 9.8 * h)
##print('%.2f' % speed(0, 100))               ## 44.27

''' Exercises::
1. The Earth is sphere, two long distance points are not on a stright line.
   Given (t1, g1) and (t2, g2) are (latitude, longitude) of two points.
      distance = 6371.01*arccos(sin(t1)*sin(t2) + 
                  cos(t1)*cos(t2)*cos(g1 - g2))
      where latitudes and longitude must be in degrees
            6371.01 is the earth radius in kilometers.
   Write a function distance(t1, g1, t2, g2).
        Hint:  math.radians(<degree>)  return <radian>.

2. Easter is the Sunday immediately after the first full moon that follows
     the spring equinox. It is not a fixed date in the Gregorian calendar
     and vary between March 22 and April 25.
   An algorithm to compute the date of Easter for a year.
       a = year % 19
       b = math.floor(year / 100)
       c = year % 100
       d = math.floor(b / 4)
       e = b % 4
       f = math.floor( (b + 8) / 25 )
       g = math.floor( (b - f + 1) / 3 )
       h = (19*a + b - d - g + 15) % 30
       i = math.floor(c / 4)
       k = c % 4
       j = (32 + 2*e + 2*i - h -k) % 7
       m = math.floor( (a + 11*h + 22*j) / 451)
    The month of Easter is math.floor( (h + j - 7*m + 114) / 31)
    The date of Easter is ((h + j - 7*m + 114) % 31) + 1
    Write a function easter(year) which returns (month, date) of
      the Easter of the year.

3. In winter, wind chill makes us felt cooler than the real temperature.
   In 2001, Canada, United Kingdom and United States defined:
     wind_chill_index = 13.12 + 0.6215*T - 11.37*V**0.16 + 0.3965*T*V**0.16
         where T is the temperature in Celsius
               V is the wind speed kilometers/hour.
   The wind chill index is the feel temperature in Celsius, which will be
     effective if the temperature is below 10 Celsius and wind speed is
     more than 4.8 kilometers/hour.
   Write a function wind_chill_index(T, V)
'''


