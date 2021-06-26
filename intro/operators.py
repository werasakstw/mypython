''' Arithmetic Operators:
 + addition,   - subtraction,  * multiplication,   ** power
If both operands are int, the result is an int.
If one or both operands are float, the result is a float.
'''
def ari_op():
    print(1 + 2)          # 3
    print(4 ** 0.5)	  # 2.0

    # / is floating point division returns a float.
    print(3 / 2)          # 1.5

    # // is integer division returns the quotient as an int.
    # But may be applied to floats and results in float.
    print(3 // 2)         # 1
    print(3.0 // 2.1)     # 1.0
    
    # % is integer remainder returns the remainder as an int.
    print(5 % 2)          # 1
    print(5.0 % 2.5)      # 0.0

    # divmod() returns a tuple of quotient and remainder 
    q, r = divmod(5, 2)
    print(q, r)	          # 2, 1
##ari_op()

#-----------------------------------------------------------------

'''In-Place Operators:  (with side effect)
           <variable> <op>= <expression>
    +=   -=   *=   /=   //=   %=   **=
'''
def ass_op():
    a = 1
    a += 1          # same as a = a + 1
    print(a)        # 2    
    
    a *= 2
    print(a)        # 4
##ass_op()

#-----------------------------------------------------------------

''' Logical Operators:
    not        unary negation
    and        conditional and
    or         conditional or
The operands and result are boolean.
'''
def logical_op():
    print(not True)         # False
    print(True and True)    # True
    print(True or False)    # True
##logical_op()

def short_circuit():
    def true_func():
        print("true_func()")
        return True

    def false_func():
        print("false_func()")
        return False

    print(true_func() or false_func())  # true_func() True
    print(false_func() or true_func())  # false_func() true_func() True
    print(true_func() and false_func()) # true_func() false_func() False
    print(false_func() and false_func())# false_func() False
##short_circuit()

#-----------------------------------------------------------------

''' Bitwise Operators:
   ∼  bitwise complement (prefix unary operator)
   &  bitwise and
   |  bitwise or
   ^  bitwise exclusive-or
The operands and result are int.
'''
def bit_op():
    a = 0b01
    b = 0b11
    x = a & b
    y = a | b
    z = a ^ b
    print(x, bin(x))        # 1 0b1
    print(y, bin(y))        # 3 0b11
    print(z, bin(z))        # 2 0b10
##bit_op()

#-----------------------------------------------------------------

''' Bit-Shift Operators.
  x << n     shifted left n bits, filling in with zeros
          ==  x * 2**n        multuplied by 2 to the power of n
  x >> n     shifted right n bits, filling in with zeros
          ==  x / 2**n        divided by 2 to the power of n
Bit shift allows multiply and divide integers by multiple of 2.
'''
def bit_shift():
    x = 1
    for _ in range(5):
        x <<= 1
        print(x, end=', ')   # 2, 4, 8, 16, 32,
    print()
    
    for _ in range(5):
        x >>= 1
        print(x, end=', ')   # 16, 8, 4, 2, 1,
##bit_shift()

#-----------------------------------------------------------------

'''
Comparison Operators:
     <   less          <=    less equal
     >   greater       >=    greater equal
     ==  equal         !=    not equal
May be mix_mode, the result are alway boolean.
Numeric operands are compared by cardinal order.
String operands are lexicographically compared.
An exception is raised if the operands are incomparable types.
'''
def comp_op():
    print(1 == 1.0)             # True         equal to
    print(False < True)         # True         less than
    print('jack' <= 'john')     # True         less than or equal to
    print(1 > True)             # True         greater than
    print(0 >= 0.0)             # True         greater than or equal to

    # Python allows comparison expressions.
    x = 1; y = 12
    print(0 < x < 10 < y)	# True
##comp_op()

#-----------------------------------------------------------------

'''
Type Conversion Operators:
All built-in type implements 'factory' functions which are the same name as the type.
Factory functions can be used for:
- Creating default values of the types.
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

###################################################################

'''
1. Semantics of // and %
For q = n // m and r = n % m, that means q * m + r == n.
Python guarantees that:
   For m is positive, 0 ≤ r < m.
   For m is negative, m < r ≤ 0.
'''  
##print(-27 // 4, -27 % 4)        # -7 1
##print(27 // -4, 27 % -4)        # -7 -1

'''
2. Precedence:
For expression,    <operand_1> <op1> <operand_2> <op2> <operand_3>
If it is evaluated as ((<operand_1> <op1> <operand_2>) <op2> <operand_3>)
Then the operator <op1> has more priority than <po2>, else otherwise.

          Order of Precedence in Python
1. Tuple, List and Dictionary creations.
2. Indexing and Slicing operations.
3. Bracket: (), [], {}.
4. Attribute Accessing: .
5. Function invocation.
6. Arithmetic operators: unary(-), exponential(^), (*, /), and (+, -)
7. Bitwise operators.
8. Comparison and Identity operators.
9. Logical operators
10. Anonymous operators

3. Associative:
For expression,    <operand_1> <op> <operand_2> <op> <operand_3>
If it is evaluated as ((<operand_1> <op> <operand_2>) <op> <operand_3>)
   Then the operator <op> is left associative.
If it is evaluated as (<operand_1> <op> (<operand_2> <op> <operand_3>))
   Then the operator <op> is right associative.
'''


