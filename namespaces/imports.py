'''
A 'module' is a file that contains definitions of variables,
functions or classes.
The file name is the name of the module and its namespace.

'import' statements allow using names defined in the modules.
Python has several import options.
'''

# 1.  import <module>
# The imported names must be referred via the module name.
def import1():
    import mymod        # May be locally imported.
    print(mymod.one)    # 1
    mymod.hello()       # Hello
    mymod.A.hi()        # Hi
##import1()

# 2.  import <module> as <other>
# The module name is redefined.      
def import2():
    import mymod as m
    print(m.one)        # 1
    m.hello()           # Hello
    m.A.hi()            # Hi
##import2()

# 3.  from <module> import <name1>,<name2>,...
# Static import: One or names can be imported and referred directly.
def import3():
    from mymod import one, hello
    print(one)          # 1
    hello()             # Hello
##import3()

# 4.  from <module> import <name> as <other>
# Static import with redefined name. 
def import4():
    from mymod import hello as greet
    greet()             # Hello
##import4()

# 5. from <module> import *
# Static All import: allowed only at the module level.
from mymod_ import *            
def import5():
    hello()         # Hello how are you?

    # Names that begins with an underscore cannot be referred to.
##    _hi()         # error
##import5()

# But the names are not private since they can be imported normally.
def import_():
    import mymod_
    mymod_._hi()    # Hi
##import_()

# Static All imports should be avoided since there may be name collision.
from mymod import *
def collision():
    hello()       # Hello
##collision()

#--------------------------------------------------------------------

# With static import all, a module may define a tuple __all__
# to specify only the names that can be referred to.
from mod_all import *    
def mod_all_test():
    print(john)         # John Rambo
##    print(jack)       # error
    hello()             # Hello
##    hi()              # error

    # But __all__ does not make the names un-importable.
    # Since it can be imported explicitly.
    import mod_all
    print(mod_all.jack) # Jack Ripper
    mod_all.hi()        # Hi
##mod_all_test()

#--------------------------------------------------------
    
# A 'package' is a directory that may contain modules and subpackages.
# Packages allow organizing a lot of modules.

# Importing a module in a package needs the path to the module.
# In the old time a package directory must have a file '__init__.py'
# to indicates that it is a package. But no longer needed since Python 3.3. 
def pack_import():
    # 1.  import <module path>
    # <module path> starts from the search path.
    import mypack.one.greet
    mypack.one.greet.hello()    # Hello (from mypack.one).
    mypack.one.greet.hi()       # Hi (from mypack.one).

    #  2. from <module path> import <name>
    from mypack.one.greet import hello
    hello()         # Hello (from mypack.one).

    #  3.  from <module path> import <name> as <other>
    from mypack.one.greet import hi as h
    h()             # Hi (from mypack.one).

    #  4. from <package path> import <module>
    from mypack.one import greet
    greet.hello()   # Hello (from mypack.one).
    greet.hi()      # Hi (from mypack.one).
##pack_import()

# 5.  from <module path> import *
#  Allowed only at the top level.
from mypack.one.greet import *
def import_pack_star():
    hello()     # Hello (from mypack.one).
    hi()        # Hi (from mypack.one).
##import_pack_star()

#--------------------------------------------------------

# All module has attributes e.g.  __name__, __file__.
# The first executed module always named __main__.
def attr_test():
    print(__name__) # __main__
    print(__file__) # Path to this file.
##attr_test()

'''
When an 'import <module>' is executed:
1. The module is loaded.
2. The module's namespace is created as a dict and can be referred by __dict__.
3. The module code is executed.
4. Objects defined in the module are created and added to the dict.
So two modules may contain the same name, since they are different namespaces.
'''
def nsp_dict():
    import mymod  # The namespace 'mod' is created and added to current namespace.
    print(dir())            # ['mod']
 
    print(mymod.__name__)     # mymod
    print(mymod.__file__)
    print(mymod.__dict__)
##nsp_dict()

