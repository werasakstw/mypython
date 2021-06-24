# pip install pandas
import pandas as pd

# 'Series' are lists that represent column (of table).
def sr_create():
   # Create from a range().
   # 'dtype' specifies the type of elements.
   print(pd.Series(range(3)))

   # Series may have index, default index is a range().
   print(pd.Series(range(3), index=['A','B','C']))
   
   # Create from a list.
   print(pd.Series([2, 1, 3]))

   # Series elements may be objects.
   print(pd.Series([123, 'John', 3.8]))

   # Series may contain None for absent values, and allows tailing comma.
   print(pd.Series([ 0, None, 3, ]))
##sr_create()

def sr_op():
   sr = pd.Series(range(10))

   # Series info
   print(sr.shape)          # (10,)
   print(sr.size)           # 10
   print(sr.count())        # 10    (excludeing None)
   print(sr.describe())     # statistic info

   # Access elements
   print(sr.values)           # [0 1 2 3 4 5 6 7 8 9]
   print(sr.head().values)    # [0 1 2 3 4]     default is 5 elements
   print(sr.head(3).values)   # [0 1 2]

   # Indexing
   print(sr[0], sr[1], sr[2])  # 0 1 2
   
   # Iteration with 'for' loop or comprehension.
   print([x for x in sr])   # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
##sr_op()

def sr_aggregation():
   sr = pd.Series(range(5))
   
   # Perform operation on each elements.
   print((sr*2).values)                  # [0 2 4 6 8]
   
   # Apply a function to each elements
   print(sr.map(lambda x : x**2).values) # [ 0  1  4  9 16]
##sr_aggregation()

def sr_none():
   sr = pd.Series([0, 1, 2, None, 4])
   print(sr.values)           # [ 0.  1.  2. nan  4.]
   print(sr.count())          # 4

   # Aggregate test for None.
   print(sr.isnull().values)  # [False False False  True False]
   print(sr.notnull().values) # [ True  True  True False  True]
   
   # Removes None.
   print(sr.dropna().values)    # [0. 1. 2. 4.]
   
   # Replaces None with a value.
   print(sr.fillna(-1).values)   # [ 0.  1.  2. -1.  4.]
##sr_none()

#------------------------------------------------------------------

# Dataframe represent a table which is implemented as a dict.
# The syntax is the same as json.
student_table = {  'name': ['John', 'Jack', 'Joe'],
                   'id': [1, 2, 3],
                   'gpa': [3.8, 4.0, 2.7],
                   'dep': ['cs', 'math', 'it'] }

def data_frame():
   df = pd.DataFrame(student_table, columns=['id', 'name', 'dep', 'gpa'])
   print(df)
#                  id  name   dep  gpa
#               0   1  John    cs  3.8
#               1   2  Jack  math  4.0
#               2   3   Joe    it  2.7

   print(df.values)      # list of list (without index).
#               [[1 'John' 'cs' 3.8]
#                [2 'Jack' 'math' 4.0]
#                [3 'Joe' 'it' 2.7]]


   # print(df.head())    # The default is 5 rows. 
   print(df.head(1))
#                     id  name dep  gpa
#                  0   1  John  cs  3.8

   print(df.head(1).values) # [[1 'John' 'cs' 3.8]]  list of lists.
   
   # Projection:
   print(df['name'].values)   # ['John' 'Jack' 'Joe']
   print(df['gpa'].values)    # [3.8 4.  2.7]
   
   # Dot projection (compile time binding).
   print(df.dep.values)       # ['cs' 'math' 'it']  

   # Columns info   
   print(df.info())

   # Statistic for number type columns, exclude object type.
   print(df.describe())    
##data_frame()

# CSV with Pandas:
def csv_pandas():
   # Read CSV:
   df = pd.read_csv('data/students.csv')
   print(df)

   # Write:
   df.to_csv('data/tmp.csv', index=False)
##csv_pandas()

# Sorting with Data Frame
def df_sort():
   df = pd.read_csv('data/students.csv')
   print(df.sort_values(by='name'))
   print()
   print(df.sort_values(by='fin',  ascending=True))
##df_sort()   


def students_st():
    df = pd.read_csv('data/tmp.csv') 

    # 'total' column Statistic:
    t = df.total
    print('min = %.2f, max = %.2f mean = %.2f, median = %.2f, sd = %.2f' % \
          (t.min(), t.max(), t.mean(), t.median(), t.std()))

    # 'total' column Describe:
    print(t.describe())
    # print(t.describe()['std'])  # t.std()

    # Frequency count:
    gc = df.grade.value_counts()        # dict
    # print(fc)
    print([(k,v) for k, v in gc.items()])
##students_st()    

# pip install matplotlib
import matplotlib.pyplot as pp
def students_pie():
    df = pd.read_csv('data/tmp.csv')

    pp.figure(1)
    pp.title('Total Histogram')
    pp.hist(df.total)

    
    pp.figure(2)
    pp.title('Grade Histogram')
    df = df.sort_values(by='grade')
    pp.hist(df.grade)

    pp.figure(3)
    pp.title('Grade Pie')
    gc = df.grade.value_counts()
    pp.pie(gc, autopct='%.1f%%', labels=('C', 'D', 'B', 'A', 'F'))

    pp.show()
##students_pie()


