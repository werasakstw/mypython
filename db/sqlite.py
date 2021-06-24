import sqlite3
# Sqlite GUI: https://sqlitestudio.pl/

def create_init():
    # 'with' context provides automatic closing.
    with sqlite3.connect('mydb.db') as con:     # 'mydb.db' is created in working dir.
        cur = con.cursor()  # A cursor is created from the connection.
        # SQL is sent through the cursor.
        cur.execute('''CREATE TABLE students (id INT, name TEXT, gpa REAL)''')
        cur.execute('''INSERT INTO students VALUES(1, 'John Rambo', 0.9)''')
        cur.execute('''INSERT INTO students VALUES(2, 'Jack Ripper', 4.0)''')
        cur.execute('''INSERT INTO students VALUES(3, 'Joe Green', 2.3)''')
        con.commit() # The connection must be commited to save the data.
##create_init()

def list_all():
    with sqlite3.connect('mydb.db') as con:
        cur = con.cursor()
        for r in cur.execute('SELECT * FROM students'):  # Return a cursor iterator.
            print(r)    # A record is a tuple.
##list_all()

def find_by_name(name):
    qt = 'SELECT * FROM students WHERE name = ?'  # A query template.
    with sqlite3.connect('mydb.db') as con:
        cur = con.cursor()
        for r in cur.execute(qt, (name,)):
            print(r)
##find_by_name('Jack Ripper')

def insert(rec):
    qt = 'INSERT INTO students VALUES(?, ?, ?)'
    with sqlite3.connect('mydb.db') as con:
        cur = con.cursor()
        cur.execute(qt, rec)
        con.commit()
    list_all()
##insert((4, 'Jame Bond', 1.6))

def update(name, gpa):
    qt = 'UPDATE students SET gpa = ? WHERE name = ?'
    with sqlite3.connect('mydb.db') as con:
        cur = con.cursor()
        cur.execute(qt, (gpa, name))
        con.commit()
    list_all()
##update('Jame Bond', 3.8)

def delete_by_name(name):
    qt = 'DELETE FROM students WHERE name = ?'
    with sqlite3.connect('mydb.db') as con:
        cur = con.cursor()
        cur.execute(qt, (name,))
        # No error if the name is not found or the table is empty.
        con.commit()
    list_all()
##delete_by_name('Jame Bond')

def delete_all():
    with sqlite3.connect('mydb.db') as con:
        cur = con.cursor()
        cur.execute('DELETE FROM students')
        # No error if the table is empty.
        con.commit()
    list_all()
##delete_all()

def drop_table(tname):
    with sqlite3.connect('mydb.db') as con:
        cur = con.cursor()
        cur.execute('DROP TABLE '+ tname)
        # error: if no table
        con.commit()
##    list_all()  # error: no table
##drop_table('students')
