'''
There are many things that must perform 'post operation' e.g. close(), delete(),
reset() after they had been used unless the results would be devastating.
Ex. Most of IO streams, e.g. file and socket must be properly closed.
'''
def bad_read(fname):
    f = open(fname, 'r')
    print(f.read())  #  If an exception occurs here the file would not be closed.
    f.close()
##bad_read(__file__)

'''
Acessing files should be in a 'try' block since a lot of things could go wrong
and close() should be in its 'finally' block to ensure that it would be executed.
But closing a None file reference is an error, so we need a checking.
That is a big boilerplate for using files.
'''
def read_file(fname):
    try:
        f = open(fname)
        print(f.readline())
    except Exception as exc:
        print(exc)
    finally:
        if f is not None: 
            f.close()

##read_file(__file__)
##read_file('x.txt')          # error: No such file or directory: 'x.txt'

'''
Pyton provides 'with' statement that supports Context Manager.
     with <expression> as <reference>:
         <body>
A context manager sets up a scope where an object can be created and used
then at end of the scope the object is automatically closed.

<expression> is executed to create an object that is referred by the
<reference> which can be used in the <body>. Then at the end of the <body>
the object's close() will be called.
'as' is optional, in case the object does not needed to be referred to.
'''
def with_statement(n):
    try:
        with open(n, 'r') as f:
            print(f.readline())
    except Exception as exc:
        print(exc)
##with_statement(__file__)

'''
The object created by <expression> is called a 'context manager'.
A context manager creates an object to be managed called 'managed object'.

A context manager must have:
   __enter__() to create and return a managed object to the <reference>.
   __exit__() to delete or close the managed object.
   
When the <body> terminates, the context manager's __exit__() is invoked.
'''
def ctx_mgr_test():
    #  For simplicity, here the 'Hello' str is the managed object.
    class ctx_mgr:
        def __enter__(self):
            print('enter', end=',')
            return 'Hello'
        def  __exit__(self, exc_type, exc_value, traceback):
            print('exit', end=',')

    with ctx_mgr() as t:
        print(t, end=',')       #  enter,Hello,exit,
##ctx_mgr_test()

#  Managed Object and Context Manager:
def mg_obj_test():
    class mg_obj:
        def __init__(self, ctx):  #  ctx is the context manager.
            self.ctx = ctx
            print('init', end=',')
        def do_something(self):
            print('do_something', end=',')
        def __del__(self):  #  __del__() is executed when the object is deleted.
            print('del', end=',')

    class ctx_mgr:
        def __enter__(self):
            print('enter', end=',')
            self.ins = mg_obj(self) #  managed object is created.
            return self.ins
        def __exit__(self, exc_type, exc_val, exc_tb):
            print('exit', end=',')
            #  The managed object is implicitly deleted.
    
    with ctx_mgr() as mo:
        mo.do_something()  #  enter,init,do_something,exit,del,
##mg_obj_test()

'''
Python has 'TextIOWrapper' for context manager that is created by open().
     __enter__() returns the opened stream.
     __exit__() closes the stream.
'''
def file_mgr_test():
    class file_mgr():
        def __init__(self, fname):
            self.fname = fname
        def __enter__(self):
            self.file = open(self.fname, 'r')
            return self.file
        def __exit__(self, exc_type, exc_val, exc_tb):
            if self.file:
                self.file.close()
                
    with file_mgr(__file__) as f:
        print(f.readline())
##file_mgr_test()

'''
Creating a class is more troublesome than a function.
Alternaively we can to create a context managers from a coroutine function.
The function must be decorated with @contextlib.contextmanager.
The function must have a 'yield' that produces whatever the __enter__() return.
 The code before 'yield' will be executed as in __enter__().
 The code after 'yield' will be executed as in __exit__().
'''
import contextlib
def coroutine_ctx(): 
    @contextlib.contextmanager
    def file_mgr(name):
        try:
            f = open(name, 'r')
            yield f
        finally:
            f.close()
            
    with file_mgr('08_ctx_mgr.py') as f:
        print(f.readline())
##coroutine_ctx()

'''
If the managed object just returns a result. The managed object and
the context manager can be combined into a coroutine function.
'''
def hello_mgr():
    @contextlib.contextmanager
    def hello(name):
        print('enter' , end=', ')   #  Do what __enter__() do
        yield "Hello " + name       #  Return a result
        print('exit' , end=', ')    #  Do what __exit__() do

    with hello('John') as result:
        print(result, end=', ')     #  enter, Hello John, exit,
##hello_mgr()

'''
In case we already have a class to a managed object with
 __init__() that can be used as __enter__().
 close() that can performs as __exit__().
Its context manager can be created with the help of a wrapper.
     contextlib.closing(<managed object>)
'''
def wrapper_mgr():
    class Hi:
        def __init__(self):
            print('init', end=',')
        def hi(self, name):
            print('Hi '+name, end=',')
        def close(self):
            print ('close', end=',')

    with contextlib.closing(Hi()) as h:
        h.hi('John')
##wrapper_mgr()        #  init,Hi John,close,

