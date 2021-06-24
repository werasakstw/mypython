import pandas as pd
import csv

def to_total(hw, mid, fin):
    return float(hw) + float(mid) * 0.4 + float(fin) * 0.5
def to_grade(total):
    return 'A' if total >= 90 else 'B' if total >= 80 else \
           'C' if total >= 70 else 'D' if total >= 60 else 'F'

def students_grade():
    df = pd.read_csv('statistics/data/students.csv')

    # Dataframes allow adding new columns.
    # Create 'total' column:  total = hw + 40% mid + 50% fin
    df['total'] = (df.hw) + (0.4 * df.mid) + (0.5 * df.fin)

    # Create 'grade' column:
    df['grade'] = df['total'].map(to_grade)

    # Sort by total.
    df = df.sort_values(by='total',  ascending=False)
    print(df)

    # Save:
    df.to_csv('statistics/data/tmp.csv', index=False)
##students_grade()

import statistics as st
import numpy as np
def students_stats():
    df = pd.read_csv('statistics/data/tmp.csv')
    td = df.total.describe()
    print('Number of Students: %d' % td['count'])
    print('Min: %.2f\tMax: %2.f' % (td['min'], td['max']))
    print('Median: %.2f\tMean: %2.f' % (np.median(df.total), td['mean']))
    print('Sd: %.2f, %.2f, %.2f' % (td['std'], np.std(df.total), st.pstdev(df.total)))
    print('Frequency count:')
    gc = df.grade.value_counts()        # dict
    for g, c in sorted(gc.items(), key=lambda item: item[0]):
        print('%s: %d' % (g, c))
##students_stats()  

import matplotlib.pyplot as pl
def students_plot():
    df = pd.read_csv('statistics/data/tmp.csv')

    pl.figure(1)
    pl.title('Total Bar')
    pl.hist(df.total)

    
    pl.figure(2)
    pl.title('Grade Bar')
    df = df.sort_values(by='grade')
    pl.hist(df.grade)

    pl.figure(3)
    pl.title('Pie')
    gc = df.grade.value_counts()
    pl.pie(gc, autopct='%.1f%%', labels=('C', 'D', 'B', 'A', 'F'))

    pl.show()
##students_plot()


