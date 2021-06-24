''' Range: is a generator, not a list.
A generator does not have its elements but creates and returns one at time.
A range returns a sequence defined by: <start>, <stop>, <step>
'''
def range_ex():
    r = range(3)
    print(r, type(r))       # range(0, 3) <class 'range'>

    # A list can be created from a range using factory.
    print(list(r))          # [0, 1, 2]

    # [<start>, <stop>, <step>)  Begins from <start> and ends before <stop>.      
    # Default <start> is 0.
    # Default <step> is 1.
    # <stop> must be specified, no default.
    print(list(range(3)))           # [0, 1, 2]
    print(list(range(1, 3)))        # [1, 2]
    print(list(range(1, 10, 3)))    # [1, 4, 7]
##range_ex()
    
#--------------------------------------------------------------------

# List: is a sequence of elements.
# A list has memory to store its elements.
#   - order-oriented.
#   - mutable.
#   - generic (elements may be any types).
#   - nestable

def list_literal():
    # List literals are enclosed in [ ] using , as separator.
    a = [1, 2, 3]
    print(a, type(a))           # [1, 2, 3] <class 'list'>

    # Empty list literal is [] or may be created using its factory.
    print( [], list() )         # [] []

    # List may contain duplicate elements since they are order-oriented.
    print( [1, 2, 1] )

    # Lists are generic and nestable.
    print([1, 2.0, '3', True])
    print([1, [2, 3]])

    # A comma after the last element is optional.
    print([1, 2, 3,])           # [1, 2, 3]
    
    # That allows listing elements in separated line with the last
    #  element may or may not has a comma.
    print([ 'John',
            'Jack',
            'Joe',  # Always end with , for consistency.
         ])                     # ['John', 'Jack', 'Joe']
##list_literal()

def list_create():
    # List can be created by its factory from a str, range(), list, tuple or set.
    print(list('Hello'))        # ['H', 'e', 'l', 'l', 'o']
    print(list(range(3)))       # [0, 1, 2]
    print(list( [1, 2, 1] ))    # [1, 2, 1]
    print(list( (1, 2, 1) ))    # [1, 2, 1]
    print(list( {1, 2, 1} ))    # [1, 2]

    # List can be created with initialized value using * (repeat opertor).
    print([True]*3)             # [True, True, True]

    # List can be created with comprehension.
    print( [i*i for i in range(5)] )   # [0, 1, 4, 9, 16]
##list_create()

#-----------------------------------------------------------------

# List lelements can be accessed with indexing.
# List elements are accessed by 'index' operator:
#          <list>[<position>}
def list_access():
    a = [1, 2, 3, 4]
    # The first position is 0.
    print(a[0])             # 1

    # Index out of bounds are checked at runtime.
##    print(a[5])             # error

    # Negative index starts from the last position.
    print(a[-1])            # 4

    # Lists can be member tested with 'in' opertor.
    print(1 in a, 5 in a)   # True False
##list_access()

# Ranges and lists can be iterated with 'for' loop and comprehension.
def list_iterate():
    for x in range(5):
        print(x, end=',')   # 0,1,2,3,4,
    print()
    
    a = ['john', 'jack', 'joe']
    for x in a:
        print('Hello ' + x)   # Hello john
                              # Hello jack
                              # Hello joe
    
    [print('Hi ' + x) for x in a]  # Hi john
                                   # Hello jack
                                   # Hello joe

    ## Since Pyton 3.8 there is a new form of 'for'.
    for i in 2, 1, 3:
        print(i, end=',')   # 2,1,3
    print()

    # enumerate() provides index and element.
    for i, x in enumerate(a):
        print(i, x)         # 0 john
                            # 1 jack
                            # 2 joe
    # zip() allows parallel iteration of more then one lists.
    b = ['rambo', 'ripper', 'green']
    for x in zip(a, b):     # ('john', 'rambo')
        print(x)            #('jack', 'ripper')
                            #('joe', 'green')

    #  zip() stops when the shortest sequence is done.
    for i in zip([1, 2, 3], [4, 5]):
        print(i, end=',')   # (1, 4),(2, 5),

    #  zip() can be nested
    for i in zip(zip([1, 2, 3], [4, 5, 6]), [7, 8, 9]):
        print(i, end=',')   # (1, 4),(2, 5),((1, 4), 7),((2, 5), 8),((3, 6), 9),

    # reversed() applicable to order-oriented sequence e.g. str, list and tuple.
    for i in reversed('abc'):
        print(i, end=',')   # 'c', 'b', 'a