# The module namespace is created once at the first import.
# Reimporting an imported module does not create a new namespace.
def reimport():
    import mymod
    print(mymod.one)        #  1
    mymod.one = 11
    
    import mymod            #  The namespace is not recreated.
    print(mymod.one)        #  11

    #  importlib.reload() allows importing to recreate new namespace.
    import importlib
    importlib.reload(mymod)
    print(mymod.one)        # 1
##reimport()

'''
sys.path is a list of search paths for searching imported modules.
By default the sys.path is initialized as:
   - Working directory.
   - PYTHONPATH environment variable.
   - The installation dependent default.
'''
import sys
def search_path():
    for p in sys.path:
        print(p)
##search_path()

'''
The sys.path is a list which is mutable.
That allows importing modules from specified directories.
Suppose we want to import \mypack\greet.py
'''
def mod_path():     #  / is the path separator.
    sys.path.append('C:/mypython/basic/mypack')
    import greet
    greet.hello()
##mod_path()

'''
Normally the sys.path should not be modified since the
search path will be vary from program to program and
longer search path would make module searching slow.
If the 'mypack' is visible in the search path, we can
import a module from the package normally.
'''
def imp_mypack():
    from mypack import greet
    greet.hello()
##imp_mypack()

#-----------------------------------------------------------

'''
To speed up execution, the compiled modules and saves in the
__pycache__ directory as <module>.<version>.pyc files.
The __pycache__ is created only when a module is imported and
compiled, but not when it is just executed.

'py_compile' module can be used to manually compile a module e.g.
        python -m py_compile myprogram.py

The result is in \__pycache__ of the current directory.
Then we can excute the moulde as
        python myprogram.py

The Python compiler checks modify time of both .py and .pyc files,
if the .pyc is obsolete it will be recompiled.

The compiled code speed up execution of big programs.
It does not run much faster for small programs 
It may help if a module is imported frequently.

The compiler 'optimization switches' reduce the size of the compiled module.
-O removes assert statements.
-OO removes both assert and doc strings.

'compileall' module compiles all modules in the current directory.
 python -m compileall
'''

#-----------------------------------------------------------

'''
Python files are supposed to be used as:
 - scripts (applications) which will be executed by the python.exe.
 - modules (libraries) which will be imported to others.

Python programs do not need a main() as the starting point.
Since when an app is started or a module is imported, all statements
at top level will be executed from top to buttom. e.g.
'''
##import hello        #  I am hello.py

'''
Modules are created to be imported, but some must be executable by itself,
e.g. as for testing. These kind of modules should not contains statements
at the top level since they will be executed when imported.

Python proposed a pattern for a file that can be both script and module as:
- No statements at top level.
- Has a main() for designated starting point.
- Has an 'if' statement to execute main() if it is executed as a script.
python app.py        ## This is the starting point of the app.
'''
# Importing app.py module, the main() would not be executed.
##import app

#----------------------------------------------------------------

# A big application is normally created as a package.
# Python allows specifying the application's main script (the first to be executed)
#  by creating a __main__.py in the package directory.
# The application is executed with option -m.
# Normally __main__.py would not be imported so the 'if' statement is not needed.
# python -m myapp

#-----------------------------------------------------------------

# Many Python apps are executed in text mode as 'command line'.
# Python provides sys.argv for accessing command line arguments.
# python arg.py John Jack Joe

# 'cmd' lib supports 'command line' execution.
# 'cmd.Cmd' class provides a REPL execution.
import cmd, sys
def cmd_test():
    class CmdLoop(cmd.Cmd):
        def preloop(self):
            print('Start')
        def do_help(self, arg):
            print('Help', arg)
        def do_hello(self, arg):
            print('Hello', arg)
        def do_hi(self, arg):
            print('Hi', arg)
        def emptyline(self):
            print('Exit')
            sys.exit()
            
    CmdLoop().cmdloop()
##cmd_test()

#-----------------------------------------------------------

# To make a Python script file executable.
# pip install pyinstaller
# pyinstaller --onefile hello.py
# The result is in dist\hello.






    
