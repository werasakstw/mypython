'''
Python runtime monitors if an illegal operation is encountered
an exception will be raised to signal an error.
Exceptions are objects to notify that something wrong.
Exceptions should be catched to handle the situation and go on.
If an exception is not catched, it will be propagated up and handled by default.
'''
def excep_ex():
    # Index out-of-bound
    a = [0, 1, 2]
    print(a[3])       # IndexError

    # The default handler
    #    print the stack trace and the exception info.
    #    stops the program.

    # Division by zero
    x = 0
    print(1/x)        # ZeroDivisionError

    print(1 + '1')    # TypeError
##excep_ex()

'''
               try:
                   <try block>
               except:
                   <except block>
               [finally:
                   <finally block>]
<try block> is executed unconditionally.
If there is an exception raised the <except block> is executed.
Otherwise the execution continues at the next statement.
After the error is handled in <except block> execution proceed the next statement.
'''
a = [0, 1, 2]
def index_acc(n): 
    try:
        print(a[n])
    except:           # catch all exception types
        print('Index out of bound.')
##index_acc(1)        # 1
##index_acc(3)        # Index out of bound.

'''
Exceptions may be catched by type.
         except <exception type> as <object>       
<object> is an error object contains information about the error.
<exception type> is the exception class.
'Exception' is the super class of all exception class.

A 'try' block may raise exceptions of many types.
But there can be only the first one that is raised.
A 'try' block may be followed by multiple 'execpt' blocks as catching each types.
'''
def mul_catch(n):
    try:
        print(a[n])
    except IndexError as err:
        print(err)
    except Exception as err:
        print(err)   
##mul_catch(1)        # 1
##mul_catch(3)        # list index out of range
##mul_catch(None)     # list indices must be integers or slices, not NoneType

# IndexError is a descendant class of Exception
##print(isinstance(IndexError(), Exception))  # True

# The order of catching child/parent classes is no matter.
def catch(n):
    try:
        print(a[n])
    except Exception as err:
        print(n, err) 
    except IndexError as err:
        print(n, err)
##bad_catch(3)
##bad_catch(None)

# Python exceptions are unchecked, the compiler does not enforce all catching.

''' Python provides 'try-else' block which will be executed if
no exceptions is raised, but not executed if an exception is
raised or abnormaly abort.
'''
def try_else(n):
    try:
        print(1/n, end=', ')
        if n == 2:
            return   # abnormal abort
    except ArithmeticError as e:
        print(e)
    else:
        print('else')
##try_else(0)        # division by zero
##try_else(1)        # 1.0, else
##try_else(2)        # 0.5
        
#-------------------------------------------------------------------

'''
The finally block will alway be executed, even there is
a return or another exception is raised.
'''
def try_finally(n):
    try:
        print(1/n, end=', ')
        if n == 2:
            return          # abnormal abort
    except ArithmeticError as err:
        print(err, end=', ')
        raise Exception()
    finally:
        print('finally')
def try_finally_test():
    try:
        try_finally(0)      # division by zero, finally
    except:
        print('exception')  # exception
    try_finally(1)          # 1.0, finally
    try_finally(2)          # 0.5, finally
##try_finally_test()

## Finally in loop:
def fin_loop():
    for i in range(5):
        print(i, end=', ')
        try:
            print(1/i, end=', ')
            if i == 2:
                continue
            elif i == 3:
                break
        except ArithmeticError as err:
            print(err, end=', ')
        else:
            print('else', end=', ')
        finally:
            print('finally')
##fin_loop()        # 0, division by zero, finally
                    # 1, 1.0, else, finally
                    # 2, 0.5, finally
                    # 3, 0.3333333333333333, finally

#---------------------------------------------------------------

'''
User Defined Exception may provide a proper name to indicate error.
'Exception' class is the parent for all error classes.
'''
class MyException(Exception):  
    pass
##raise Exception()
##raise MyException()

# Do not use 'try-except' as decision. Since a simple if-else would do.
def bad_except():
    #  The place that raises and catches an exception is in the same scope.
    def greet(name):
        try:
            if name == 'John':
                raise MyException()
            print('Hello ', name)
        except MyException:
            print('Hi ', name)

    greet('John')       #  Hi  John
    greet('Jack')       #  Hello  Jack
##bad_except()

def good_except():
    #  The place that raises and catches the exception is in the different scope.
    def greet(name):
        if name == 'John':
            raise MyException()
        print('Hello ', name)
            
    def caller(name):
        try:
            greet(name) 
        except MyException:
            print('Hi ', name)

    caller('John')      #  Hi  John
    caller('Jack')      #  Hello  Jack    
##good_except()

'''
Transaction:
          turn auto-commit off
          try:
              operation1()
              operation2()
              ....
              commit()
          except:
              roolback
When an exception is raised, statements after the place are not executed.
'''
def transaction():
    class Exception1(Exception):
        pass
    class Exception2(Exception):
        pass
    
    def op1():
        raise Exception1()
    def op2():
        raise Exception2()
    
    #  Independence Operations
    try:
        op1()
    except Exception1:
        print('S1')         #  S1
    try:
        op2()
    except Exception2:
        print('S2')         #  S2

    #  Transaction
    try:
        op1()
        op2()
    except Exception1:
        print('S1')         #  S1
    except Exception2:
        print('S2')   
##transaction()

#------------------------------------------------------------------

'''
Assertion: is a debugging aid that used for detecting errors.
If a program violates an assert expression, an exception is
raised forcing the program to exit with no recovering.
           assert <expression>
           assert <expression>, <error message>

   if __debug__:
       if not <expression>:
           raise AssertionError(<error message>)
'''
def assertion(x):
    print(__debug__)
    assert x == 0
    assert x == 0, 'x must be zero.'
##assertion(0)
##assertion(1)

'''
Assertions should be used in development, not in production mode.
Assertions should never be used for validation/authentication.
 Since it can be turn off by setting __debug__.

Assertion will be disabled if Python performs optimization.
python -O 07_exception.py        Big-O

Alternatively.
set PYTHONOPTIMIZE=1
python 07_exception.py

Beware: Do not wrap <expression>, <error message> in ( ) that
makes it a tuple and always True.
'''
x = 1
assert (x == 0, 'x must be zero.')
