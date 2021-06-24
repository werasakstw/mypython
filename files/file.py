''' Write/Read File:
Files must be write/read via file reference.
open(<file path>, <mode>) returns the opened file reference,
some named arguments are allowed.
  e.g. open('file', 'r', newline='')
       open('file', 'w', encoding='ascii')
       open('file', 'r', errors='replace')

    Modes:
      'r' Read text file (default)
      'w' Write text file (truncates if exists)
      'x' Write text file, throw  FileExistsError if exists.
      'a' Append to text file (write to end)
      'rb' Read binary file
      'wb' Write binary (truncate)
      'w+b' Open binary file for reading and writing
      'xb' Write binary file, throw  FileExistsError if exists.
      'ab' Append to binary file (write to end)
'''
def open_test():
    # If the file already exists it will be overriden.
    f = open('tmp/tmp.txt', 'w')
    print(f.name)       # tmp/tmp.txt
    print(f.mode)       # w
    print(f.closed)     # False
    
    f.write('Hello\nHow are you today?')
    f.close()
    print(f.closed)     # True
    # A file must be closed before it can be reopened.

    f = open('tmp/tmp.txt', 'r')
    print(f.read())         # read the whole file
    # print(f.readline())   # read one line

    # All opened files will be closed when Python VM is shutdown.
    # f.close()
##open_test()

#  Write/Read File should be within a 'try' block.
def read_try():
    ## f = None          # Not needed anymore.
    try:
        f = open('tmp/tmp.txt', 'r')
        print(f.read())
    except FileNotFoundError as err:
        print(err)
    finally:
        if f is not None:
            f.close()
##read_try()

# Context Managers provide automatic file closing.
def write_read():
    # write
    with open('tmp/tmp.txt', 'w') as f:  # The 'data' directory must exist.
        f.write('Hello how do you do?')   # write() does not append '\n' to the end of line.
        
    # read
    with open('tmp/tmp.txt', 'r') as f:
        print(f.read())         # reads the whole file.
##write_read()

''' Good Practice Write/Read File.
- File existing should be checked.
- Write/Read operations should be within a 'try' block.
'''
import os
def write_file(file, data):
    if os.path.exists(file):
        return 'The file already exists.'
    try:       
        with open(file, 'w') as f:
            f.write(data)
        return 'Write Success'
    except FileNotFoundError as er:
        return er
def read_file(file):
    try:       
        with open(file, 'r') as f:
            return f.read()
    except FileNotFoundError as er:
        return er
##print(write_file('tmp/tmp.txt', 'Hello'))
##print(read_file('tmp/tmp.txt'))

#---------------------------------------------------------

# Creates Directory: error if the directory exists.
def make_dir(d):
    try:
        os.mkdir(d)
    except FileExistsError as e:
        print(e)
##make_dir('temp')

# Remove Directory: error if the directory does not exist
#   or the directory is not empty.
##os.rmdir('temp')

# Remove Tree: error if the directory does not exist.
import shutil
##shutil.rmtree('temp')

#----------------------------------------------------------

# Copy Files.
def copy_file(src, tar):
    if os.path.isdir(src):
        return '<src> must be a file.'
    if os.path.isdir(tar):
        return '<tar> must be a file.'
    if os.path.exists(tar):
        return '<tar> already exists.'
    try:
        data = None
        with open(src, 'r') as f:
            data = f.read()
        with open(tar, 'w') as f:
            f.write(data)
        return 'Success'
    except FileNotFoundError as er:
        return er
##print(copy_file('tmp/tmp.txt', 'tmp/target.txt'))
##print(copy_file('tmp/tmp.txt', 'tmp'))

''' shutil.copy(<src>, <tar>) 
<src> must be a file or file path.
If <tar> is an already exist file, it will be overwritten.
If <tar> is a directory, <src> will be copied to the directory.
The file's contents and permissions are copied, but not other meta data.
'''
##shutil.copy(__file__, 'tmp/tmp.py')

