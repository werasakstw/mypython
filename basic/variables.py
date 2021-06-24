''' Python is a pure object oriented language, but it spent
a lot of effort not to look like an OOP language.

Many textbooks avoid talking about OO concepts by calling:
a class as a type, and an object as a variable.

Python creats variables dynamically.
'''
def dyn_create():  # A function definition create its namespace.
    # An object is created when a name is assigned a value for the first time.
    a = 1
    
    # dir() return a list of names in the current scope.
    print(dir())  # ['a']

    # Python creates variables at runtime when the definition is executed.
    b = 2
    print(dir())  # ['a', 'b']

    # If the definition is not executed the variable is not created.
    if a > 1:
        x = 3
    else:
        y = 4
    print(dir())   # ['a', 'b', 'y']
##dyn_create()
    
''' Variable: is storage of value that can be referred to by its name.
A variable has a 'name', an 'identifier'(or address) and a 'value'.

Identifiers can be anything that used for accessing the values.
CPython uses the memory address that stores the value as an identifier.
Identifiers should not be used directly, they are useful only for checking
if values are stored at the same location.
'''
def variable():
    x = 1
    # In de-referenced context e.g. expression, 'name' is mapped to its 'value'.
    print(x)            # 1

    # In referenced context e.g. left side of assignment, 'name' is mapped to its 'identifier'.
    x = x + 1
    print(x)            # 2
          
    # id(<var>) returns 'identifier' of the <var>.
    print(id(x))        # an address

    # type(<var>) returns the type of the <var>.
    print(type(x))      # <class 'int'>
##variable()

''' A variable(object) may be either:
1. Immutable objects do not allow modification its value.
  e.g. Numbers, str and tuple.
  
2. Mutable objects allow modification its value.
  e.g. list, set, and dict.

Python assignment operator '=' modifies the identifier not value.

When an object is assigned with a new value or object, its
identifier is changed to the identifier of the assigned value.
'''
def immut_obj():
    x = 1     # 'int' is immutable.
    print(id(x), x)     # 1692706736 1
    x = 2
    print(id(x), x)     # 1692706752 2
    
    # Inplace operators return a new object.
    x += 1
    print(id(x), x)     # 1692706768 3
##immut_obj()

# Mutable objects have methods to modify its values.
def mut_obj():
    a = [0]   # 'list' is mutable.
    print(id(a), a)     # 62217640 [0]

    # Assignment as a whole changes the identifier.
    a = [1]
    print(id(a), a)     # 31185864 [1]

    # Inplace operators return the same object.
    a += [2]
    print(id(a), a)     # 31185864 [1, 2]

    # Methods that modify values do not return a new object.
    a.append(3)
    print(id(a), a)     # 31185864 [1, 2, 3]
##mut_obj()

#--------------------------------------------------------------

'''
 - Identifiers (of both immutable and mutable) can be modified.
 - An identifier may access values of any types.
 - Type is associated with a value, not the identifer or object.
'''
def dyn_type():
    x = 1     # 'x' is int.
    print(id(x), type(x))       # 1833478064 <class 'int'>

    # The result may have different type and assigned to the identifier.
    x /= 3    # Now 'x' is float.
    print(id(x), type(x))       # 48831424 <class 'float'>
##dyn_type()
    
''' So Python variables may change type dynamically. But Python is a typed
language because type checking is performed before operations.   
'''

#--------------------------------------------------------------

''' Alias: is the condition that two or more objects share the same value.
That is their identifiers point to the same location.
Assignment and parameter passing create alias.
'''
def alias():
    # For immutable object, if the shared value is modified, the alias is broken.
    x = 1
    y = x                   # 'x' and 'y' are alias.
    print(id(x) == id(y))   # True
    
    x += 1
    print(id(x) == id(y))   # False  They have thier own value.

    # For mutable object, the alias is maintained. 
    a = b = [1]
    print(id(a) == id(b))   # True
    
    a += [2]
    print(id(a) == id(b))   # True
