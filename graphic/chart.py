
import matplotlib.pyplot as pp
import numpy as np

# Bar Charts:
def bar():
    x = range(10) # must be the same size
    y = [7, 2, 5, 3, 3, 8, 9, 1, 2, 3]
    pp.bar(x, y)     
    
    # Stem plots draw a vertical line from (x, 0) to (x, y).
##    pp.stem(x, y)
    
    pp.show()
##bar()

# Stacked Bar Charts:
import random
def stack_bar():
    x = range(10)
    y1 = [random.randint(1, 5) for _ in x]
    y2 = [random.randint(1, 5) for _ in x]
    pp.bar(x, y1, color='g') 
    pp.bar(x, y2, bottom=y1, color = 'r')
    pp.show()
##stack_bar()

# Histograms: Plots number of occurrences for each values.
def histogram():
    y = [2, 4, 5, 4, 2, 2, 4, 1, 4, 1]
    pp.hist(y)
    pp.show()
##histogram()

# Pie Charts:
def pie():
    d = [20, 40, 10, 30] # The sum must be 100.
    pp.pie(d)
    pp.show()
##pie()

def pie_config1():
    d = [5, 15, 40, 30, 10]  

    pp.subplot(221)
    pp.pie(d)                           # default

    pp.subplot(222)
    pp.pie(d, autopct='%1.1f%%')        # show percentage

    pp.subplot(223)    
    pp.pie(d, colors=('r', 'g', 'b', 'y', 'm'))   # colors: default=('b', 'g', 'r', 'c', 'm', 'y', 'k', 'w')

    pp.subplot(224)
    grades = ('A', 'B', 'C', 'D', 'F')
    pp.title('OOP Spring 2017')         # labels and title
    pp.pie(d, autopct='%1.1f%%', labels=grades)
    
    pp.show()
##pie_config1()

# Box Plot
# A box shows <min>-<lower>-<median>-<upper>-<max> values.  
def box_plot():
    # d = [2, 1, 5, 4, 3]
    d = [[2, 1, 5, 4, 3], [2, 1, 1, 4, 3], [2, 4, 5, 3, 6]]
    pp.boxplot(d)
    pp.show()
# box_plot()

def stock_box():
    with open('data/stock.csv') as f:
        f_csv = csv.DictReader(f)
        s = []
        for row in f_csv:
            # print([row['v1'], row['v2'], row['v3'], row['v4'], row['v5']])
            s.append([int(row['v1']), int(row['v2']), int(row['v3']), int(row['v4']), int(row['v5'])])
        pp.boxplot(s, labels=('abc', 'ddd', 'xyz', 'cnn', 'mtv', 'ptt'))
        pp.show()
##stock_box()

# Scatter Plot:
# Scatter plots display points (x, y) that are not related by any known functions.
# A scatter plot is often used to visual the correlation or
#  a potential association between two variables.
def scatter_ex():
    # The controlled x values
    x = np.random.randn(1000)

    # random measurements, no correlation
    y1 = np.random.randn(len(x))
    
    # some (unknow function) correlation
    y2 = np.exp(x) - x/1.3

    pp.subplot(121)
    pp.scatter(x, y1)

    pp.subplot(122)
    pp.scatter(x, y2)
    pp.show()
##scatter_ex()

# Logarithmic Plots:
# semilgox() and semilogy() plot the x-axis and y-axis in logarithmic scale.
# loglog() plot both the x-axis and y-axis in logarithmic scale.

# np.logspace() generates logarithmically spaced values between 10**start and 10**stop.
# num specifies how many values in the range.
# print(np.logspace(1, 5, num=3))

def logplot():
    energy = np.logspace(1, 5, num=10)
    decibels = [ 20*np.log10(x) for x in energy]
    
    pp.subplot(121)
    pp.semilogy(decibels, energy)

    pp.subplot(122)
    pp.scatter(decibels, energy)
    
    pp.show()
##logplot()