# Remove File.
# os.remove(<file>): error if <file> does not exist.
##os.remove('tmp/tmp.py')

# Copy Directory:
# shutil.copytree(<src>, <tar>): returns an error if <src> does not exist
# or <tar> already exists.
##shutil.copytree('txt', 'tmp/tmp')

# Rename File:
# os.rename(<old>, <new>): error if <old> does not exist or <new> already exists.
##os.rename('tmp/tmp.py', 'tmp/tmp1.py')

# Move File:
# shutil.move(<src>, <tar>) : error if <tar> directory does not exist
# <src> may be file or directory.
# If <src> and <tar> are files it is a renaming.
##shutil.move('tmp/tmp1.txt', 'tmp/tmp2.txt')

#----------------------------------------------------------

''' 'Temp Files' are used for temporary data which cannot be accessed by other processes.
It is not likely that someone can guess the temp file names and steal the data.
'''
import tempfile, linecache
def tempfile_test():
    fd, fname = tempfile.mkstemp()
    os.close(fd)       # To allow unlink the file.
    print(fname)       # temp file names are generated randomly.
    print(tempfile.gettempdir())    # C:\WINDOWS\TEMP
    print(tempfile.gettempprefix()) # tmp

    with open(fname, 'w') as f:
        f.write('Hello!\nGoodbye.')
    with open(fname, 'r') as f:
        print(f.read())

    # 'linecache' allows simple reading at specified line number.
    print(linecache.getline(fname, 1))   # line number starts with 1.
    print(linecache.getline(fname, 2))

    # Unlink and remove the temp file.
    os.unlink(fname)
##tempfile_test()

''' Temp files be created, write, read, closed and removed within a
'with' block there is no ways to refer to the file later. '''
def temp_file():
    with tempfile.TemporaryFile(mode='w+t') as f:
        f.write("What's up?")
        # After writing, the file must be reset.
        f.seek(0)  
        print(f.read())
##temp_file()

##-------------------------------------------------------

''' String IO: is a string that can be used as a file.
which are faster and more secure than temp files. '''
import io
def string_io():
    s = io.StringIO()
    s.write('Hello! ')
    print(s.getvalue())     # Hello!

    # Print to a string io.
    print('John', end='', file=s)
    print(s.getvalue())     # Hello! John
##string_io()

#----------------------------------------------------------------

''' Txt File.
Python's file reading operates in 'universal newline' mode, that means
all newline characters are converted to \n while reading.
Windows text files have '\r\n' as the end of line symbol.
'''
def print_file():
    with open('tmp/test.txt', 'w') as f:
        # write() does not append '\n' to the end of line.
        f.write('Hello')
        f.write('John')
  
        # print() always writing to a file and allow appening '\n' to the end of line. 
        print('Hello', file=f)
        print('Jack', file=f)

    # print() also allows attribute 'end'.
    with open('tmp/test.txt', 'r') as f:
        for line in f:
            print(line, end='') # end='' suppress '\n'.  
##print_file()

#----------------------------------------------------------##

''' Write/Raed Binary.
Python arrays are sequences of homogeneous binary values,
e.g. unicode, int or float
An array must have a 'type code' for interpreting its stored values.
Type code       Underline Type    Minimum size in bytes 
  'b'         signed integer              1 
  'B'         unsigned integer            1 
  'u'         Unicode character           2
  'h'         signed integer              2 
  'H'         unsigned integer            2 
  'i'         signed integer              2 
  'I'         unsigned integer            2 
  'l'         signed integer              4 
  'L'         unsigned integer            4 
  'q'         signed integer              8 
  'Q'         unsigned integer            8 
  'f'         floating point              4 
  'd'         double-precision float      8
Homogeneous binary files use less space but not human readable.
'''
import array
def array_test(size):
    a = array.array('i', range(size))
    with open('tmp/test.bin', 'wb') as f:
        a.tofile(f)

    b = array.array('i')
    with open('tmp/test.bin', 'rb') as f:
        b.fromfile(f, size)
    print(b)
    print(list(b))
