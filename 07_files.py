
import os
def rename_files():
    wd = 'files/txt/'
    for f in os.listdir(wd):
        if f.endswith('.txt'):
            n = f.replace('test_data', 'data')
            os.rename(wd+f, wd+n)
            print(n)
##rename_files()

#-----------------------------------------------------

def image_conversion():
    with open('files/images/john.png', 'rb') as rf:
        data = rf.read()
        with open('files/images/john.jpg', 'wb') as wf:
            wf.write(data)
##image_conversion()

#------------------------------------------------------

# Multiplication Tables.
def mul_tables_file(n):
    with open('files/tmp/mul.txt', 'w') as f:
        for i in range(2, n):
            for j in range(2, 13):
                f.write('%3d x %2d = %4d\n' % (i, j, i*j))
            f.write('\n')
##mul_tables_file(100)

#-------------------------------------------------------

import random
def kumon_file(n):
    ops = ['+', '-', '*', '/']
    def gen_question():        
        x = random.randrange(1, 100)
        op = random.choice(ops)
        y = random.randrange(1, 100)
        return (x, op, y)
 
    with open('files/tmp/kumon.txt', 'w') as f:
        for q in range(n):
            f.write('%2d %s %2d =\n' % gen_question())
##kumon_file(100)

#-------------------------------------------------------

students = [ (1, 'John Rambo', 6, 78, 82),
             (2, 'Jack Ripper', 10, 97, 91),
             (3, 'Joe Green', 8, 87, 82),
             (4, 'Jame Bond', 3, 67, 78),
             (5, 'Jet Ready', 7, 76, 65),
             (6, 'Janet Long', 4, 86, 78),
             (7, 'Jessie Howdy', 0, 42, 52),
             (8, 'Jim Morrison', 9, 79, 73),
             (9, 'Judy Anne', 6, 84, 81),
             (10, 'Jude Zebra', 7, 72, 83),
            ]
def txt_test():
    # Write txt file.
    with open('files/tmp/students.txt', 'w') as f:
        for s in students:  
            _id, name, hw, mid, fin = s
            print(_id, name, hw, mid, fin, file=f)
            
    # Read txt file.
    with open('files/tmp/students.txt', 'r') as f:
        # Read the whole file.
##        print(f.read())

        # Read by line.
##        for line in f:
##            print(line, end='')     #  end='' suppress '\n'.

        # Split line
        for line in f:
            _id, first_name, last_name, hw, mid, fin = line.split()
            print(_id, first_name, last_name, hw, mid, fin)
##txt_test()

#---------------------------------------------------------------------

import csv
def csv_test():
    with open('files/tmp/students.csv', 'w', newline='\n') as f:
        wt = csv.writer(f)
        wt.writerow(['id', 'name', 'hw', 'mid', 'fin']) # Header
        for s in students:
            wt.writerow(s)
           
    with open('files/tmp/students.csv') as f:
        data = csv.DictReader(f)    # Read into a dict
        for r in data:
            print(r['id'], r['name'], r['hw'], r['mid'], r['fin'])
##csv_test()
   
