'''
All values are associated with its type.
A type defines how to access the value which includs allowed operations.

Python implements types using class, no primitive types.
Everything in Python are objects(instances) of some classes.

The most commonly used built-in types:
    1. Number: int, float, boolean and complex.
    2. Sequence: str, list, tuple, set, and dict. (There are a lot more).
Python has no byte, short, long, double and char.

Literals: are symbols in source codes to represent values.
All literals have characteristic that indicate its type.
Compilers know the literal's type at the compile time. e.g.
       1                 int
       1.0               float
       True              bool
       1+2j              complex
       'Hello'           str  (string type)
       [1, 2]            list
       (1, 2)            tuple
       {1, 2}            set
       {'a':1, 'b':2}    dict
'''

# 'bool' literals are True and False.
##print(True, type(False))    # <class 'bool'>

'''
'int' literal represents integer value which is a sequence
of digits (0-9) that do not begin with 0 and contain no decimal point.
type(<arg>) returns the type of <arg> which may be literal, variable or type.
'''
##print(1, type(1))     #  1 <class 'int'>
##print(012)          # error

'''
Python creates an 'int' value as a PyIntObject for small integers (-5 -> 256).
Bigger integers are created with increasing size as needed.
sys.getsizeof(<var>) returns the size of <var> in bytes.
'''
import sys
##print(sys.getsizeof(2))           # 14
##print(sys.getsizeof(2**10))       # 14
##print(sys.getsizeof(2**100))      # 26
##print(sys.getsizeof(2**10000))    # 1346

# Python allows number based 'int' literals with prefixed.
def int_bases():
    print(10)	        # 10   decimal (default)
    print(0b10)	        # 2    binary
    print(0o10)	        # 8    octal
    print(0x10)	        # 16   hexadecimal

    # There are built-in functions to converse decimal value to the base values.
    print(bin(10))	# 0b1010
    print(oct(10))	# 0o12
    print(hex(10))	# 0xa

    # int(<str>) creates an int value from <str> in decimal base.
    # int(<str>, <base>) creates an int value from <str> in <base>.
    print(int('007'))       # 7
    print(int('100', 2))    # 4
    print(int('100', 5))    # 25
    print(int('a', 16))     # 10
    # print(int('a', 10))   # error: there is no 'a' symbols in base 10. 
##int_bases()

#--------------------------------------------------------------

'''
'float' literal represents floating-point value, there are two representations:
    - floating-point notation  e.g  1.23
    - scientific notation      e.g  1.2e3
Zero trailing are optional.
'''
##print(1.23, 1.23e4)  # 1.23 12300.0

# Python as well as the others have problem with float computation.
##print(0.1 + 0.2)      # 0.30000000000000004

# Divide by 0(int) or 0.0(float) are ZeroDivisionError.
# Python has no undefined, Infinity and NaN.

#--------------------------------------------------------------

''' Embedded Underscore:
'int' and 'float' literals allow embedded _ within digits.
That do not affect the values just improve readablility.
'''
def underscore_embedded():
    print(1_000)                    # 1000
    print(1_000.00)                 # 1000.0
    print(0b1000_1100_1110_1111)    # 36079
    print(0x8C_EF)                  # 36079
##underscore_embedded()

#--------------------------------------------------------------  

''' All built-in type implements 'factory' functions.
Factory functions can be used for
- Creating default values.
- Type conversions.
'''
def default_values():
    print(bool())           # False
    print(int())            # 0
    print(float())          # 0.0
    print(str())            # <empty str>
    print(list())           # []
    print(tuple())          # ()
    print(set())            # set()
    print(dict())           # {}
##default_values()

def type_conversions():
    # bool: Values are False if it is zero or empty, and True otherwise.
    print(bool(0), bool(''), bool([]))        # False False False
    print(bool(1), bool('hello'), bool([1]))  # True True True

    # int:
    print(int(False), int(1.2), int('2'))     # 0 1 2

    # float:
    print(float(True), float(1), float('1.2')) # 1.0 1.0 1.2

    # str:
    print(str(True), str(1), str(1.2))      # True 1 1.2
##type_conversions()
    
#------------------------------------------------------------------

''' Typed Languages: performs type checking to ensure that operand types
must be correspond to the operator.
Python is a typed language, but not all type errors can be detected at compile time. 

If the types are miss-matched it is called mix-mode expression e.g. 1 + 1.2.
Python performs automatic type conversion for Number types: bool, int and float.
'''
##print(True + 1, 1 + 1.2, 1.2 + False)     # 2 2.2 1.2

# But mix-mode is not allowed for non-numberic type, explicit conversion is needed.
##print(1 + '2')            # error
##print(1 + int('2'))       # 3
##print(str(1) + '2')       # 12

# Another kind of automatic type conversion is 'coercion' which is
# conversing a value of any type to a bool value, mostly used as condition.
def coercion():
    x = 1
    if x:           # x != 0
        print('Not Zero')           # Not Zero

    if not x:       # x == 0
        print('Zero')

    a = [0]
    if a:           # len(a) > 0
        print('Not Empty')          # Not Empty
    if not a:       # len(a) == 0
        print('Empty')
        
    # Coercion should be used in condition only, not part of comparisons. 
    print(x == True, a == True)      # True False
    
    # Numbers are allowed in mix-mode, but not non-numbers.
    print(x + True, x + False)       # 2 1
##    print(a + True)                  # error

    # Coercion should not be part of any logical expression.
    print(x and False, x or True, a and False, a or True) # False 1 False [0]
##coercion()

#-------------------------------------------------------------------------

# Python has 'None' literal for representing no value, but not an empty value.
def none():
    n = None
    # None is coerced to False
    if not n:
        print('None')        # None

    # But None is not equal to False.
    print(n == False)        # False

    # None is not an Empty value.
    print(n == [])           # False

    # None should not take part in any expressions.
    print(n and False)       # None
##    print(n + 1)           # error
##none()    






