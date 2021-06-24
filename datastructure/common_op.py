

st = 'abc'                  ## str
l = [0, 1, 2]               ## list
t = (0, 1, 2)               ## tuple
s = {0, 1, 2}               ## set
d = {'a':0, 'b':1, 'c':2}   ## dict

## Python has builtin functions for sequence types.

## 'in' returns True if the first operand occurs in the second operand,
##   applicable to all sequence types.
##print('b' in st, 1 in l, 1 in t, 1 in s, 'b' in d)

## max() and min() applicable to all sequence types.
##print(max(st), max(l), max(t), max(s), max(d))
##print(min(st), min(l), min(t), min(s), min(d))

## len() returns number of elemenmts, applicable to all sequence types.
##print(len(st), len(l), len(t), len(s), len(d))

##  '+' is append operator.       '*' is repeate operator.
## Applicable to str, list and tuple, but not set nor dict.
##print(st+st, l+l, t+t)
##print(st*3, l*3, t*3)

## <seq>.count(<item>) is a method of str, list, and tuple 
##    which returns the number of occurrence of the <item> in <seq>.
##print(st.count('b'), l.count(1), t.count(1))

## <seq>.index(<item>) is a method of str, list, and tuple 
##    which returns the position of the <item> in <seq>.
##print(st.index('a'), l.index(1), t.index(1))

## index() raises ValueError when the <item> is not found.
##print(st.index('ac'), l.index(3), t.index(3))     ## error

#-------------------------------------------------------------

## Indexing:  Not applicable to set.
## List and tuple can be indexed with position.
## Dict can be indexed with key.
def indexing():  
    ## Negative index counts from the last, which is -1.
    ## An exception is throwed when index out of bound.
    print(st[-1], st[1], l[-1], t[-1], l[0], t[0])  ## c b 2 2 0 0

    ## Nested Indexing: applicable to list/tuple and dict.
    a = [0, [1, 2]]
    print(a[1], a[1][0])        ## [1, 2] 1

    d = {'a':1, 'b':{'x':2, 'y':3} }
    print(d['b'], d['b']['x'])  ## {'x': 2, 'y': 3} 2
##indexing()

#-----------------------------------------------------------

## Slicing:
##      <seq>[<start>:<end>:<step>] is 'sclice' operator
##  which extracts elements in the <seq>.
##Applicable to order-oriented types str, list, and tuple, not set and dict.
def slicing():
    a = '0123456789'
    
    ## <start>: to the end
    print(a[1:])       ## 123456789
    
    ## :<stop>  from the beginning
    print(a[:3])        ## 012     First three.

    ## Negative begin starts from the last.
    print(a[-2:])       ## 89     Last two

    ## <start>:<stop>  [<start>, <stop>)
    print(a[1:5])       ## 1234

    ## Negative stop starts from the last. 
    print(a[3:-3]) 	## 3456   Middle four

    ## <start>:<stop>:<step>
    ## default <start> is 0, default<stop> is len(a), default <step> is 1.
    print(a[::])        ## 0123456789  The whole
    print(a[::2])       ## 02468  Even positions
    print(a[1::2])      ## 13579  Odd positions
##slicing()

#-------------------------------------------------------------

## Iteration:
## Range, str, list, tuple, set, and dict can be iterated
##   by for loop and comprehension.
def iteration():
    print([e for e in st])      ## ['a', 'b', 'c']

    ## Dict iterations:
    print([e for e in d])           ## ['a', 'b', 'c']
    print([e for e in d.items()])   ## [('a', 0), ('b', 1), ('c', 2)]
    print([k for k in d.keys()])    ## ['a', 'b', 'c']
    print([v for v in d.values()])  ## [0, 1, 2]
##iteration()

