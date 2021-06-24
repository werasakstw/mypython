
''' List
Josephus Problem:
When an Egyptian troop chased a group of Hebrew up to a mountain.
They surrounded the mountain and won't let any escape.
The Hebrews despairingly wanted to die rather than captured.
They invented an amazing mass suicide method:
 - They will form a circle.
 - Then start at a person counts 1, person on the left counts 2, and the next counts 3.
 - The person who counts 3 will be killed by the other.
 - Then the counting 1, 2, 3 and killing continue for the next person.
 - The last person must perform suicide.
While the last farewell was going on, a once high ranking gerneral in the group
spotted Josephus a well known mathematician. He approached Josephus and ask,
"Are you ready to die?".  Josephus promptly replied, "No".
The general said: "You must quicky compute the last survive two positions.
As an old general, I can arrange the circle and appoint anyone to start first.
You and I will be in that positions." 
The legend said there were 41 persons, what are the two positions?
'''
def josephus():
    a = list(range(1, 42))
    while len(a) > 2:
       a.append(a.pop(0))
       a.append(a.pop(0))
       a.pop(0)
    print(a)
# josephus()

''' List allows representing order oriented data.
ex. A polynomial:  1 + 2*x + 3*x**2 + 4*x**3 
  can be represented as a list of coefficient  [1, 2, 3, 4]
'''
def eval_poly(p, x):
    r = 0
    for i, c in enumerate(p):
        r += c*x**i
    print(r)
##eval_poly([1, 2, 3, 4], 1.5)
    
# Lists allow iteratating a sequence with some actions.
def iterate():
    names = ['John', 'Jack', 'Joe']
    for name in names:
        print('Hello', name)
##iterate()

# Lists allows passing a sequence to/from a function.
def passing():
    def hello(names):
        for name in names:
            print('Hello', name)

    names = ['John', 'Jack', 'Joe']
    hello(names)
##passing()

# Create a list of n booleans, filled with True except the first two.
def gen_list(n):
    a = [False, False]  # position 0 and 1 are False. 
    for i in range(2, n):
        a.append(True)
    return a
##print(gen_list(5))      # [False, False, True, True, True]

''' Lists are 'ramdom access' memory, that means all elements
can be accessed in approximately the same time.
Lists allows ramdom access an element by possition.
'''
# Mapping with Indexing
grade_map = ('A', 'B', 'C', 'D', 'F')
def score_map(score):
    return 0 if 90 <= score else    \
           1 if 80 <= score else    \
           2 if 70 <= score else    \
           3 if 50 <= score else 4
def frequency_count(): # (histogram)
    scores = (83, 74, 51, 79, 91, 80, 94, 89, 43, 77, 56, 67, \
              88, 57, 33, 57, 66, 78, 64, 71, 85, 72, 76, 70, 76, 74)
    grades = [0, 0, 0, 0, 0]
    for s in scores:
       grades[score_map(s)] += 1
       
    for i in range(len(grades)):
       print(grade_map[i], end=': ')
       for j in range(grades[i]):
          print('*', end='')
       print()
##frequency_count()

#---------------------------------------------------------------

''' Generating a deck of random cards.
A card is represented by an int. A deck is [0, 1, ..., 51].
'''
import random
def rand_deck1():   # bad
    deck = []
    while len(deck) < 52:
       x = random.randrange(0,52)
       if x not in deck:
          deck.append(x)
    print(deck)
##rand_deck1()

def rand_deck2():   # not so bad
    deck = set()
    while len(deck) < 52:
        deck.add(random.randrange(0,52))
    print(deck)
##rand_deck2()
    
def rand_deck3():  # better
    deck = list(range(52))
    for i in range(52):
        x = random.randint(0, 51)
        deck[i], deck[x] = deck[x], deck[i] # swap at position i and x.
    print(deck)
##rand_deck3()

def rand_deck4():   # pro
    deck = list(range(52))
    random.shuffle(deck)
    print(deck)
##rand_deck4()

#-------------------------------------------------------------------

