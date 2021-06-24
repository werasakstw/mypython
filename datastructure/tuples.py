
# Tuple: is a sequence of elements.
#   - order-oriented.
#   - immutable.
#   - generic
# Tuples can be used similar to lists except operations that cause side effect.
# Tuples use less memory and more efficient then lists.

def tuple_literal():
    # Tuple literals are enclosed in ( ), using , as separator.
    t = (1, 2, 3)
    print(t, type(t))           # (1, 2, 3) <class 'tuple'>

    # Empty tuple.
    print( (), tuple() )

    # Single element tuple listeral.
    print( (1) )            # 1 of 'init' in parenthesis.
    print( (1,) )           # tuple with 1 element.

    # Tuples may contain duplicate elements
    print( (1, 2, 1) )

    # Tuples are generic and nestable.
    print( (1, 2.0, '3', True) )  
    print( (1, (2, 3)) )

    # A comma after the last element is optional.
    print( (1, 2, 3,) )     # (1, 2, 3)
##tuple_literal()

def tuple_create():
    # Tuple may be created by tuple() factory.
    print(tuple('Hello'))       # ('H', 'e', 'l', 'l', 'o')
    print(tuple(range(3)))      # (0, 1, 2)
    print(tuple( [1, 2, 3] ))   # (1, 2, 3)
    print(tuple( (1, 2, 3) ))   # (1, 2, 3)
    print(tuple( {1, 2, 1} ))   # (1, 2)

    # Tuple can be created with initialized value using *
    print((True,)*3)        # (True, True, True)
    
    # Tuple cannot be created from comprehension.
    print( (i for i in range(3)) )   # a generator
##tuple_create()

def tuple_access():
    t = (1, 2, 3, 4)
    # Tuples can be accessed with indexing.
    print(t[0])         # 1

    # Index out of bounds are checked at runtime.
    # Negative index starts from the last position.
    print(t[-1])        # 4
    
    # Tuples can be member tested with 'in' operator.
    print(1 in t)       # True
##tuple_access()

# Tuple can be iterated with 'for' loop and comprehension.
def tuple_iterate():
    for x in ('john', 'jack', 'joe'):
        print('Hello ' + x)   # Hello john
                              # Hello jack
                              # Hello joe
    # Tuples can be iterated with enumerate() and zip().
##tuple_iterate()

# Tuples are immutable.
def immutable_tuple():
    t = (1, 2, 3, 4)
    # Tuple elements cannot be modified.
    ##t[0] = 0          # error

    # Tuple cannot be appended.
    ##t.append(3)       # error

    # Tuple Element cannot be deleted.
    ##del(t[1])         # error

    # Tuple can be modified as a whole.
    t = ('x', 'y')
    print(t)            # ('x', 'y')

    # Tuple can be deleted as a whole. clear() is not supported.
    del(t)
    ##print(t)          # error

    # If a tuple element is mutable, the element may be modified.
    b = (1, [2, 3])
    b[1].append(4)      # Lists are mutable.
    print(b)            # (1, [2, 3, 4])

    # Tuples have no methods that modifies their state e.g. append(), extends(),
    #  insert(), remove(), pop() reverse() and sort().
##immutable_tuple()

#-------------------------------------------------------------------

# Tuple Unpacking: is an assignment of a tuple to several variables.
def unpacking():
    a, b, c = ('John', 'Jack', 'Joe')
    print(a, b, c)          # John Jack Joe

    # Multiple Tuples Unpacking:
    (a, b), (c, d, e) = (1, 2), (3, 4, 5)
    print(a, b, c, d, e)    # 1 2 3 4 5

    # Nested Tuples Unpacking:
    (a, (b, c)) = (1, (2, 3))
    print(a, b, c)          # 1 2 3

    # The left and right sides of tuple unpacking must have the same size.
    ##(a, b) = (1, 2, 3)    # error
    ##(a, b, c) = (1, 2)    # error

    # Wildcards *
    (a, b, *c) = (1, 2, 3, 4, 5)    # c is a list, not a tuple.
    print(a, b, c)          # 1 2 [3, 4, 5]

    (a, *b, c) = (1, 2, 3, 4, 5)
    print(a, b, c)          # 1 [2, 3, 4] 5

    (a, b, *c) = (1, 2)
    print(a, b, c)          # 1 2 []

    # Automatic tuple packing.
    t = 1, 2, 3   # On the right side of =, the () is optional.
    print(t)                # (1, 2, 3)

    # Multiple Assignment is a tuple unpacking in disguise.
    x, y, z = 1, 2, 3
    print(x, y, z)          # 1 2 3

    a, b, *c = 1, 2, 3, 4, 5
    print(a, b, c)          # 1 2 [3, 4, 5]

    # Tuple unpacking can exchange values in one statement
    #   without using a temporary holder.
    x, y = 1, 2
    y, x = x, y
    print(x, y)             # 2 1

    # The assignment operator =, is right associative and
    #   returns result as functions.
    a = b = c = 1
    print(a, b, c)          # 1 1 1
##unpacking()

#-----------------------------------------------------------------

# Passing tuples as parameters has no side effect.  
def tuple_param():
    def add_x(a):
        a += 'x'
    
    a = ['a','b']
    add_x(a)
    print(a)        # ['a', 'b', 'x']
    
    t = ('a','b')
##    add_x(t)      # error
##tuple_param()
 
# Tuples allow a function to return more than one values.
def div10(n):
    return n//10, n%10
##print(div10(12))          # (1, 2)

# Tuples allows passing variable length arguments (var-arg).
def var_arg():
    # Arguments are collected into a tuple and passed to the parameter.
    def f(*a):
        print(a)

    f()             # ()
    f(1)            # (1,)
    f(1, 2)         # (1, 2)
##var_arg()

#------------------------------------------------------------

# Tuples may reperent structured data without creating a class.
# A mechanism for DOO (Diluted Object Oriented).
def doo():
    john = (1, 'John Rambo', 3.8)
    
    # Tuple elements must be accessed by position.
    print(john[0], john[1], john[2])
        
    # Tuple has no protection against missing, extra and wrong order fields.
    jack = (1, 'John Rambo', 'cs', 3.8)
##doo()
    
# 'namedtuple' object can be used like a tuple but elements can be accessed by field names.
# Nametuples are implemented as immutable objects and more memory efficient than regular objects.
from collections import namedtuple
def named_tuple():
    # namedtuple(<type name>, <fields>)
    Student = namedtuple('Student', 'id name gpa')
    
    john = Student(1, 'John', 1.8)
    print(john)
    print(john.id, john.name, john.gpa)

    # Nametuples has protection against missing and extra fields.
##    jack = Student(2, 'Jack')
##    joe = Student(3, 'Joe', 3.5, 'cs')
    
    # But no protection against type or wrong order fields.
    jim = Student(4, 3.5, 'Joe')
    print(jim)
##named_tuple()

# typing.NamedTuple
import typing
def typing_nametuple():
    class Student(typing.NamedTuple):
        sid: int
        name: str
        gpa: float

    john = Student(1, 'John', 1.8)
    print(john)
    print(john.sid, john.name, john.gpa)

    # typing.NamedTuple has protection against type or wrong order fields.
##    jack = Student(2, 'Jack')
##    joe = Student(3, 'Joe', 3.5, 'cs')
    # Type annotations are not enforced by default.
    # A type checking tool like mypy is needed.
    jim = Student(4, 3.5, 'Joe')
##typing_nametuple()
