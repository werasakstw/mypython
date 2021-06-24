
# Python string literals may be enclosed with:
#	'           single quotes
#	"           double quotes
#	'''  """    triple single/double quotes
##print('Hello')
##print("Hello")
##print('''Hello''')
##print("""Hello""")

# Single quotes and double quotes may be nested.
##print('John said, "Hello".')
##print("Jack said, 'Hi'.")

'''
Single/double quotes cannot contain <newline> nor <return>.
Triple quotes are useful for multiple line strings which may contain ' or ".
'''
##print('''
##When I saw John yesterday.
##He said, "Hello". I said, 'Hi'.
##''')

'''
Escape sequences:
Special characters begins with \ and must be escaped inside quoted strings.
 \',  \",  \\,  \r (return),  \n (newline),  \s (space), and \t (tab)
'''
##print('Joe said, \'Hello\'.')

# Consecutive 'str' literals with no separators are combined into a value.
##print('Hello' 'John')         # It is also true in REPL.

# That allows separating a long str into multiple lines.
##print('Hello how do you do?'  
##      "It's nice to see you.")

# Beware of missing separators between elements of str lists.
##print(['a', 'b' 'c'])           # ['a', 'bc']

# A string that created by +(append) has more overhead than creating at once.
##print('Hello' + ' ' + 'how' + ' ' + 'are' + ' ' + 'you?')  # bad
##print(' '.join(['Hello', 'how', 'are', 'you?']))           # good

def str_iterate():
    s = 'abc'
    
    # Iterate a str with indexing (Bad).
    for i in range(len(s)):
        print(s[i], end=',')  # a,b,c,
    print()

    # Iterate a str with iterator.
    for c in s:
        print(c, end=',')      # a,b,c,
##str_iterate()

#---------------------------------------------------------------

                    # String Operations:
def str_op():
    # Conditional String
    print('Hello' if False else 'Hi')   # Hi

    s = 'Hello'
    # Built-in functions
    print(len(s), min(s), max(s))   # 6 ! o

    # in
    print('el' in s)          # True
    
    # Find
    print(s.find('el'))       # 1

    # Startswith, Endswith
    print(s.startswith('Hell'), s.endswith('lo')) # True True

    # Occurance count
    print(s.count('l'))       # 2

    # Slice
    print(s[1:3], s[1:], s[:3]) # el ello! Hel

    # Reverse
    print(s[::-1])          # ?uoy era woh olleH

    # Step
    print(s[::2])            # Hlo

    # Str to int 
    print(int('123'), int('10', 2), int('F', 16))  # 123  2  15

    # Int to str
    print(bin(5), oct(8),hex(15) )      # 0b101  0o10  0xf

    # <str>.strip(<chars>) removes characters from both ends of a string.
    print(' Hello '.strip())            # Hello  
    print('...Hello.how.are.you?.......'.strip('.'))    # Hello.how.are.you?

    # <str>.replace(<str1>,<str2>) replaces str1 with str2.
    print('john jack joe'.replace('j', 'J'))    # John,Jack,Joe

    # list -> str
    # <separator>.join(<str list>) creates a string from <str list>.
    a = ['a', 'b', 'c']
    print(', '.join(a))         # a, b, c

    # join() only works with str.
    a = [1, 2, 3]
    # print(', '.join(a))       #  error
    print(', '.join(str(x) for x in a))   # 1, 2, 3    

    # str -> list
    # <str>.split(<separator>) splits the <str> into a list of str.
    # The default separator is a blank.
    print('a,b,c'.split(','))           # ['a', 'b', 'c']

    # Split with separator
    x = '  a  b    c '
    print(x.split())        # ['a', 'b', 'c']
    print(x.split(' '))     # ['', '', 'a', '', 'b', '', '', '', 'c', '']

    # str -> str
    # <str>.partition(<separator>) partitions the <str> into head, sep, and tail.
    head, separator, tail = 'John Jack Joe'.partition(' ')
    print([head], [separator], [tail])  # ['John'] [' '] ['Jack Joe']
##str_op()

def cases():
    s = 'john jack joe'
    
    # <str>.capitalize() capitalizes only the first word.
    print(s.capitalize())  # John jack joe

    # <str>.title() capitalize all the words.
    print(s.title())       # John Jack Joe

    # <str>.upper() converts all characters to uppercase.
    print(s.upper())       # JOHN JACK JOE

    # <str>.lower() converts all characters to lowercase.
    print('John Jack Joe'.lower())    # john jack joe

    # <str>.swapcase()
    print('John Jack Joe'.swapcase())   # jOHN jACK jOE
##cases()
                                                                                                     
#-------------------------------------------------------------

