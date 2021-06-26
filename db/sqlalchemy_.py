# pip install sqlalchemy

import sqlalchemy as sq
##print(sq.__version__)
                        
en = sq.create_engine('sqlite:///mydb.db')  # , echo=True)
                   # 'dialect+driver://user:pwd@host:port/dbnamr'
def create_table():
    md = sq.MetaData()
    sq.Table('students', md, 
        sq.Column('sid', sq.Integer, primary_key = True), 
        sq.Column('name', sq.String), 
        sq.Column('dep', sq.String),
        sq.Column('gpa', sq.Float)
    )
    md.create_all(en)
    print('Create table success.')
##create_table()

def load_table(tname):
    return sq.Table(tname, sq.MetaData(), autoload=True, autoload_with=en)

def insert(rec):  # 'rec' is a record represented as json.
    tb = load_table('students')
    with en.connect() as con:
        con.execute(tb.insert(), rec)
    print('Insert:', rec)
##insert( {'sid': 1, 'name':'John', 'dep' : 'ee', 'gpa': 1.8} )
       
def init():
    tb = load_table('students')
    with en.connect() as con:
        con.execute(tb.insert(), [
           {'sid': 2, 'name': 'Jack', 'dep': 'cs', 'gpa': 4.0},
           {'sid': 3, 'name': 'Joe', 'dep': 'ce', 'gpa': 2.8},
           {'sid': 4, 'name': 'Jame', 'dep': 'it', 'gpa': 0.5},
           {'sid': 5, 'name': 'Jim', 'dep': 'cs', 'gpa': 3.8},
           {'sid': 6, 'name': 'Judy', 'dep': 'cs', 'gpa': 3.2}
        ])
    print('Init success.')
##init()

def list_all():
    tb = load_table('students')
    q = tb.select()
    with en.connect() as con:
        for r in con.execute(q):
            print(r)
##list_all()
            
def fetch():  # Return a list of records(tuples).
    q = load_table('students').select()
    with en.connect() as con:
        return con.execute(q).fetchall()
##print(fetch())

def list_pro():
    tb = load_table('students')
    q = tb.select().where(tb.c.gpa < 2.0)   # 'c' is alias for column.
    with en.connect() as con:
        for r in con.execute(q):
            print(r)
##list_pro()

def get_by_name(name):
    tb = load_table('students')
    q = tb.select().where(tb.c.name == name)
    with en.connect() as con:
        return con.execute(q).fetchall()[0]
##print(get_by_name('Jame'))

def update(name, gpa):
    tb = load_table('students')
    q = tb.update().where(tb.c.name==name).values(gpa=gpa)
    with en.connect() as con:
        con.execute(q)
    list_all()
##update('Jame', 2.1)

def delete_by_name(name):
    tb = load_table('students')
    q = tb.delete().where(tb.c.name==name)
    with en.connect() as con:
        con.execute(q)
    list_all()
##delete_by_name('Jame')


