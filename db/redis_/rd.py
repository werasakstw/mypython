# pip install redis

import redis
r = redis.Redis() # host='localhost', port=6379, db=0, 
                  # password=None, socket_timeout=None,...
##r.ping()

# Data are dumped into 'dump.rdb' in working directory when the server
#  is closed or as defined by:
#       save <seconds> <changes>
# If the server is closed and 'dump.rdb' is deleted all data will be lost.

# Redis implements a connection pool, 'r' needs no closing.

def set_test():
    r.set('john', 'john@rambo.com')
    r.set('jack', 'jack@ripper.com')

    print(r.get('john'))
    print(r.get('john').decode()) 
##set_test()

# Close the server and delete 'dump.rdb' then restart.
##print(r.get('john'))

# Delete all
r.flushall()

# List
def list_test():
    r.rpush('a', 'john')
    r.rpush('a', 'jack')
    r.rpush('a', 'joe')
    print(r.lrange('a', 0, 2))  # [b'john', b'jack', b'joe']
    print(r.lrange('a', 0, -1)) # [b'john', b'jack', b'joe']

    print(r.rpop('a'))          # b'joe'
    print(r.lpop('a'))          # b'john'
    print(r.lrange('a', 0, -1)) # [b'jack']
##list_test()

# Set:
def set_test():
    r.sadd('s', 'john')
    r.sadd('s', 'john')
    r.sadd('s', 'jack')
    r.sadd('s', 'joe')
    
    print(r.smembers('s'))      # {b'jack', b'john', b'joe'}
    print(r.sismember('s', 'joe')) # True
##set_test()
        
# Dict:
def dict_test():
    d = { 'john': 'rambo',
          'jack': 'ripper' }
    r.mset(d)

    print(r.get('john'))          # b'rambo'
    print(r.mget('jack', 'john')) # [b'ripper', b'rambo']

    # Update
    r.set('john', 'Rambo')
    print(r.get('john'))        # b'Rambo'

    # Add
    r.set('joe', 'green')
    print(r.get('joe'))         # b'green'

    # Delete
    r.delete('joe')
    print(r.get('joe'))         # None

    # Exists
    print(r.exists('jack'))     # 1
##dict_test()

# Hashes:  (Multiple dict)
def hash_test():
    r.hmset('john', {'sid': 1, 'gpa': 1.5 })
    r.hmset('jack', {'sid': 2, 'gpa': 4.0 })
    
    print(r.hget( 'john', 'gpa' ))          # b'1.5'
    print(r.hmget( 'john', 'sid', 'gpa' ))  # [b'1', b'1.5']

    print(r.hlen( 'john' ))     # 2    
    print(r.hkeys( 'john' ))    # [b'sid', b'gpa']
    print(r.hvals( 'john' ))    # [b'1', b'1.5']
    print(r.hgetall( 'john' ))  # {b'sid': b'1', b'gpa': b'1.5'}
    print(r.hscan( 'john' ))    # (0, {b'sid': b'1', b'gpa': b'1.5'})
    for i in r.hscan_iter('john'):
        print(i, end='  ')      # (b'sid', b'1')  (b'gpa', b'1.5')  
##hash_test()


