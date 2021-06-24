
'''

'For' loop is lazy in the sense that elements are processed one at a time
    and leaves result as side effect.

Comprehension is eager since all elements are processed and collected before
returning as the result, that called 'as a whole'.
   Ex. reading a large file into a list is not a good idea.
 
A 'generator' is an object that returns elements one at a time.
A generator does not store all elements but creates(or fetched from somewhere)
and returns one at a time.
A generator uses less memory and be more efficient to copied or passed.

A generator is created by an expression syntax similar to conprehension
but surrounded by (), this is called 'conprehension generator'.
'''
def generator():
    g = (x for x in range(5))
    print(type(g))          #  <class 'generator'>

    # Generators can be used for iteration and comprehension.
    for i in g:
        print(i, end=',')   #  0,1,2,3,4,
    print()

    # Just like comprehensions, a 'comprehension generator' can be used only once.
    # It will run out off elements after its first iteration.
    print([x for x in g])   #  []
    
    # Factory functions may create the whole sequence from a generator.
    print(list((x for x in range(5))))          #  [0,1,2,3,4]
##generator()

''' Generator Iteration:
next() is a built-in function for requesting elements of a generator one at a time.
There is no ways to check for how many elements lefted.
A StopIteration error is raised if next() is called when run out off elements.
''' 
def generator_iter():
    g = (x for x in range(5))
    try:
        while True:
            print(next(g), end=',')
    except Exception as e:
        print(type(e))

    # 'for' loops and comprehensions internally handled next() and StopIteration.
    g = (x for x in range(5))
    for x in g:
        print(x, end=',')
##generator_iter()

'''
Alternatively a generator can be created by a function, called
'function generator' which is a function that sends out a value with 'yield'.
'yield' does not terminate the function's execution, just temporarily
halts the execution until the next() is called and execution resumes.  
'''
def my_range(first, last, step=1):
    i = first
    while i < last:
        yield i
        i += step

##print([x for x in my_range(1, 5)])  #  [1, 2, 3, 4]

def nest_iteration():
    # A comprehension generator cannot be reused.
    # So it cannot be reused in nested iteration properly.
    g = (i for i in [0, 1])
    print([(x, y) for x in g
                  for y in g])	    #  [(0, 1)]

    # A generator function creates its namespace each time it is called.
    # It is easier to be used in nested iteration.
    print([(x, y) for x in my_range(0, 2)
                  for y in my_range(2, 5)])
            #  [(0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (1, 4)]
##nest_iteration()

'''
It is not possible to create an infinite sequence.
But function generators may create more elements until some condition is true.
'''
def inf_seq():
    def seq(first):
        n = first
        while True:
            yield n
            n += 1

    # The user must terminate the sequence at a specified value.
    for i in seq(1):
       if i == 5:
           break
       print(i, end=",")    #  1,2,3,4,
##inf_seq()

'''
A generator lazyly create elements one at a time, not as a whole.
An element is not created until it is requested.
'''
def lazy():
    def gen():
        print('one', end=',')
        yield 1
        print('two', end=',')
        yield 2

    # 'for' loops internally call next() to request value one at a time.
    for i in gen():
        print(i, end=',')       #  one,1,two,2,
    print()

    # Comprehension generator lazily craetes element one at a time. 
    for i in (i for i in gen()):
        print(i, end=',')       #  one,1,two,2,
    print()
    
    # Comprehension eagerly creates all elements and returns as a whole.
    c = [i for i in gen()]      #  one,two
    print(c)                    #  [1, 2]
##lazy()

#-------------------------------------------------------------------------

'''
Generators may be used as stateful functions.
A stateful function may behaves like an object.
Ex. Factorial
           fac(n) = 1*2*3*...(n-1)*n
'''
def facorial():
    #  Factorial Function starts over from 1 every time.
    def fac(n):
        r = 1
        for i in range(2, n+1):
            r *= i
        return r

    #  Factorial Generator return a result one at a time.
    def facg():
        r, i = 1, 0
        while True:       
            i += 1  
            yield r
            r *= i
       
    f = facg()
    for i in range(10):
        print(i, fac(i), next(f))
##facorial()

#  Ex. A non repeated random numbers generator may keep a set of numbers that already had been generated.
import random
def random_generator():
    def ran(n):   
        s = set()
        while len(s) < n:
            r = random.randint(1, n)
            if r not in s:
                s.add(r)
                yield r
        yield None

    r = ran(10)
    for _ in range(10):
        print(next(r), end=',')     #  6,2,3,10,1,4,7,5,8,9,
##random_generator()

#--------------------------------------------------------------------------

'''
A coroutine is a function with
               <variable> = yield <expression>
which suspends the execution and sends <expression> to the caller.
The caller must call next() to proceeds to the first 'yield', this is called 'priming'.
Then the caller may call send(<value>) then the coroutine resumes execution and
the <variable> is assigned with the <value>.
Calling send() when there is no next 'yield' will raise a StopIteration.
'''
def cor():
    print('start')
    x = yield 1
    print('x = ', x)
    y = yield 2
    print('y = ', y)
        
def cor_test():
    try:
        r = cor()                  # No execution yet.
        print(next(r))             # 'start'  and proceeds to the first 'yield'
                                   # 1 
        print(r.send('hello'))     # x =  hello
                                   # 2
        print(r.send('hi'))        # y =  hi
    except StopIteration as e:
        print(type(e))             # <class 'StopIteration'>
##cor_test()

# A coroutine may be closed as needed when the caller calls close().
def close_test():
    c = cor()
    print(next(c))              #  start
                                #  1
    print(c.send('hello'))      #  x =  hello
                                #  2
    c.close()
##close_test()

'''
Generators may send data to the caller only.
Coroutine, data can be sent both ways.
'''
def both_ways():
    def inc(first=0):
        n = first
        while True:
            n += 1
            cmd = yield n
            if cmd == 'stop':
                break
        yield None

    # Caller
    s = inc()
    i = next(s)             #  Priming.
    while True:
        print(i, end=',')
        i = s.send('more')
        if i > 10:
            s.send('stop')
            break
##both_ways()

