''' Suppose the total score is 100 which is accounted from
        10% homework, 40% midterm and 50% final. '''
def to_total(hw, mid, fin):
    return float(hw) + float(mid) * 0.4 + float(fin) * 0.5

'''
Grades is accounted from the total score as the following:
          A if total >= 90, B if total >= 80,
          C if total >= 70, D if total >= 60, else F. '''
def to_grade(total):
    return 'A' if total >= 90 else 'B' if total >= 80 else \
           'C' if total >= 70 else 'D' if total >= 60 else 'F'

import csv
def students_grade():   
    with open('files/data/students.csv') as f:
        for row in csv.DictReader(f):
            total = to_total(row['hw'], row['mid'], row['fin']) 
            print('%s\t%s' % (row['name'], to_grade(total)))
##students_grade()

def read_students(fname):
    with open(fname) as f:
        f_csv = csv.DictReader(f)
        name, hw, mid, fin, total, grade = [], [], [], [], [], []
        for row in f_csv:
            name.append(row['name'])
            hw.append(row['hw'])
            mid.append(row['mid'])
            fin.append(row['fin'])
            t = to_total(row['hw'], row['mid'], row['fin'])
            total.append(t)
            grade.append(to_grade(t))
        return name, hw, mid, fin, total, grade
def read_students_test():
    name, _, _, _, _, grade = read_students('files/data/students.csv')
    print(name)
    print(grade)
##read_students_test()

import numpy as np
from collections import Counter
def students_stats():
    _, _, _, _, total, grade = read_students('files/data/students.csv')
    print('Number of Students: %d' % len(total))
    print('Min: %.2f\tMax: %2.f' % (min(total), max(total)))
    print('Median: %.2f\tMean: %2.f' % (np.median(total), np.mean(total)))
    print('Sd: %.2f' % np.std(total))
    print('Frequency Count:')
    cgd = dict(Counter(grade))
    for g, c in sorted(cgd.items(), key=lambda item: item[0]):
        print('%s: %d' % (g, c))
##students_stats()

#--------------------------------------------------------------
        
import matplotlib.pyplot as pl
from collections import Counter
def students_plots():
    _, _, _, _, total, grade = read_students('files/data/students.csv')
    pl.figure(1)
    pl.title('Bar')
    pl.bar(range(len(total)), total)
    
    pl.figure(2)
    pl.title('Histogram')
    pl.hist(total)

    pl.figure(3)
    pl.title('Pie')
    grade_count = dict(Counter(grade))
    pl.pie(grade_count.values(), autopct='%.1f', labels=('A', 'B', 'C', 'D', 'F'))
    
    pl.show()
##students_plots()

