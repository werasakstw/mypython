# pip install matplotlib
import matplotlib.pyplot as pl

# Define x and y axises as list.
# The lists must have the same size.
def xy_plot():
    x = [1, 5, 10, 14, 19]
    y = [1, 0, 4, 2, 5]
    pl.plot(x, y)
    pl.show()
##xy_plot()

# Default x-axis is [0, 1, 2, ...].
def default_x():
    y = [2, 3, 0, 5]
    pl.plot(y)    
    pl.show()
##default_x()

# Multiple y axises on a default x-axis.
def mul_y():
    y1 = [0, 3, 2, 4]
    y2 = [1, 0, 1, 6]
    pl.plot(y1)
    pl.plot(y2)
    pl.show()
##mul_y()

# Separate graphs on a frame.
def sep_plot():
    x1 = range(0, 4)
    x2 = range(0, 10, 3)
    y1 = [0, 3, 1, 4]
    y2 = [1, 0, 2, 5]
    pl.plot(x1, y1, x2, y2)
    pl.show()
##sep_plot()

# Separate frames.
# A frame is defined as a figure.
def sep_frame():
    pl.figure(1)            
    pl.plot([3, 2, 5])
    pl.title('Figure 1')

    pl.figure(2)
    pl.plot([1, 3, 1, 2])
    pl.title('Figure 2')
    pl.show()
##sep_frame()

# Sub plots in a frame.
def sub_plot():
    pl.figure()     # create a new figure
    
    pl.subplot(221) # divide subplots into 2 x 2 grid and select no. 1
    pl.title('Figure 1')
    pl.plot([1, 2, 0, 4])

    pl.subplot(222) # select no. 2
    pl.title('Figure 2')
    pl.plot([6, 3, 5, 2])
    
    pl.subplot(223) # select no. 3
    pl.title('Figure 3')
    pl.plot([2, 1, 5, 2])

    pl.tight_layout()   # Add margin between subplots.
    pl.show()
##sub_plot()

xr = range(10)
y1 = [i for i in xr]
y2 = [i*2 for i in xr]
y3 = [i*3 for i in xr]
y4 = [i*4 for i in xr]
y5 = [i*5 for i in xr]
y6 = [i*6 for i in xr]
y7 = [i*7 for i in xr]
y8 = [i*8 for i in xr]

def color_test():
    pl.plot(y1, color='b')          # Blue (default)
    pl.plot(y2, color='tab:orange') # Orange
    pl.plot(y3, color='g')          # Green
    pl.plot(y4, color='r')          # Red
    pl.plot(y5, color='tab:purple') # Purple
    pl.plot(y6, color='tab:brown')  # Brown
    pl.plot(y7, color='tab:pink')   # Pink
    pl.plot(y8, color='tab:gray')   # Gray
                                    # 'tab:olive' Olive
                                    # 'c' Cyan
                             # 'k' Black
                             # 'w' White
                             # 'm' Magenta
                             # 'y' Yellow
        # RGB   #rrggbb
        # RGBA  #rrggbbaa
    pl.show()
##color_test()

def linewidth_test():
    pl.plot(y1)             # default: 1
    pl.plot(y2, linewidth=2)
    pl.plot(y3, lw=3)
    pl.plot(y4, lw=4)
    pl.plot(y5, lw=5)
    pl.show()
##linewidth_test()

def alpha_test():
    pl.plot(y1, color='b', alpha=0.1)             
    pl.plot(y2, color='b', alpha=0.2)
    pl.plot(y3, color='b', alpha=0.3)
    pl.plot(y4, color='b', alpha=0.4)
    pl.plot(y5, color='b', alpha=0.5)
    pl.plot(y6, color='b', alpha=0.6)
    pl.plot(y7, color='b', alpha=0.7)
    pl.plot(y8, color='b') # default: 1
    pl.show()
##alpha_test()

def linestyle_test():
    pl.plot(y1, linestyle='-')      # Solid (default)
    pl.plot(y2, linestyle='--')     # Dashed 
    pl.plot(y3, linestyle='-.')     # Dash-dot 
    pl.plot(y4, linestyle=':')      # Dense Dotted 
    pl.plot(y5, linestyle='dotted') # Dotted 
    pl.plot(y6, linestyle='')       # Nothing
    pl.show()
##linestyle_test()

def marker_test():
    pl.plot(y1, marker='o')          # Circle (default)
    pl.plot(y2, marker='^')          # Upward-pointing triangle
    pl.plot(y3, marker='s')          # Square
    pl.plot(y4, marker='+')          # Plus
    pl.plot(y5, marker='x')          # Cross
    pl.plot(y6, marker='D')          # Diamond
    pl.show()
