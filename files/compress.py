
# Read/Write a file:
def read_file(fname):
    with open(fname, 'r') as f:
        doc = f.read()
    return doc
def write_file(fname, doc):
    with open(fname, 'w') as f:
        f.write(doc)

# GZip a file:
import gzip, os
def gzip_test():
    inp = 'data/students.csv'
    doc = read_file(inp)
    print(os.stat(inp).st_size)
    
    with gzip.open('tmp/students.gz', 'wb') as f:
        f.write(doc.encode())
    print(os.stat('tmp/students.gz').st_size)

    with gzip.open('tmp/students.gz', 'rb') as f:
         print(f.read().decode())
##gzip_test()

##------------------------------------------------------------##
        
## Zip files:
import zipfile
def zipfile_test():
    with zipfile.ZipFile( "tmp/students.zip", "w" ) as f:
        f.write('data/students.csv')
        f.write('data/students.json')

    with zipfile.ZipFile( "tmp/students.zip", "r" ) as f:
        f.printdir()             # print all zipped file names
##        print(f.read('data/students.csv').decode())  # extract a specified file
##        f.extractall()         #  extract all files to current directory
##zipfile_test()
