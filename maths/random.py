from random import *
def random_test():
    # randint(a, b) returns a random integer in [a, b] (inclusive).
    for _ in range(10):
        print(randint(1, 5), end=',')   # 5,5,5,3,1,1,2,3,5,5,
    print()
    
    # randrange(a) returns a random integer in [0, a) (exclusive).
    for _ in range(10):
        print(randrange(5), end=',')    # 3,1,3,4,3,3,0,1,3,3,
    print()

    # randrange(a, b) returns a random integer in [a, b).
    for _ in range(10):
        print(randrange(1, 5), end=',') # 1,4,1,3,3,3,3,3,4,4,
    print()

    # randrange(a, b, c) returns a random integer in [a, b) with c step.
    for _ in range(10):
        print(randrange(1, 10, 3), end=',') # 1,4,7,7,1,7,1,1,7,7,
    print()
    
    # random() returns a random float in [0.0, 1.0).
    for _ in range(10):
        print('%.2f' % random(), end=', ')
            # 0.50, 0.75, 0.55, 0.88, 0.26, 0.32, 0.21, 0.96, 0.90, 0.63,
##random_test()

## Seed:
## Python uses pseudo random generator, which produces a deterministic sequence.
## The result sequence can be reproduced by setting the seed.
## random() automatically uses time as default seed.
## Normally a seed is an integer, but string, bytes, or bytearray are acceptable.
def seed_test():
    # No seed
    print([randint(1, 10) for _ in range(10)])
    print([randint(1, 10) for _ in range(10)])
    
    # Set seed
    seed(7);  print([randint(1, 10) for _ in range(10)])
    seed(7);  print([randint(1, 10) for _ in range(10)])  
##seed_test()

def rand_bits():
    # getrandbits(n) returns a random n bits as an integer. 
    print([getrandbits(8) for _ in range(10)])
        # [76, 103, 44, 77, 70, 130, 175, 89, 10, 55]
    print([getrandbits(16) for _ in range(10)])
        # [16263, 31361, 41150, 57525, 12994, 55689, 36738, 62155, 32762, 23370]

    import os
    # os.urandom(n) returns a random n bytes as an array of bytes.
    print([os.urandom(2).hex() for _ in range(10)])
        # [e565, 7d28, 12e2, afd8, 8d83, 0cd8, 0dde, 5de0, e315, 38a3]
##rand_bits()

