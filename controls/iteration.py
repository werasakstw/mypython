'''
Iterations are loops that repeatedly doing something.

'while' loop is an undeterministic iteration that means
the termination cannot be predetermined.

'while' loop executs the <body> as long as the <condition> is true.
               while <condition>:
                   <body>

<condition> is a boolean expression that may contain:
     Logical operations:   and, or, not
     Comparison operations: <, ==, !=, >, <=, >=
So 'while' loops offer flexible and general termination controls.
'''
def while_loop():
    i = 0
    while i < 5:
       print(i, end=',')
       i = i + 1
##while_loop()                #  0,1,2,3,4,

# Ex. To print digits of an integer in reverse order.
# We use 'while' loop since 'n' can be any digits number.
def rev_digits(n): 
    while n > 0:
        print(n % 10, end=',')
        n //= 10
##rev_digits(1234)          #  4,3,2,1,

#-----------------------------------------------------------------

''' 'for' loop is a deterministic iteration.
               for <item> in <iterable>:
                   <body>        
'for' loop performs iteration for each <item> in the <iterable>.
str, list, tuple, set, dict, and range() are iterable.

'for' and 'while' loops may be nested.
'''
def nested():
    for i in ['a', 'b']:
        for j in [1, 2, 3]:
            print('(%s,%d)' % (i, j), end=' ')
##nested()        # (a,1) (a,2) (a,3) (b,1) (b,2) (b,3) 

'''
'while' loop tests the <condition> before the first iteration.
Python does not have 'repeat until' nor 'do while'.
'''
def skip_test():
    # 'break' allows skipping the rest of iteration.
    for i in range(5):
        if i == 2:
            break
        print(i, end=',')       # 0,1,
    print()
    
    # 'continue' allows skipping the rest of the loop and
    # continues the next iteration.
    for i in range(5):
        if i == 2:
            continue
        print(i, end=',')       # 0,1,3,4,
##skip_test()

#---------------------------------------------------------

''' Python allows 'else' block for 'while' and 'for' loops.
   while <condition>:          for <item> in <iterable>:
       <body>                       <body>
   else:                       else:
       <else body>                  <else body>
<else body> will be executed if the iteration terminates normally
but not executed if the iteration aborted abnormally.
Abnormal abortion may be 'break', 'return', an exception, and
sys.exit(), but not include 'continue'.
'''
def else_loop():
    a = [1, 2, 3]
    while a:
        print(a.pop(), end=',')  
    else:
        print('Else') 
                                #  3,2,1,Else

    for x in [1, 2, 3]:
        print(x, end=',')
    else:
        print('Else')           #  1,2,3,Else
# else_test()

# A reason to have this feature is to perform an action once the 
#  iteration ends normally, but not if ends abnormally.
# A use case is searching an item in a list.
def lookup_list(x, a):
    for i in a:
        if i == x:
            print('Found at:', i)
            break
    else:
        print('Not Found')
##lookup_list(4, [1, 2, 3])          #  Not Found
##lookup_list(2, [1, 2, 3])          #  Found: 2
# But the same logic could be easily implemented with an extra boolean.

#---------------------------------------------------------

'''                     Comprehension
'while' and 'for' loops are statements.
Comprehension is an iteration expression.
     <expression> for <item> in <iterable> if <condition>

All 'iterable' objects that can be iterated. e.g.
range(), str, list, tuple, set, and dict.
'''
# Ex. To compute a list of n**2 where n is even in range(10).
def comprehension():
    # Using 'for' loop.
    a = []
    for n in range(10):
        if n % 2 == 0:
            a.append(n**2)
    print(a)                        # [0, 4, 16, 36, 64]
    
''' Using comprehension.
<expression> defines what to do with each element before collect to the result.
'if <condition>' is a filter, if true the element will be processed to the result.
'''
    print([n**2 for n in range(10) if n % 2 == 0]) # [0, 4, 16, 36, 64]
## comprehension()

# 'if <condition>' is optional, if not present all elements will be processed.
##print([x**2 for x in range(5)])           ## [0, 1, 4, 9, 16]

# <expression> may be <key>:<value> to define elements of dict as the result.
grades = ['D', 'A', 'C', 'B', 'F', 'C', 'C', 'B']
##print({g:grades.count(g) for g in grades})
                        ## {'D': 1, 'A': 1, 'C': 3, 'B': 2, 'F': 1}

# <item> defines how to match elements in the <iterable>.
##print([a+b for (a, b) in [(1,2),(3,4),(5,6)]])  # [3, 7, 11]
##print({x:v for (x, v) in zip([1, 2, 3], ['a', 'b', 'c'])})  # {1: 'a', 2: 'b', 3: 'c'}

'''
Multiple comprehensions are faster than multiple 'for' loops.
Comprehension does not create a new block.
Comprehension can be nested and does not need indentations.
But line saparation improves readability.
'''
##print([(x, y) for x in [1, 2]
##              for y in ['a', 'b']])
        # [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]

'''
The result of comprehension may be:
   A list if enclosed with [].
   A set or dict if enclosed with {}.
A dict result must be enclosed with {} and <expression> is <key>:<value>.
A comprehension cannot result a tuple. 
Enclosing comprehension with () results a 'generator', not a tuple.
'''
##print([x for x in 'Hello'])             #  ['H', 'e', 'l', 'l', 'o']
##print({x for x in 'Hello'})             #  {'o', 'H', 'l', 'e'}
##print({x:x.isupper() for x in 'John'})  #  {'J': True, 'o': False, 'h': False, 'n': False}

#-----------------------------------------------------------------

# Comparing performance between 'for' loop and comprehension.
# To create a large list filled with numbers.
from time import perf_counter as pc
def performance_test():
    r = range(10**7)
   
    ## Using 'for' loop.
    start = pc()
    a = []
    for i in r:
        a.append(i)
    stop = pc()
    print(stop - start)

    ## Using comprehension.
    start = pc()
    b = [i for i in r]
    stop = pc()
    print(stop - start)
##performance_test()

