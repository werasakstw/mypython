
'''
A function is defined with a keyword 'def' follows by a <name>
and possiblly <parameters> in () and a <body> of the function.
         def <name>(<parameters>):
             <body>

A function definition without a body is an error.
'pass' is a keyword to denote an empty body.
'''
def empty_function():
    pass
##empty_function()

''' 'Doc String' is meta information of a function.
A doc string is defined between the head and body of the function
and bound to the __doc__ attribute.
'''
def func():
    '''This is a doc string.'''
    pass    # If an empty function has a doc string, 'pass' is optional.
##print(func.__doc__)

# The doc string is shown when the function is passed to help().
##help(func)

# PEP257 defines what should be given in a docstring.

#------------------------------------------------------------

'''
Parameters are values that passed to the execution of a function.
That allows a function to be used in different contexts.
Parameters are defined without type.

The passed value on caller side is called 'argument'.
The variables to receive values on callee side is called 'parameter'.
'''
def hello(name):
    print('Hello ' + name)
##hello('John')

# Parameter types may vary at each executions.
def hello(name):
    print('Hello', name)
##hello('John')       # Hello John
##hello(123)          # Hello 123

'''
A function may or may not return a value.
The returned value must be specified with 'return' keyword. 
Python functions are defined without returned type.
'''
def hi(name):
    return 'Hi ' + name
##print(hi('John'))
 
# A function may return different types.
def return_type(x):
    if x == 1:
        return 1
    return 'A'
##print(return_type(1), return_type(2))   # 1 A

# A function must return a single value, but may be a tuple.
def return_tuple():
    return 1, 2     # Tuple packing
##x, y = return_tuple(); print(x, y)    # 1 2

# 'return None', 'return' and no return are the same.
def greet(name):
    if name == 'John':
        return 'Hello'
    ##return None
    ##return
##print(greet('Jack'))        # None

'''
'None' is a special value that allows passing/returning nothing.
But its value must be test and handled explicitly.
'''
def greet(name):
    if name is None:
        print('Hello whoever you are.')
    else:
        print('Hello', name)
        
##greet()       #  error    
##greet(None)     #  Hello whoever you are.
##greet('John')   #  Hello John
        
#-----------------------------------------------------------

''' Python 3.5 allows type annotations for function header:
     - parameter follows :
     - return type follows ->
The metadata is just for type hints, no effect to the codes
Compilers do not perform type checking nor enforcement.
They are stored in the  __annotations__ attribute of the function.
'''
def type_anno(x: int, y: float) -> str:
    return x + y
##print(type_anno(1.0, 2))
##print(type_anno.__annotations__)

# Metadata may be type(e.g. int and str), but variable names or expressions are allowed. 
john = 'John Rambo'
def f(x: john, y: 'int > 0' = 1):
    pass

#------------------------------------------------------------------

# Python allows nested functions.
def outter(name):
    print('Start')
    def inner(n):       
        return 'Hello ' + n
    print(inner(name))
##outter('John')

# Python creates a function (which is an object) dynamically.
def fun_def():
    def f():
        pass
    print(dir())    #  ['f']     A list of name defined in the current scope.
    
    def g():
        pass
    print(dir())    #  ['f', 'g'] 
##fun_def()

# Python does not allowed function overloading.
def function_shadowing():
    def f(x):
        print(x)
        
    def f(x, y):    #  The previous f() is shadowed.
        print(x, y)

    # f(1)          #  error
    f(1, 2)         #  1 2
##function_shadowing()

#-----------------------------------------------------------

'''
There are different interpretations of 'pass by reference'.
Python parameter passing is called 'call by sharing' which means
the argument and parameter are alias.
We need to concern only whether the arguments have side effect.
If the arguments are immutable, there will have no side effect.
If the arguments are mutablem, there will be side effect.
If side effect is not desirable, the mutable arguments must be copied and pass the other copy.
'''
def sharing():
    def f(x, y):
        x += y
        return x
    
    a, b = 1, 2             #  int is immutable.
    print(f(a, b), a, b)    #  3 1 2   

    a, b = 'a', 'b'         #  str is immutable.
    print(f(a, b), a, b)    #  ab a b 

    a, b = (1, 2), (3, 4)   #  tuple is immutable.
    print(f(a, b), a, b)    #  (1, 2, 3, 4) (1, 2) (3, 4) 

    a, b = [1, 2], [3, 4]   #  list is mutable.
    print(f(a, b), a, b)    #  [1, 2, 3, 4] [1, 2, 3, 4] [3, 4]  