# Sieve of Eratosthenes: efficiently create a lot of primes.
def sieve(n): 
    a = gen_list(n+1)
    # From 2 to the half of n.    
    for i in range(2, n // 2):
        # Start for a prime position
        if a[i]:
            # Jump by i 
            for j in range(i*2, n+1, i):
                # Mark the j position is not prime.
                a[j] = False
    # Return a list of prime positions 
    return [i for i in range(n+1) if a[i]]
##print(sieve(100))

# Binary Sort:
# Sorting a list of integers of narrow range.
def bin_sort():
    a = [3, 2, 6, 2, 6, 4, 9, 6, 1, 7]  # <range> 0 -> 9
    
    # create list of size <range> filled with 0.
    r = 10
    c = [0]*r
    
    # Using the element value as position
    for i in a:
        c[i] += 1

    # Collecting the result.
    b = []
    for i in range(r):
        for _ in range(c[i]):
            b.append(i)
    print(b)
##bin_sort()

''' Normally a mapping is performed by a function or dict.
But lists can map from a integer to a value.

Day Mapping:
sat = 0, sun = 1, mon = 2, tue = 3, wed = 4, thu = 5, fri = 6
'''
dm = ['sat', 'sun', 'mon', 'tue', 'wed', 'thu', 'fri' ]
## print(dm[6])        # fri

''' List allows storing results for using later instead of recompute.
    Factorial: 
          n! = fac(n) = n * (n-1) * (n-2) .... * 1
'''
def fac(n):
    r = 1;
    for i in range(1, n+1):
        r *= i
    return r

''' Find a 3 digits integer 'abc' such that:
          abc = a! + b! + c!
hint:     145 = 1! + 4! + 5!
'''
def abc():
    for a in range(1, 10):
        for b in range(0, 10):
            for c in range(0, 10):
                if 100*a+10*b+c == fac(a) + fac(b) + fac(c):
                    print(a, b, c)			
##abc()

# Trading memory for speed.
def abcx():
    # Create a list of 10 factorials.
    fac = [1, 1]
    for i in range(2, 10):
        fac.append(fac[i-1]*i)

    for a in range(1, 10):
        for b in range(0, 10):
            for c in range(0, 10):
                if 100*a+10*b+c == fac[a] + fac[b] + fac[c]:
                    print(a, b, c)			
##abcx()

#--------------------------------------------------------------

''' Dict provides mapping by key.
Day Mapping:
   sat = 0, sun = 1, mon = 2, tue = 3, wed = 4, thu = 5, fri = 6
'''
dm = {'sun': 1, 'mon': 2, 'tue': 3, 'wed': 4, 'thu': 5, 'fri': 6, 'sat': 0 }
##print(dm['mon'])        # 2

# Morse Code:
code = {
    'A': 'o-', 'B': '-ooo', 'C': '-o-o', 'D': '-oo', 'E': 'o', 'F': 'oo-o',
    'G': '--o', 'H': 'oooo', 'I': 'oo', 'J': 'o---', 'K': '-o-', 'L': 'o-oo',
    'M': '--', 'N': '-o', 'O': '---', 'P': 'o--o', 'Q': '--o-', 'R': 'o-o',
    'S': 'ooo', 'T': '-', 'U': 'oo-', 'V': 'ooo-', 'W': 'o--', 'X': '-oo-',
    'Y': '-o--', 'Z': '--oo', ' ': ' ',
    '1': 'o----', '2': 'oo---', '3': 'ooo--', '4': 'oooo-', '5': 'ooooo',
    '6': '-oooo', '7': '--ooo', '8': '---oo', '9': '----o', '0': '-----' }

def encode(msg):
    def enc(k):
        return code[k]
    
    # encode the message
    morse = ''
    for m in msg:
        morse += enc(m) + ','      # Using ',' as separator.
    return morse[0: len(morse)-1]  # remove the last ','

def decode(morse):
    def dec(v):
        for i in code.keys():
            if code[i] == v:
                return i
            
    # decode the message
    msg = ''
    for m in morse.split(','):
        msg += dec(m)
    return msg

def morse_code():
    msg = list('HELLO HOW DO YOU DO')
    morse = encode(msg)
    print(morse)
    print(decode(morse))
##morse_code()

#---------------------------

''' Chinese Zodiac:
The Chinese assign animals to years in a 12 year cycle.
The pattern repeats before and from there:
      2000 Dragon         % 12  == 8
      2001 Snake                   9
      2002 Horse                  10
      2003 Sheep                  11
      2004 Monkey                  0
      2005 Rooster                 1
      2006 Dog                     2
      2007 Pig                     3
      2008 Rat                     4
      2009 Ox                      5
      2010 Tiger                   6
      2011 Hare                    7
'''
def zodiac(year):
    r = year % 12
    if r == 8:
        return 'Dragon'
    elif r == 9:
        return 'Snake'
    elif r == 10:
        return 'Horse'
    elif r == 11:
        return 'Sheep'
    elif r == 0:
        return 'Monkey'
    elif r == 1:
        return 'Rooster'
    elif r == 2:
        return 'Dog'
    elif r == 3:
        return 'Pig'
    elif r == 4:
        return 'Rat'
    elif r == 5:
        return 'Ox'
    elif r == 6:
        return 'Tiger'
    else:
        return 'Hare'

# Using list/tuple for mapping.
z = ( 'Monkey', 'Rooster', 'Dog', 'Pig', 'Rat', 'Ox', 'Hare',
      'Tiger', 'Dragon', 'Snake', 'Horse', 'Sheep' )
def zodiac(year):
    return z[year % 12]

predict = { 'Rat': 'Charm, smart, adroit, agile',
            'Ox': 'Mild, prudent, honest, endure',
            'Tiger': 'Bold, allure, quick-tempered',
            'Hare' : 'Bland, courtesy, politeness, good taste',
            'Dragon': 'Leader, astute, dexterous, attractive, ambitious',
            'Snake': 'Mysterious, elegant, individual, indolent',
            'Horse': 'Honesty, shy, intensive, athlete',
            'Sheep': 'Artist, romantic, imaginative, unreliable',
            'Monkey': 'Clever, playful, persuasive, talkative',
            'Rooster': 'Confident, generous, lively, entertainment',
            'Dog': 'Trustworthy, instinct, intuitive unrest',
            'Pig': 'Simple mind, forgiveness, kindness, careless'}
def zodiac_test(year):
    zod = zodiac(year)
    print('%s:\t%s' % (zod, predict[zod]))
##zodiac_test(2021)

#--------------------------------------------------------------

''' Str.
Random Password Generator:
   - length between 8 to 10 characters.
   - begins with an upper case letter then follow by digits, lower case or upper case letters.
'''
import string
def gen_pwd():                                                  # (lists.py)
    DIGITS = list(string.digits)                # 'string' lib  (strings.py)
    UPPER = list(string.ascii_uppercase)
    LOWER = list(string.ascii_lowercase)
    SYM = [DIGITS, LOWER, UPPER]
    
    def gen():
        p = random.choice(string.ascii_uppercase)  # The first character.
        for i in range(random.randint(7, 9)):
            s = random.choice(SYM)
            p += random.choice(s)
        return p
    
    for i in range(10):
        print(gen())
##gen_pwd()

#----------------------------------------------------------------

''' Python integers are not allowed to begin with 0.
Sometime it is safer to work with str.
car(<seq>) returns a tuple of <head> and <tail>.
'''
def car(n: str):                           # type annotation (types.py)
   return (n[0], n[1:])                             # tuple (tuples.py)
##print(car('123'))       # ('1', '23')
##print(car('1023'))      # ('1', '023')

# Count the number of <digit> at the beginning of <number>.
def prefix_count(digit: str, number: str):
   c = 0
   while len(number) > 0:
      head, tail = car(number)
      if digit == head:
         c += 1
      else:
         break
      number = tail
   return c
##print(prefix_count('1', '11123'))     # 3
##print(prefix_count('1', '110123'))    # 2

# Find a square number n**2 with the most 7 prefixed for n below 1_000_000.
def most7_prefix(m):
    n, max = None, 0
    for i in range(2, m):
        x = prefix_count('7', str(i*i))
        if x > max:
            max = x
            n = i            
    return (n, n*n)
##print(most7_prefix(1_000_000))    # (881917, 777777594889)

#------------------------------------------------------------------------

''' Pig Latin: A children's encryption.
         https://www.wikihow.com/Speak-Pig-Latin
  If a word begins with a vowel(a, e, i, o, u) add 'way' to the end.
  Else move the first character to the end then add 'ay'.
'''
def pig_latin(s):
    def encrypt(w):
        if w[0] in 'aeiou':
            return f'{w}way'            # function string (strings.py)
        return f'{w[1:]}{w[0]}ay'       # slice           (strings.py)
    
    # str -> list and comprehension
    en= [encrypt(w) for w in s.split(' ')]
    print(' '.join(en))                 # list -> str
##pig_latin('Hello what time is it')

# Try: Handle capital letters at the beginning of statement.

''' Exercises
The United State banknotes in have images of famous presidents:
        George Washington  (gw)	 $1
        Thomas Jefferson   (tj)	 $2
        Abraham Lincoln    (al)	 $5
        Alexander Hamilton (ah)  $10
        Andrew Jackson	   (aj)  $20
        Ulysses S. Grant   (ug)  $50
        Benjamin Franklin  (bf)  $100

That allows encoding an integer value into a string by the rules:
        - 2 characters (of a president) represent an integer.
        - The result is summation of each values.
    There can be many ways to represent a value.
    e.g.   gwgwgw = 1 + 1 + 1 = tjgw = 2 + 1 = 3
               ah = gwgwgwgwgwal = altjgwtj = 5
    Write functions:
            decode(<string>) -> <integer>
            encode(<integer>) -> <string>   for the shortest string
'''