##alias()

#----------------------------------------------------------------------

''' Literal Pool:
To keep the number of literals low, Python creates a pool to prevent
creating duplicated literals, this technique is called  'interning'.

When a literal is encountered it is checked if it is not in the pool
it is added to the pool but if it is the value is used.

Python performs interning for Number and str only.
'''
def intern():
    x, y = 1, 1
    print(id(x) == id(y))      # True

    # Other types are not interned.
    a, b = [1], [1]
    print(id(a) == id(b))      # False

    # User defined types are not interned.
    class A: pass
    a1 = A()
    a2 = A()
    print(id(a1) == id(a2))    # False
##intern()

# Interning is undocumented, different Python implementations may use
# different techniques. So it is safer to compare literals by values
# using == other than by identifiers using 'is'.

# Static intern is performed if the value is known at compile time.
# Those values that created at runtime are not interned.
def static_intern():
    a = 1.0
    b = 0.5 + 0.5           # performed at compile time.
    print(id(a) == id(b))   # True

    s = 'Hello'
    v = 'He' + 'llo'        # performed at compile time.
    print(id(s) == id(v))   # True
    
    w1 = 'He'
    w2 = 'llo'
    w = w1 + w2             # performed at runtime
    print(id(s) == id(w))   # False
##static_intern()
    
#----------------------------------------------------------------

''' Python supports two kinds of comparisons.
  1. == and != compares values.
        x == y is True, if x and y have the same values.

  2. 'is' and is not' compares identifiers.
        x is y is True, iff id(x) == id(y)
'''
def comparison():
    # interned
    x = 1
    y = 1
    print(x == y, x is y)   # True True
    # created at runtime
    z = (x+y)/2
    print(x == z, x is z)   # True False

    # not interned
    a = [1, 2]
    b = [1, 2]
    print(a == b, a is b)    # True False

    # Set is value-oriented.
    x = {1, 2}
    y = {2, 1}
    print(x == y, x is y)    # True False

    # 'n is not m' is the same as 'not n is m' but more reable.
    n, m = 1, 2
    print(n is not m, not n is m)      # True True
    # 'is' cannot be used with !.
##comparison()

#-------------------------------------------------------------

''' Object Copy:
There is no reasons to make a copy of immutable objects.
Immutable types have no copy().
It is more efficient to alias immutable objects.
'''
def factory_copy():
    # Factory methods of immutable objects return the same object.
    x1 = 1
    x2 = int(x1)
    print(x1 is x2)         # True
     
    y1 = 'Hello'
    y2 = str(y1)
    print(y1 is y2)         # True

    t1 = (1, 2)
    t2 = tuple(t1)
    print(t1 is t2)         # True

    # Factory methods and copy() of mutable objects returns a new object.
    a1 = [1, 2]
    a2 = list(a1)
    a3 = a1.copy()            # Try: a1[:]
    print(a1 is a2, a1 is a3) # False False
    
    s1 = {1, 2}
    s2 = set(s1)
    s3 = s1.copy()
    print(s1 is s2, s1 is s3) # False False
    
    d1 = {'a':1}
    d2 = dict(d1)
    d3 = d1.copy()
    print(d1 is d2, d1 is d3) # False False
##factory_copy()

# Shallow Copy VS Deep Copy:
def shallow_deep():
    # Shallow copy bitwisely copies only the top level of value.
    # copy() is shallow copy.
    a = [1, [2]]
    b = a.copy()
    print(a, b)			# [1, [2]], [1, [2]]
    a[1].append(3)
    print(a, b)			# [1, [2, 3]], [1, [2, 3]]

    # Deep copy copies all levels of the value.
    # copy.deepcopy() is deep copy.
    import copy
    a = [1, [2]]
    b = copy.deepcopy(a)
    print(a, b)			# [1, [2]], [1, [2]]
    a[1].append(3); 	
    print(a, b)     		# [1, [2, 3]] [1, [2]]
##shallow_deep()

