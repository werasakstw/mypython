
## Elements of a list may be listerals or variable of some type
##  which have memory overhead.
## Python array can store sequence of int or float as binary.
## So the elements are homogeneous and can be as lean as C arrays.

## When creating an array we must provide a typecode for determining
##   the underlying type of elements.
##    Type code        Type             Minimum size in bytes 
##      'b'         signed integer              1 
##      'B'         unsigned integer            1 
##      'u'         Unicode character           2
##      'h'         signed integer              2 
##      'H'         unsigned integer            2 
##      'i'         signed integer              2 
##      'I'         unsigned integer            2 
##      'l'         signed integer              4 
##      'L'         unsigned integer            4 
##      'q'         signed integer              8 
##      'Q'         unsigned integer            8 
##      'f'         floating point              4 
##      'd'         double-precision float      8 

import array
def array_test():
    ## create an array of 'b' (signed integer) with initialized value range(10)
    a = array.array('b', range(10)) 
    print(a)    ## array('b', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    ## All arrays can be indexed.
    for i in range(10):
        print(a[i], end=",")    ## 0,1,2,3,4,5,6,7,8,9,
    print()
    
    ## iterated.
    for x in a:
        print(x, end=",")       ## 0,1,2,3,4,5,6,7,8,9,
# array_test()  

## Array has methods for fast data transfer to and from a file. 
def file_test():
    size = 100
    a = array.array('H', range(size)) ## two bytes unsigned int
    
    fp = open('test.bin', 'wb')
    a.tofile(fp)
    fp.close()

    fp = open('test.bin', 'rb')
    b = array.array('b')        ## one byte signed int
    b.fromfile(fp, size)
    fp.close() 
    print(b)
# file_test()

## Memory View:
## A memorview is a shared memory of sequence type.
## memoryview.cast() allows defining how the elements are read or written,
##  it returns another memory view instance that shares the same memory.
def mv_test():
    a = array.array('b', [-2, -1, 0, 1, 2, 3])  # 1 byte signed int
    print(a.tolist())
    
    mv = memoryview(a)
    ## 1 byte unsigned int
    print(mv.cast('B').tolist())    ## [254, 255, 0, 1, 2, 3]
    
    # 2 byte unsigned int
    print(mv.cast('H').tolist())    ## [65534, 256, 770]
# mv_test()
