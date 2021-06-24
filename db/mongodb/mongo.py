# pip install pymongo
import pymongo as pm

def connect():
    try:            # 'mongodb://localhost:27017/'
        connection = pm.MongoClient()
##        print('Connect success.')
    except:
        print('Connect fails.')
    return connection
##print(connect())

# Create 'students' table in the 'mydb' database and insert records.
def init():
    with connect() as con:
        tb = con['mydb']['students']
        print("Create 'students' table success.")
        
        # insert_one()  Records are represented as dict(json).
        tb.insert_one({'name': 'John', 'dep': 'cs', 'gpa': 2.8})
        tb.insert_one({'name': 'Jack', 'dep': 'ee', 'gpa': 4.0})

        # insert_many()
        joe = {'name': 'Joe', 'dep': 'cs', 'gpa': 1.8}
        jim = {'name': 'Jim', 'dep': 'cs', 'gpa': 3.5}
        jame = {'name': 'Jame', 'dep': 'ce', 'gpa': 0.7}
        tb.insert_many([jim, jame, joe])
        print('Insert success.')
##init()

from pprint import pprint
def db_status(): 
   with connect() as con:
       pprint(con['mydb'].command('dbstats'))
##db_status()

def list_tables():  # in the database
   with connect() as con:
       print(con['mydb'].list_collection_names())
##list_tables()

def find_one():
    with connect() as con:
        tb = con['mydb']['students']
        pprint(tb.find_one()) # '_id' is automatically created.
##find_one()

def find_all():
    with connect() as con:
        tb = con['mydb']['students']
        for r in tb.find():
##        for r in tb.find().limit(2):
##        for r in tb.find().skip(2):
            pprint(r)
##            print(r['name'])
##find_all()

def filter_test():
    with connect() as con:
        tb = con['mydb']['students']
        
        # find(<filter>)
        for s in tb.find({'dep': 'cs'}):
##        for s in tb.find({'gpa': {"$lt": 2.0}}):
##        for s in tb.find({'name': {'$regex': '^Ja'}}):

        # find(<filter>, <projection>)
##        for s in tb.find({}, {'name', 'gpa'}):
##        for s in tb.find({}, {'_id': False, 'name': True, 'gpa': True}):
            pprint(s)
##filter_test()

def cursor_test():
    with connect() as con:
        tb = con['mydb']['students']
        cs = tb.find({}, {'_id': False, 'name': True})
        # 'cs' starts at before first and move after next().
        print(cs.next()['name'])    # John
        print(cs.next()['name'])    # Jack
        
        cs.rewind() # back to the beginning.
        print(cs.next()['name'])    # John

        # index, cursor does not moved.
        cs.rewind()
        print(cs[0]['name'], cs[1]['name']) # John Jack

        # iterate
        for i in cs:
            print(i['name'], end=', ')
        print()             # John, Jack, Jim, Jame, Joe,
        # The 'cs' is run out after iteration.
        
        # slice
        cs.rewind()
        for i in cs[1:3]:
            print(i['name'], end=', ')  # Jack, Jim, 
##cursor_test()

def delete_test():
    with connect() as con:
        tb = con['mydb']['students']

        # Delete the first one:
        tb.delete_one({'dep': 'cs'})

        # Delete many:
        x = tb.delete_many({'gpa': {"$lt": 2.0}})
        print(x.deleted_count)

        find_all()
##delete_test()

def update_test():
    with connect() as con:
        tb = con['mydb']['students']

        # update_one()
        condition = { 'name': 'Jim' }
        new_value = { "$set": { 'dep': 'it' } }
        # tb.update_one(condition, new_value)

        # update_many()
        tb.update_many(
            {'gpa': {"$lt": 2.0}},
            { '$set': {'isPro': True}}
        )
        find_all()
##update_test()

def sort_test():
    with connect() as con:
        tb = con['mydb']['students']
        
        for s in tb.find().sort('name'): 
        # for s in tb.find().sort('name', -1):
        # for s in tb.find().sort('name', pm.DESCENDING):  # ASCENDING
            print(s['name']) 
##sort_test()

def json_test():
    with connect() as con:
        tb = con['mydb']['students']
        # A cursor is an cursor object.
        cs = tb.find({}, {'_id': False, 'name': True, 'gpa': True})
##        print(list(cs))     #  list of dict.

        for d in cs:
            print(d)
##json_test()

def drop_table():
    with connect() as con:
        con['mydb']['students'].drop()
    print('Drop table success.')
##drop_table()
