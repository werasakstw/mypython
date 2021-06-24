'''
Events A and B are independent if A occurs does not affect B.
The probability that A and B heppen is the product of the probabilities of A and B.
          P(E, F) = P(E) P(F)

Coin Flipping:       P(HEAD) = 1/2
                  P(HEAD, HEAD) = 1/2 x 1/2
                  P(HEAD, HEAD, HEAD) = 1/2 x 1/2 x 1/2
'''
import random
HEAD, TAIL = 0, 1
def flip():   
    return random.choice([HEAD, TAIL])
def head_test(n):
    def test():
        h = hh = hhh = 0
        for _ in range(n):
            a, b, c = flip(), flip(), flip()
            if a == HEAD:
                h += 1
            if a == HEAD and b == HEAD:
                hh += 1
            if a == HEAD and b == HEAD and c == HEAD:
                hhh += 1
        print(round(h/n,3), round(hh/n,3), round(hhh/n,3))
        
    for _ in range(10):
        test()
##head_test(10000)

# Die Rolling:       P(ONE) = 1/6
ONE, TWO, THREE, FOUR, FIVE, SIX = 1, 2, 3, 4, 5, 6
def roll():   
    return random.choice([ONE, TWO, THREE, FOUR, FIVE, SIX])

#                    P(HEAD, ONE) = 1/2 x 1/6 = 1/12 = 0.08333...
def coin_die(n):
    def test():
        ho = 0
        for _ in range(n):
            f = flip()
            r = roll()
            if f == HEAD and r == ONE:
                ho += 1
        print(round(ho/n, 3))
        
    for _ in range(10):
        test()
##coin_die(10000)

#----------------------------------------------------------------#

'''
For rolling two dies independently, the number of possible outcomes is 6x6 = 36.
Find all probabilities for the sum of two dies.
'''
def two_dies():
    oc = {(a, b): a+b for a in range(1,7) for b in range(1,7)}
##    print(len(oc), oc)

    from collections import defaultdict
    doc = defaultdict(list)
    for k,v in oc.items():
        doc[v].append(k)
##    print(len(doc), doc)

    r = {k:len(v)/36 for k,v in doc.items()}
    for s, p in r.items():
        print('%d: %.2f' % (s,p))
##two_dies()

#----------------------------------------------------------------#

'''
Events A and B are dependent if one event affects the other.
Let P(B | A) is the probability of B given that A happened.
              P(A, B) = P(A) P(B|A)

A deck of 52 cards has 4 queens.
What is the probability of drawing two queens from a deck, without put back.
  P(FIRST_Q)            = 4 /52
  P(SECOND_Q | FIRST_Q) = 3 /51
  P(FIRST_Q, SECOND_Q) = 4 /52 x 3 /51 = 1/221 = 0.00452
'''
QUEEN = -1
def two_queen(n):
    qq = 0.0
    for _ in range(n):
        deck = list(range(48)) + [QUEEN]*4    # create a deck
        first = random.choice(deck)
        if first == QUEEN:
            deck.remove(first)
            second = random.choice(deck)
            if second == QUEEN:
                qq += 1
    print(round(qq/n, 5))
##two_queen(100_000)

