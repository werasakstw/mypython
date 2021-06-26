''' A farmer say 'In my farm there are 36 heads and 100 feet altogether.'
He has just chickens and pigs. How many chickens and pigs does he have? 
'''
def farmer():
    for chickens in range(36):
        pigs = 36 - chickens
        if (chickens*2 + pigs*4 == 100):
            print(chickens, pigs)
##farmer()

''' A monkey ate 100 coconuts in 5 dates, each day ate 6 more than the previous day. 
How many did he eat on each days?
'''
def monkey():
    for a in range(100):
        for b in range(100):
            if (6+a == b):   
                for c in range(100):
                    if (6+b == c):
                        for d in range(100):
                            if (6+c == d):
                                for e in range(100):
                                    if (6+d == e) and (a+b+c+d+e == 100):
                                            print(a, b, c, d, e)                           
    #! comprehension  (iteration.py)
    [ print(a, b, c, d, e)
        for a in range(100)
        for b in range(100) if (6+a == b)
        for c in range(100) if (6+b == c)
        for d in range(100) if (6+c == d)
        for e in range(100) if (6+d == e) and (a+b+c+d+e == 100) ]
##monkey()

''' There is a flock of birds and herd of cows.
  If a brid rest on back of a cow there will be a bird left.
  If two brids rest on a cow there will be a cow left.
Find the smallest numbers of birds and cows.
'''
def brids_cows():
    for b in range(100):
        for c in range(100):
            if (b - c == 1) and (c - b/2 == 1):
                print(b, c)
                break
##brids_cows()

#----------------------------------------------------------------

'''                   Logic Puzzles
Pork and Chicken.
A, B, and C always have lunch together.
    (1). If A order chicken, then B order pork.
    (2). Either A or C order chicken.
    (3). At least one of B and C order chicken.
Who do not eat pork?
'''
def pork_chicken():
    def test1(a, b):
        if a == 'chicken' and not (b == 'pork'):
            return False
        return True

    def test2(a, c):
        if (a == 'chicken' and c == 'pork') or \
           (a == 'pork' and c == 'chicken') :
            return True
        return False

    def test3(b, c):
        if b == 'chicken' or c == 'chicken':
            return True
        return False

    order = ['pork', 'chicken']
    for a in order:
        for b in order:
            for c in order:
                if test1(a, b) and test2(a, c) and test3(b, c):
                    print('A = %s, B = %s, C = %s' % (a, b, c))
##pork_chicken()

''' Lion and Tiger.
Lion always lies on Monday, Tuesday, and Wednesday, 
    and tell the truth for the rest of the week.
Tiger lies on Thursday, Friday, and Saturday, 
    and tell the truth for the rest of the week.
Today the lion say 'Yesterday I am a liar.' 
The tiger say 'Me too'. 
What is the day of the week, today?
'''
def lion_tiger():
    def yesterday(day):
        return (day - 1) % 7
    
    lion = ('T', 'T', 'T', 'T', 'L', 'L', 'L')
    def lion_say(day):
        say  = lion[yesterday(day)] == 'L'
        if lion[day] == 'T':
            return say
        return not say
    
    tiger = ('T', 'L', 'L', 'L', 'T', 'T', 'T')    
    def tiger_say(day):
        say  = tiger[yesterday(day)] == 'L'
        if tiger[day] == 'T':
            return say
        return not say

    days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
    for day in range(len(days)):
        if lion_say(day) and tiger_say(day):
            print(days[day])
##lion_tiger()

''' Big Peppers.
In a mystery foreign language:
       'le ka bu' means 'buy green peppers',
       'ma bu gu' means 'big green cars',
       'ko le ma' means 'quickly buy cars'.
How do you say 'big peppers' in this language?
'''
def big_peppers():
    a = ['le', 'ka', 'bu']
    b = ['ma', 'bu', 'gu']
    c = ['ko', 'le', 'ma']
    found = False
    while (not found):
        random.shuffle(a)
        random.shuffle(b)
        random.shuffle(c)
        buy, green, peppers = a
        big, _green, cars = b
        quickly, _buy, _cars = c
        if (green == _green) and (buy == _buy) and (cars == _cars):
            print(big, peppers)
            found = True
##big_peppers()

''' Three Gods:
There are 3 gods which are a truth teller, a liar, and a free will.
But we don't know who is who?
    God0 say: 'God1 is a liar(L).'
    God1 say: 'I am a free will (F)'
    God2 say: 'God1 is a truth teller (T).'
Who is the truth teller?
'''
def three_gods():
    def say(x, y, t):   ## x say 'y is t'.
        if x == 'T':
            return y == t
        elif x == 'L':
            return not (y == t)
        else:
            return True

    for gods in itertools.permutations(['F', 'L', 'T']):
        if say(gods[0], gods[1], 'L') and \
           say(gods[1], gods[1], 'F') and \
           say(gods[2], gods[1], 'T'):
                print('God0 = %s, God1 = %s, God2 = %s' % gods)
##three_gods()