'''                String Format
Python provide many alternative string formattings:
    1. Old Style String Formatting: Similar to C's printf().
           <str with format characters> % values
If values have more than one values, they must enclosed in ().
Values are substituted in order.
            Format Characters:
     b binary
     c character - convert to unicode character
     d decimal (default)
     n decimal with locale specific separators
     o octal
     x hex (lower-case)
     X hex (upper-case)
     e/E Exponent. Lower/upper-case e
     f Fixed point
     g/G General. Fixed with exponent for large, and small numbers ( g default)
     n g with locale specific separators
     % Percentage (multiplies by 100)
'''
def old_style():
    print('Hello! %s.' % 'John')            # Hello! John.
    print('Hello! %s  and %s.' % ('John', 'Jack')) # values are wrapped as a tuple
                                            # Hello! John  and Jack.
    # Formatting with number bases
    # %b is not supported. 
    print('%o, %d, %x' % (10, 10, 10))      # 12, 10, a

    # Float format
    print('%.2f' % 123.456)                 # 123.46

    # Sequences can be formatted to str.
    print('Hello! %s.' % ['John', 'Jack'])  # Hello! ['John', 'Jack'].
    
    # But sequences can be printed.
    print([1, 2])                            # [1, 2]
##old_style()

''' 2. New Style String Formatting: (Python3.0)
Create a str from a template by substitute values in place holders.
       <str with place holders>.format(<values>)         
{} specifies a place holder.
Place holders can be referred by order, position or name.
Values may be formatted by default, according to the types.
format() is a method of the 'str' class.
'''
def new_style():
    # {} are place holder for formatted values.
    print('Hello {} and {}.'.format('John', 'Jack'))  # Hello John and Jack.

    # Place holders may specify value positions.
    print('Please bring me {1} {0}.'.format('books', 10))
                                                    # Please bring me 10 books.
    # Place holder may specify name of the values.
    print('Hello {n1} and {n2}.'.format(n2 = "John", n1 = "Jack"))
                                                    # Hello! Jack and John.
    # name/position with format characters
    print('Hello {n1:s} and {n2:s}.'.format(n2 = 'John', n1 = 'Jack'))
                                                    # Hello! Jack and John.
    print('{0:s}, {1:.2f}, {2:3d}'.format('books', 1.2, 12)) # books, 1.20,  12
    
    # Format with number bases
    print('{:b}, {:d}, {:o}, {:x}'.format(10, 10, 10, 10))  # 1010, 10, 12, a

    # Float format
    print('{:.2f}'.format(123.456))                 # 123.46

    # Default list/set format.
    print('{}, {}'.format([1, 2, 3], {1, 2, 3}))    # [1, 2, 3], {1, 2, 3}
##new_style()

''' 3. format() built-in function:
          format(<value>, <pattern>)
<pattern> is  [sign][width][.precision][type]
Mostly for decimal, float and number base formats.
'''
def format_function():
    # d   Displayed as decimal.
    print(format(12, '+4d'))    #  +12

    x = 12.3456   
    # f    Fixed point with default precision 6.
    # F    Same as f , except nan is converted to NAN and inf to INF.
    print(format(x, 'f'))       # 12.345600
    print(format(x, '+4.2f'))   # +12.35

    # e, E Exponential format, with e/E to mark the exponent. Default precision is 6.
    print(format(x, 'e'))       # 1.234560e+01
    print(format(x, '.2E'))     # 1.23E+01

    # g, G, n General format, where the number is rounded to the given precision.
    print(format(x, 'G'))       # 12.3456

    # %   multiplied by 100, displayed in f format with a percentage sign.
    print(format(0.25, '.1%'))  # 25.0%

    # Convert int to str, with number bases:
    print(format(10, 'b'))      # 1010
    print(format(10, 'o'))      # 12
    print(format(10, 'd'))      # 10
    print(format(10, 'x'))      # a
    print(format(10, 'X'))      # A  
##format_function()

''' 4. String Interpolation: Introduced in Python 3.6
Function Str allows expressions embedded inside str literals.
A function str is prefixed with 'f'.
Expressions must be surrounded by { }.
Expressions contain variables that values must be known at runtime.
'''
def interpolation():
    thing = 'books'
    price = 12.345
    print(f'This {thing} costs {price:.2f}.')

    a, b = 1, 2
    print(f'a + b = {a + b}')   # a + b = 3
##interpolation()

''' 5. Template String is less powerful but simple and more suitable in some cases.
All values are formatted according to the type.
It allows creating a str from a template which all default format.
Template strings are not a core language feature but supplied by standard library.
'''
from string import Template     # Python has 'string' module.
def temp_str():
    t = Template('Hello $name please send me $value buck.')
    print(t.substitute(name='John', value='10')) # Hello John please send me 10 buck.
##temp_str()

''' Zen of Python: There should be one obvious way to do something.
    Rich languages provide many ways to do the samething.  '''

#---------------------------------------------------------------

# String Close Match:
from difflib import get_close_matches
def close_match():
    x = 'abc'
    y = ['aaa', 'bac', 'aac', 'xbc', 'bdca', 'abb']
    print(get_close_matches(x, y))
    print(get_close_matches(x, y, n=1))
    print(get_close_matches(x, y, cutoff=0.4))
    print(get_close_matches(x, y, cutoff=0.7))
##close_match()

# 'string' lib: provides ready to use characters, digits and symbols.
import string
def str_const():
    print(string.ascii_lowercase)
    print(string.ascii_uppercase)
    print(string.ascii_letters)
    print(string.digits)
    print(string.punctuation)
    print(string.whitespace)
    print(string.printable)
##str_const()

