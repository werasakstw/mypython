# File Path.
# File Path as String (for Windows).
print('c:\\tmp\\test.txt')          # c:\tmp\test.txt

import os
# File path separator in the current operating system.
print(os.sep)           # \

# File extension separator.
print(os.extsep)        # .

# Directory:
# Current directory symbol.
print(os.curdir)        # .

# Parent directory symbol
print(os.pardir)        # ..

# Current Working Directory
cwd = os.getcwd()
print(cwd)

# List names in the current directory
print(os.listdir())

# Change Directory
os.chdir('..')
print(os.getcwd())
os.chdir(cwd)

# Current file path.
print(__file__)

# Create a file path with extension.
f = os.getcwd() + '\\tmp.txt'
print(f)                    # C:\mypython\files\tmp.txt

# Split a file path into a tuple of path and file.   
print(os.path.split(f))     # ('C:\\mypython\\files', 'tmp.txt')

# Split a file path into a tuple of path file  and extension.  
print(os.path.splitext(f))  # ('C:\\mypython\\files\\tmp', '.txt')

# Extract file name (with extension) from a file path.
print(os.path.basename(f))  # tmp.txt

# Extract directory path from a file path.
print(os.path.dirname(f))   # C:\mypython\files

# Create a file path from components.
print(os.path.join('c:','com','mycomp','my.txt')) # c:com\mycomp\my.txt
                           
# Create a file path from the User Directory with expand path.
print(os.path.expanduser('~\\tmp'))  # C:\Users\Mac mini\tmp

#---------------------------------------------------------------------

# File size. (bytes)
print(os.path.getsize(__file__))       # 3860

# Is the file exists?
print(os.path.exists(__file__))        # True

# Full file path.
print(os.path.realpath(__file__))      # C:\mypython\files\info.py

# Is the name is file?
print(os.path.isfile(__file__))        # True

# Is the name is directory?
print(os.path.isdir(__file__))         # False

# Is the name is link?
print(os.path.islink(__file__))        # False

# Is tha name is mounted?
print(os.path.ismount(__file__))       # False

#----------------------------------------------------------------

# 'glob' module has provides accessing files with name matching pattern.
import glob
def lookup(pattern):
    for name in glob.glob(pattern):
        print(name)
##lookup('*.py')
##lookup('file*.py')
##lookup('?????.py')


# List Directory.
# os.listdir(<dir>) returns list of names of file and directory as strings.
import os, fnmatch
def list_dir(d):
    for f in os.listdir(d):
        if os.path.isfile(f):
##            if f.endswith('.py'):     ## Try: startswith()
##            if fnmatch.fnmatch(f, '*py*'):
            print(f)
##list_dir('.')

# Scan Directory.
# os.scandir(<dir>) returns a recursive directory iterator.
def scan_dir(d):
    for f in os.scandir(d):
        if f.is_file():
            print(f.name)
        elif f.is_dir():
            print('\\' + f.name)
            scan_dir(f)
##scan_dir('.')

# Walk Directory.
# os.walk(<dir>) returns a tuple of path, directories and files.
#  path is a str. directories and files are lists.
def walk_dir(d):
    for path, dirs, files in os.walk(d):
        print('%s \t %s' % (path, dirs))
        for f in files:
            print(f)
        print()
##walk_dir('.')