##sharing()

#---------------------------------------------------------------
    
# Python supports two kinds of argument passing:
def arg_passing():
    def f(name, password):
        print(name, password)

    #  Positional Arguments
    f('John', 'hello')

    #  Named (or Keyword) Arguments
    f(password='123', name='Jack')
##arg_passing()
  
# 'Default Parameters' are parameters with given default values.
def default_param():
    def f(x, y = 0):
        print(x, y)
        
    f(1)            #  1 0
    f(1, 2)         #  1 2

    # Default parameters must defined from the right most to left.
    def f(a = 1, b = 1, c = 1):
      ##f(a, b = 1, c = 1):
      ##f(a, b, c = 1):
      ##f(a = 1, b, c = 1):      # error:
      ##f(a = 1, b = 1, c):      # error:
        print(a, b, c)
##default_param()

#-------------------------------------------------------------

'''
At the parameter definition:
A star * parameter indicates the end of positional parameters
after that must be keyword arguments.
'''
def single_star():
    def f(x = 0, *, a = 1, b = 2):
        print(x, a, b)
        
    f()                  	#  0, 1, 2
    f(3)                  	#  3, 1, 2
    ##f(1, 2)             	#  error
    f(1, a = 10, b = 20)        #  1 10 20
    f(a = 10, b = 20)     	#  0, 10, 20
    ##f(10, b = 20)         	#  error
##single_star()

'''
A star * may be applied to a name to indicates the parameter receives
a tuple that is collected from arguments at the position to the rest.
'''
def one_star():
    # Variable Length Arguments (Var-Arg)
    def f(*n):
        print(n)
    
    f()                  #  ()
    f('John')            #  ('John',)
    f('John', 'Jack')    #  ('John', 'Jack')

    # *<param> can be mixed with required parameters, but must be
    #  no more than one and the rightmost.
    def f(a, *n):        # 'a' is required.
        print(a, n)
    
    ##f()                #  error
    f(1)                 #  1 ()
    f(1, 2)              #  1 (2,)
    f(1, 2, 3)           #  1 (2, 3)
##one_star()

# Two stars **<param> indicates that the parameter receives a dict
#    that that is collected from keyword arguments.
def two_star():
    def f(**d):
        print(d)

    f()              #  {}
    f(a=1)           #  {'a': 1}
    f(a=1, b=2)      #  {'a': 1, 'b': 2}
##two_star()

'''
Required parameters, One and Two stars can be mixed.
 *args    is the tuple of positional arguments.
 **kwargs is the dictionary of keyword arguments.
'''
def one_two_star():
    def f(a, *args, **kwargs):
        print(a, args, kwargs)

    ##f()               #  error
    f(1)                #  1 () {}
    f(1, 2)             #  1 (2,) {}
    f(1, 2, b = 3)      #  1 (2,) {'b': 3}
    f(1, b = 2)         #  1 () {'b': 2}
    ##f(1, a = 2, 3)    #  error: keyword parameters must be right most

    ## It is easier to strict to a pattern.
    f('hello')              # hello () {}
    f('hello', 1)           # hello (1,) {}
    f('hello', 1, 2)        # hello (1, 2) {}
    f('hello', 1, 2, x=3)   # hello (1, 2) {'x': 3}
##one_two_star()

#-----------------------------------------------------------------------

'''
At the argument side when calling with *args or **kwargs prefixed argument name,
that indicates the argument value go to tuple or dict.
'''
def argument_side():
    def f(*args, **kwargs):
        print(args, kwargs)
        
    a = [1, 2]
    d = {'x': 3, 'y': 4}
    f(a)          #  ([1, 2],) {}
    f(*a)         #  (1, 2) {}
    f(d)          #  ({'x': 3, 'y': 4},) {}
    f(*d)         #  ('x', 'y') {}
    f(**d)        #  () {'x': 3, 'y': 4}
    f(a, d)       #  ([1, 2], {'x': 3, 'y': 4}) {}
    f(*a, **d)    #  (1, 2) {'x': 3, 'y': 4}
##argument_side()

#------------------------------------------------------------