##array_test(5)

# Byte Array.
def byte_array():
    ''' 'bytes' is an immutable array of bytes.
        encode() converts str to 'bytes'. 
        decode() converts 'bytes' to str. '''
    b = '01234'.encode()
    print(len(b), b.decode()) # 5 b'01234' 01234
    
    b = bytes(range(5))
    print(len(b), b)           # 5 b'\x00\x01\x02\x03\x04'

    # 'bytesarray' is a mutable array of bytes.
    ba = bytearray(range(5))
    print(len(ba), ba)         # 5 bytearray(b'\x00\x01\x02\x03\x04')

    s1, s2 = 'ABC', 'กขค'
    # 'str' are iterated by character.
    for c in s1:
        print(c, end=',')       # A,B,C,
    print()
    for c in s2:
        print(c, end=',')       # ก,ข,ค,
    print()
    
    # 'bytes/bytesarray' are iterated by byte.
    for c in s1.encode():       # 65,66,67,
        print(c, end=',')
    print()
    for c in s2.encode():
        print(c, end=',')       # 224,184,129,224,184,130,224,184,132,
    print()
    
    # 'bytes/bytesarray' should be write/read as a whole.
    with open('tmp/bytes.bin', 'wb') as f:
        f.write(b)
    with open('tmp/bytes.bin', 'rb') as f:
        print(f.read())         # b'\x00\x01\x02\x03\x04'
##byte_array()
    
# Pickling is the process of saving objects to files.
import pickle
def pickle_test():
    a = list(range(5))
    
    with open('tmp/obj.bin', 'wb') as f:
        pickle.dump(a, f)
        
    with open('tmp/obj.bin', 'rb') as f:
        print(pickle.load(f))
##pickle_test()

#-----------------------------------------------------------

# Structured Data Txt File.
def txt_test():
    with open('data/students.txt', 'r') as f:
        for line in f:  
            _id, name, hw, mid, fin = line.split()
            print(_id, name, hw, mid, fin)
##txt_test()

#-----------------------------------------------------------

# Xml.
# Xml simple tag:   <tag>value</tag>
# Xml tag:   <tag attribute=<attr> ...>value</tag>
# Xml requires parser to access data.
from xml.etree import ElementTree
def xml_test():
    with open('data/students.xml') as f:
        doc = ElementTree.parse(f)
        for s in doc.findall('student'):
            _id = s.find('id').text
            name = s.find('name').text
            dep = s.find('department').text
            print(_id, name, dep)
##xml_test()

#-----------------------------------------------------------

# Json:
# Json and Xml are equally expressive but Json uses less memory for the same data.
# Json can be easily converted to Javascript object or Python dict.
import json
def json_test():
    # Python dict: is a set of elements in the form of <key>:<value>.
    # <key> must be hashable, e.g. int, float, tuple or str.
    # 'str' may be single, double, or triple quoted.
    john_dict = {'id': 123, 'name': 'John Rambo', 'gpa': 1.8 }
    # Dict element sequence is no matter.
    print(john_dict == {'name': 'John Rambo', 'gpa': 1.8, 'id': 123})  # True

    # Json syntax is a sequence of elements in the form of <name>:<value>.
    # <name> must be double quoted string.
    # json.dumps(<dict>): <dict> -> json_str
    john_json = json.dumps(john_dict)
    print(john_json)     # {"id": 123, "name": "John Rambo", "gpa": 1.8}
    # Json element sequence is matter.
    print(john_json == {"name": 'John Rambo', "gpa": 1.8, "id": 123})  # False

    # json.loads(<json_str>): <json_str> -> dict
    print(json.loads(john_json))   # {'id': 123, 'name': 'John Rambo', 'gpa': 1.8}

    # Dict can be dump/load to a file as json.
    with open('data/john.json', 'w') as f:
        json.dump(john_dict, f)
    with open('data/john.json', 'r') as f:
        print(json.load(f))
##json_test()

