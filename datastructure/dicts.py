
# Dict: (Hash Table) is a collection <key>:<value> pairs.
#   - value-oriented.
#   - mutable.
#   - <key> must be hashable (immutable) and no duplicate.
#   - <value> can be any object.
#   - non-nestable.
# Dict are very efficient for lookup, insert, update, and delete operations.

def dict_literal():
    # Dict literals are enclosed in { } using ',' as separator.
    print( { 'id': 1,
             'name': 'John Rambo',
             'gpa': 1.8 } )

    # Empty Dict.
    print( {}, dict() )

    # Dict element values can be number, str, list, tuple, set and dict.
    print( {
        'id': 2,
        'name': 'Jack Ripper',
        'take_courses': [ 'oop', 'alg' ],
        'email': ( 'jack@ripper.com', ),
        'clubs': { 'football', 'guitar' },
        'info': { 'age': 25, 'weight': 80 },
    })
##dict_literal()

def dict_create():
    # Dict can be created from list or tuple (but not a set).
    print( dict([ ['id', 2],
                  ('name', 'Joe Green'),
                  ('gpa', 2.0) ]) )

    # Dict can be created from two lists with zip(). 
    k = ['a', 'b', 'c']
    v = [1, 2, 3]
    print(dict(zip(k, v)))      # {'a': 1, 'b': 2, 'c': 3}

    # Dict can be created with comprehension.
    print( {x: x * x for x in range(5)} )  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
##dict_create()

def dict_access():
    # Dict elements are accessedd by indexed with the element's key.
    d = { 'x': 1, 'y': 2 }
    print(d['x'])           # 1

    # Indexing with non-exist key is an error.
    ##print(d['z'])          # error

    # get() does not cause error and allows returning default value.
    print(d.get('z'), d.get('z', 0))   # None 0
##dict_access()

# Dicts are mutable:
def mutable_dict():
    d = {'x': 1}

    # Add new element
    d['y'] = 2
    print(d)                # {'x': 1, 'y': 2}

    # Replace an element
    d['x'] = 0
    print(d)                # {'x': 0, 'y': 2}

    # Delete an element
    del d['y']
    print(d)                # {'x': 0}

    # Update element value
    d['x'] += 1.0
    print(d)	            # {'x': 1.0}

    # Update a dict with another dict.
    a = { 'x': 1, 'y': 2 }
    b = { 'y': 3, 'z': 4 }
    a.update(b)
    print(a, b)     # {'x': 1, 'y': 3, 'z': 4} {'y': 3, 'z': 4}

    # Dict can be cleared.
    a.clear()
    print(a)         # {}

    # Dict can be deleted as a whole.
    del(a)
    ##print(a)                  # error
##mutable_dict()

def dict_iteration():
    d = {'a':0, 'b':1, 'c':2}

    # If a dict is iterated, only the keys are obtained.
    for k in d:
        print(k, end=",")       #  a,b,c,
    print()
    
    # Since Python 3.0, keys(), values(), and items() do not return a list.
    # keys() returns a dict_keys which is an iterable view of the keys.
    print(type(d.keys()))       #  <class 'dict_keys'>
    
    # A list can be created from a iterable view.
    print(list(d.keys()))       #  ['a', 'b', 'c']

    # Mostly we explicitly iterate the iterable view of keys.
    for k in d.keys():
        print(k, end=",")       #  a,b,c,
    print()

    # values() returns iterable view of values.
    for v in d.values():
        print(v, end=",")       #  0,1,2,
    print()

    # items() returns iterable view of items represented as tuple.
    for i in d.items():
        print(i, end=",")       #  ('a', 0),('b', 1),('c', 2),
##dict_iteration()

#-------------------------------------------------------------------

'''
Multiset is a set that allows elements to have more than one occurrence.
It is implemented as a dict with item of <value>:<number of occurrence>.
'''
import collections
def counter_test():
    c = collections.Counter()
    c.update({'A': 1, 'B': 3, 'C': 5})
    print(c)        # Counter({'C': 5, 'B': 3, 'A': 1})
    c.update({'B': 1, 'C': 2, 'F': 2})
    print(c)        # Counter({'C': 7, 'B': 4, 'F': 2, 'A': 1})

    # Unique elements,  Total number of elements  
    print(len(c), sum(c.values()))  # 4 14

    ## Counter is applicable to str, list, tuple, and set.
    for k,v in collections.Counter('Hello').items():
        print('%s(%d)' % (k, v), end=' ') ## H(1) e(1) l(2) o(1)
    print()

    ## Anagrams are strings that contain the same set of characters.
    print(collections.Counter('night') == collections.Counter('thing')) ## True
##counter_test()

def ordered_dict():
    # Since Python 3.6, dict instances preserve insertion order of keys.
    d = { 'john':1, 'jack': 2 }
    d['joe'] = 3
    print(d)   # {'john': 1, 'jack': 2, 'joe': 3}
    
    od = collections.OrderedDict(john=1, jack=2)
    od['three'] = 3
    print(od) # OrderedDict([('john', 1), ('jack', 2), ('three', 3)])
##ordered_dict()

def default_dict():
    # Accessing non-exist key of a dict results an error.
    d = { 'john':1 }
##    print(d['jack'])  # error

    dd = collections.defaultdict(list)
    dd['cs'].append('john')
    print(dd['ce'])     # []
    print(dd['cs'])     # ['john']
    # Here a list is used to store values of the same key.
    dd['cs'].append('jaxk')
    print(dd)   # defaultdict(<class 'list'>, {'cs': ['john', 'jaxk'], 'ce': []})
##default_dict()
    
def chain_map():
    d1 = { 'john': 1, 'jack': 2 }
    d2 = { 'jack': 3, 'joe': 4 }

    # Chain two or more dict to be searched at once.
    cd = collections.ChainMap(d1, d2)
    print(cd)    # The first occurence value is returned.
    print(cd['jack'], cd['joe']) # 2 4
##chain_map()

import types
def read_only_dict():
    d = { 'john': 1, 'jack': 2 }
    
    # A wrapper for read only view.
    rod = types.MappingProxyType(d)
    print(rod['jack'])          # 2

    # Item modification is not allowed.
##    rod['jack'] = 3           # error

    # Adding more item is not allowed.
##    rod['joe'] = 3           # error

    # The original is still mutable.
    d['joe'] = 3
    print(rod)          # {'john': 1, 'jack': 2, 'joe': 3}
##read_only_dict()

