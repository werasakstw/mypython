
s = 'Hello how do you do?'

## The string find() can find only specific substring.
# print(s.find('do'))

## To search for specific text pattern we need regular expression(RE).
## An RE may consist of characters and operators.
from re import findall
# print(findall('do', s))

## .  matches any (Unicode) character except '\n'.
# print(findall('.o', s))

## * matches 0 or more previous character repetition.
## + matches 1 or more previous character repetition.
## ? matches 1 or one previous character repetition.
def repeat():
    t = 'ac abc abbc'
    print(findall('ab*c', t))
    print(findall('ab+c', t))
    print(findall('ab?c', t))
# repeat()

## [xy] matches any one character listed within.
## [x-z] matches any one character listed within.
## ^ matches characters not in the range.
## | or
def range():
  t = 'w x y z' 
  print(findall('[xy]', t))
  print(findall('[x-z]', t))
  print(findall('x|y', t))
  
  t = 'xm xn ym zm xx'
  print(findall('[x-y][l-o]', t))
  print(findall('[x-z][^l-o]', t))
# range()

## Special Sequence: To matches any,
## \d   decimal digit [0-9]
## \D   nondigit character [^0-9]
## \s   whitespace: blank space, \t, \n, and \r
## \S   non-whitespace
## \w   alphanumeric [a-zA-Z0-9_]
## \W   nonalphanumeric [^a-zA-Z0-9_]
def special():
    t = 'a12c axyzc a1bc'
    print(findall('a\d*c', t))
    print(findall('a\D*c', t))
# special()

## Search:
from re import search
def search_test():
     m = search( 'l+' , 'hello' )
     print(m.start(), m.end())
     
     print(m.string)
     print(m.string[m.start():m.end()])

     print(m.group())
# search_test()

## Compile:
from re import compile
def compile_test():
    p = compile('\D+')
    m = p.match('Hello john 123')
    if (m):
        print(m.start(), m.end())
        print(m.group())
# compile_test()

#############################################################

## Ex. Search in File
def sea_file():
    with open('regex.py', 'r') as f: 
        for line in f:
            if search('Ex', line):
                print(line)
# sea_file()               