# Structured Data Json:
def json_file():
    with open('data/students.json') as f:
        for s in json.loads(f.read()):
            _id = s['id']
            name = s['name']
            department = s['department']
            print(_id, name, department)
##json_file()

#-----------------------------------------------------------

# CSV:
import csv
def csv_reader():
    with open('data/students.csv') as f:   # Default mode is 'r'
        data = csv.reader(f)
        header = next(data)
        print(header)       # print(header[0], header[1], header[2], header[3], header[4])   
        for row in data:
            print(row)      # print(row[0], row[1], row[2], row[3], row[4])
##csv_reader()

def csv_dic_reader():
    with open('data/students.csv') as f:
        data = csv.DictReader(f)    # a dict
        for r in data:
##            print(r)
            print(r['id'], r['name'], r['hw'], r['mid'], r['fin'])
##csv_dic_reader()

header = ['id', 'name', 'hw', 'mid', 'fin']
students = [ [1, 'John Rambo', 6, 78, 82],
             [2, 'Jack Ripper', 10, 97, 91],
             [3, 'Joe Green', 8, 87, 82] ]
# CSV Writer: the file must opened with:
#   open(<file>, <mode>='w', <newline>='\r\n')
def csv_writer():
    with open('tmp/students.csv', 'w', newline='\n') as f:
        wt = csv.writer(f)
        wt.writerow(header)
        for s in students:
            wt.writerow(s)
##csv_writer()

# quoting:
# csv.QUOTE_ALL, csv.QUOTE_NONE, csv.QUOTE_NONNUMERIC
# csv.QUOTE_MINIMAL (default) quote only if it contain delimiter or quotechar. 
def tsv_writer():
    with open('tmp/students.tsv', 'w', newline='\n') as f:
        wt = csv.writer(f, delimiter='\t', quotechar="'", quoting=csv.QUOTE_NONNUMERIC)
        wt.writerow(header)
        for s in students:
            wt.writerow(s)
##tsv_writer()

# CSV Dict Writer:
def csv_dic_writer():
    with open('tmp/s.csv', mode='w', newline='\n') as f:
        header = ['id', 'name', 'gpa']
        wt = csv.DictWriter(f, fieldnames=header)
        wt.writeheader()
        wt.writerow({'id': 1, 'name': 'John Rambo', 'gpa': 1.8})
        wt.writerow({'id': 2, 'name': 'Jack Ripper', 'gpa': 4.0})
##csv_dic_writer()

#-------------------------------------------------------------------
'''
# pip install xlwt

# Excel Writer:
import xlwt
def excel_wr():
    wb = xlwt.Workbook()
    s1 = wb.add_sheet('Sheet 1')
    s1.write(0, 0, 'id'); s1.write(0, 1, 'name'); s1.write(0, 2, 'gpa')
    s1.write(1, 0, 1); s1.write(1, 1, 'John'); s1.write(1, 2, 1.8)
    s1.write(2, 0, 1); s1.write(2, 1, 'Jack'); s1.write(2, 2, 4.0)
    s1.write(3, 0, 1); s1.write(3, 1, 'Joe'); s1.write(3, 2, 2.8)
    wb.save('tmp/tmp.xlsx')
##excel_wr()

# pip install xlrd

# Excel Reader:
import xlrd
def excel_rd():
    wb = xlrd.open_workbook('tmp/tmp.xlsx')
    print([sheet.name for sheet in wb.sheets()])    # ['Sheet 1']
    
    s1 = wb.sheet_by_name('Sheet 1')    # Sheet 1
    print(s1.name)
    print(s1.nrows, s1.ncols)           # 4 3

    print([s1.row_values(i) for i in range(s1.nrows)])
    # [['id', 'name', 'gpa'], [1.0, 'John', 1.8], [1.0, 'Jack', 4.0], [1.0, 'Joe', 2.8]]

    print([c for c in s1.row_values(1)]) # [1.0, 'John', 1.8]
##excel_rd()
'''
