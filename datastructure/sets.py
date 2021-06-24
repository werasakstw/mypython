
# Set: is a collection of elements.
#   - value-oriented.
#   - mutable.
#   - elements must be hashable.
#   - non-nestable
# Sets are very efficient for set operations.
# Set is a simple approach to eliminate dupicated values.

def set_literal():
    # Set literals are enclosed in { } using , as separator.   
    print( {1, 2, 3} )

    # Set cannot contain duplicate elements
    print( {1, 2, 1} )              # {1, 2}

    # There is no empty set literal, since {} is an empty dict.
    # An empty set is created with its factory.
    print( set() )              # set()
   
    # Set cannot contain duplicate elements
    print( {1, 2, 1} )              # {1, 2}

    # Set elements be hashable e.g. number, boolean, str and tuple.
    print({1, 2.0, True, '3', True, (1,)})

    # Sets, list and dicts are not hashable and cannot be member of a set.
##    print( {1, {2}} )             # error
##    print( {1, [2]} )             # error
##    print( {1, {'x': 2}} )        # error
    
    # Tuples are hashable and can be member of a set.
    print( {1, (2, 3)} )        # {1, (2, 3)}
    
    # A comma after the last element is optional.
    print( {1, 2, 3,} )
##set_literal()

def set_create():
    # Sets can be created by set() factory.
    print(set('Hello'))         # {'l', 'o', 'H', 'e'}
    print(set(range(3)))        # {0, 1, 2}
    print(set( [1, 2, 1] ))     # {1, 2}
    print(set( (1, 2, 1) ))     # {1, 2}
    
    # Set does not support *.
    ##print({True}*3)           # error
    
    # Set can be created from comprehension.
    print( {i for i in range(3)} )   # {0, 1, 2}
##set_create()

def set_access():
    s = {'john', 'jack', 'joe'}
    # Set elements have no positions and cannot be indexed.
##    print(s[0])
    
    # Set elements can be member tested with 'in'.
    print('jack' in s)      # True

    # Set can be iterated with 'for' loop and comprehension.
    for x in s:
        print('Hello ' + x) # Hello jack
                            # Hello john
                            # Hello joe
    # Set can be iterated with enumerate() and zip().
##set_access()

def mutable_set():
    s = {1, 2, 3}

    # An element can be added to a set, if it is not already present.
    s.add(4)
    print(s)            # {1, 2, 3, 4}

    # Sets can be added to a set.
##    s.add({5})        # error

    # An element can be removed from a set.
    s.remove(3)
    print(s)            # {1, 2, 4}

    # Error if not present.
##    s.remove(3)       # error
    
    # An element can be removed from a set, if it is present.
    s.discard(4)
    print(s)            # {1, 2}

    # No error if not present.
    s.discard(4)

    # clear() removes all elements.
    s.clear()
    print(s)            # set()

    # Set can be deleted as a whole.
    del(s)
    ##print(s)                  # e
##mutable_set()

'''
                Set Operations:
Sets are very efficient for membership tests and linear time for 
union, intersection, difference, and subset.
Python supports both set methods and operators.
'''
def set_op():
    a = { 1, 2, 3 }
    b = { 3, 4 }
    print(a & b)     # intersection() {3}
    print(a | b)     # uion()         {1, 2, 3, 4}
    print(a - b)     # difference()   {1, 2}
    print(a ^ b)     # exclusive      {1, 2, 4}

    b = { 3, 1 }
    print(b <= a)    # issubset()         True
    print(a >= b)    # issuperset()       True
    print(a < a)     # is proper subset   False
    print(b < a)     #                    True
    print(a > b)     # is proper superset True
##set_op()

#------------------------------------------------------------------

''' frozenset: is immutable set.
Frozensets can be used as sets but allows only immutable operations,
Frozensets are hashable so they can be members of a set.
'''
def frozen_set():
    d = {}      # empty dict
    
    # Normal sets cannot be as a key of a dict.
##    d[ {1, 2} ] = 'hello'         # error 
    
    # A frozenset can be a key.
    fs = frozenset({1, 2})
    d[ fs ] = 'hello'
    print(d)

    # A frozenset can be a member of a set
    print( {0, fs} )
##frozen_set()

#---------------------------------------------------------------------

# PowerSet
from functools import reduce
##print(reduce(lambda a, b: a + b, range(10)))
def powerset(s):
    return reduce(lambda p, x : p + [ss | {x} for ss in p],  s, [set()])
##print(powerset({1, 2, 3})) # [set(), {1}, {2}, {1, 2}, {3}, {1, 3}, {2, 3}, {1, 2, 3}]