##marker_test()

def mark_size():
    pl.plot(y1, marker='o')
    pl.plot(y2, marker='s', ms=10)
    pl.plot(y3, marker='^', ms=20)
    pl.show()
##mark_size()

def margins():
    pl.margins(0.1, 0.3)
    pl.plot(y1)
    pl.show()
##margins()

def scale_axis():
    i = np.linspace(0, 2*np.pi)

    pl.figure()
    pl.subplot(221)
    pl.axis('auto')   # default
    pl.plot(np.sin(i), np.cos(i))

    pl.subplot(222)
    pl.axis('equal')
    pl.plot(np.sin(i), np.cos(i))
    
    pl.show()
##scale_axis()

def title_test():
    # pl.title('Title')

    pl.figure()
    pl.subplot(221)
    # fontsize { 'large'(default), 'medium', 'small', or an actual size}
    pl.title('Title 1', fontsize='small')

    pl.subplot(222)
    # verticalalignment(va) { 'top', 'baseline', 'bottom', 'center'(default) }
    pl.title('Title 2', va='bottom')

    pl.subplot(223)
    # horizontalalignment(ha) { 'center', 'left', 'right'(default) }
    pl.title('Title 3', ha='left')

    pl.tight_layout()
    pl.show()
##title_test()

def ticks():
    t = range(5)
    s = [2*i for i in t]  # s = 2t
    pl.plot(t, s)
    
    x_labels = ['sec %d' % (i) for i in t]
    y_labels = ['%d meters' % (i) for i in s]
    pl.xticks(t, x_labels, rotation='vertical')
    pl.yticks(s, y_labels)
    pl.show()
##ticks()

def xy_labels():
    pl.xlabel('x-axes')
    pl.ylabel('y-axes')
    pl.show()
##xy_labels()

def label_legend_loc():
    pl.plot(y1, label='y1')
    pl.plot(y2, label='y2')
    pl.plot(y3, label='y3')
    pl.legend()
    
    # pl.legend(loc= 10)    # loc: 0 -> 10
    # 0 best, 1 upper right, 2 upper left, 3 lower left, 4 lower right, 5 right, 
    # 6 center left, 7 center right, 8 lower center, 9 upper center, 10 center 
    pl.show()
##label_legend_loc()

# Annotate:
def annotate():
    pl.plot(y1)
    pl.annotate('y1', xy=(8, 8), xytext=(6, 8),  
           arrowprops=dict(arrowstyle='->'))
    pl.show()
##annotate()

# Text:
def text():
    x = np.linspace(-4, 4)     # k  is black
    pl.plot(x, [0 for _ in x], 'k')   # x-axis
    pl.plot([0 for _ in x], 2*x, 'k') # y-axis
    
    # pl.text(0, 0, '(0,0)')
    # pl.text(0, 0, '(0,0)', va='center', ha='center')
    # pl.text(0, 0, '(0,0)', va='bottom', ha='right')
    pl.text(0, 0, '(0,0)', va='top', ha='left')
    pl.show()
##text()

##################################################################

'''                    SymPy Plot
SymPy provides a more simple plot.
It was designed to work with expression of symbols, but limited to only one symbol.

pip install sympy
'''
from sympy.plotting import plot
from sympy import Symbol

x = Symbol('x')
def parabola_plot():
    ## b**2 < 4*a*c   there are no solutions.
    b, a, c = 1, 1, 1
    plot( a*x**2 + b*x + c, (x, -4, 4) )   ## plot the expression, limit x axis as [-4, 4]

    ## b**2 = 4*a*c   there is one solution.
    b, a, c = 2, 1, 1
    plot( a*x**2 + b*x + c, (x, -4, 4) )

    ## b**2 > 4*a*c   there are two solutions.
    b, a, c = 3, 1, 1
    plot( a*x**2 + b*x + c, (x, -4, 4) )
##parabola_plot()  ## There are three plots, close one to see the other.

def plot_config():
    plot(2*x + 1)
    plot(2*x + 1, (x, -4, 4), title='Linear', ylabel='2x+1')
##plot_config()

# Save the plot in a file
def save_plot():
    p = plot(x**2 - 5*x - 20, (x, -20, 20), show=False)
    p.save('plot.png')
##save_plot()

# Solving Equations with Graphs:
def solve_equations():
    p = plot(2*x+3, 3*x+1, (x, 0, 5), legend=True, show=False)
    p[0].line_color = 'b'
    p[1].line_color = 'r'
    p.show()
##solve_equations()