##list_iterate()

# Lists are mutable.
def mutable_list():
    a = ['a', 'b', 'c']
    
    # Modify element.
    a[1] = 'x'
    print(a)            # ['a', 'x', 'c']
      
    # Modify the whole (change identifier).
    a = ['a', 'b']
    print(a)            # ['a', 'b']

    # + operor is for list concatenation.
    a += ['c']
    print(a)            # ['a', 'b', 'c']

    # Delete an element at position.
    del a[1]
    print(a)            # ['a', 'c']

    # Clear all elements.
    a.clear()
    print(a)            # []

    # Delete the whole.
    del a;
##    print(a)          # error
##mutable_list()

#------------------------------------------------------------------

                    # List Operations:
def list_op():
    a = ['a', 'b']

    # <list>.append(<item|list>) add to the end.
    a.append(1)
    print(a)                    # ['a', 'b', 1]
    a.append([2, 3])
    print(a)                    # ['a', 'b', 1, [2, 3]]

    # <list>.extend(<list>) or += combines two lists.
    a.extend([1, 2])
    print(a)                    # ['a', 'b', 1, [2, 3], 1, 2]    

    # <list>.insert(<pos>,<item>) insert <item> before <pos>.
    a.insert(1, 'x')
    print(a)                    # ['a', 'x', 'b', 1, [2, 3], 1, 2]

    # <list>.remove(<item>) remove the first occurrence of <item>.
    a = ['a', 'x', 'b', 'x']
    a.remove('x')
    print(a)                    # ['a', 'b', 'x']

    # <list>.pop(<pos>) pop element at <pos> and returns the element.
    #   default <pos>: is -1 (the end).
    print(a.pop(), a)               # x ['a', 'b']
    print(a.pop(0), a)              # a ['b'] 
##list_op()

#---------------------------------------------------------------------

#                       State spaces
# Cartential Product
def cart_pro():
    print([(a,b) for a in [1, 2, 3] for b in [4, 5]])
        ## [(1, 4), (1, 5), (2, 4), (2, 5), (3, 4), (3, 5)]
    
    print([(a,b) for a in 'abc' for b in 'de'])
        ## [('a', 'd'), ('a', 'e'), ('b', 'd'), ('b', 'e'), ('c', 'd'), ('c', 'e')]
##cart_pro()

def select():
    seq = range(10)

    # choice(<seq>) returns a randomly selected element from the <seq> independently.
    print(choice(seq))

    # sample(<seq>, n)) returns randomly selected n elements from the <seq> independently. 
    print(sample(seq, 4))

    # shuffle(<seq>) in place randomly shuffles the <seq>.
    a = [1, 2, 3, 4, 5]     ## range does not support shuffle.
    shuffle(a)
    print(a)
##select()
    
# Brute Force Permutation
def permuteBF():
    a = [1, 2, 3]
    return  [ print(x, y, z)
                for x in a
                for y in a if y != x
                for z in a if z not in [x, y]]
##permuteBF()

# Recursive Permutation
def _permuteR(a, i):
    def swap(i, j):
        a[i], a[j] = a[j], a[i]     ## tmp = a[i]; a[i] = a[j]; a[j] = tmp

    if i == len(a):
        print(a)
    else:
        j = i
        while j < len(a):
            swap(i, j)
            _permuteR(a, i+1)
            swap(i, j)
            j += 1

def permuteR(a):
    _permuteR(a, 0)
##permuteR([1, 2, 3])

import itertools as it
def permutation():
    print([p for p in it.permutations('abc')])
        ## [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]

    print([p for p in it.permutations([1, 2, 3])])
        ## [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

    # permutations() allows duplicated elements.
    print([p for p in it.permutations([1, 2, 1])])
        # [(1, 2, 1), (1, 1, 2), (2, 1, 1), (2, 1, 1), (1, 1, 2), (1, 2, 1)]
    
    ## Permutation with limit positions.
    print([p for p in it.permutations([1, 2, 3], 2)])
        ## [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
    
    print([p for p in it.combinations([1, 2, 3], 2)])    ## where (x, y) == (y, x)
        ## [(1, 2), (1, 3), (2, 3)]

    print([p for p in it.combinations_with_replacement([1, 2, 3], 2)])
        ## [(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]

    print([p for p in it.product([1, 2, 3], repeat=2)])   ## to itself
        ## [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
##permutation()




