import random
from PIL import Image

''' Fractals are shapes that we can zoom in indefinitely and
see similar or exactly the same shape.

Sierpinski's Triangle: 
Let x = 0 and y = 0.
Iterates as many time as you want.
      r = a random number between 0 and 1.0
      if r < 1/3 
          x *= 0.5
          y *= 0.+5
      if 1/3 <= r <= 2/3
          x = x/2 + 0.25
          y = y/2 + 0.5
      if r > 2/3
          x = x/2 + 0.5
          y *= 0.5
      point(x, y)      // scale x and y to fit the frame
'''
def triangle(n):
    w, h = 800, 800
    im = Image.new("L", (w, h), 255) ## Create an empty B/W image
    one3 = 1.0/3.0
    two3 = 2.0/3.0
    x, y = 0.0, 0.0
    for i in range(n):
        r = random.random()
        if r < one3:
            x *= 0.5
            y *= 0.5
        elif r < two3:
            x = x/2 + 0.25
            y = y/2 + 0.5
        else:
            x = x/2 + 0.5
            y *= 0.5           
        cx, cy = int(x*w), int(y*h)  ## scale to fit w, h
        im.putpixel((cx, cy), 0)
    im.show()
##triangle(100000)

''' Michael Barnsley Fern:
Let x = 0 and y =0.
Iterates as many time as you want.
      r = a random number between 0 and 1.0
      if r < 0.01                     ## 1%
          x = 0
          y = 0.13*y
      if r < 0.08                     ## 7%
          x = 0.2*x - 0.26*y
          y = 0.23*x + 0.22*y + 1.6
      if r < 0.15                     ## 7%
          x = -0.15*x + 0.28*y
          y = 0.26*x + 0.24*y + 0.44
      else                            ## 85%
          x = 0.85*x + 0.04*y
          y = -0.04*x + 0.85*y + 1.6
      point(x, y)
'''
def fern(n):
    w, h = 900, 700
    im = Image.new("L", (w, h), 255)
    x, y = 0.0, 0.0
    for i in range(n):
        r = random.random()
        if r < 0.01:
            x, y = 0, 0.13*y
        elif r < 0.08:
            x, y = (0.2*x - 0.26*y), (0.23*x + 0.22*y + 1.6)
        elif r < 0.16:
            x, y = (-0.15*x + 0.28*y), (0.26*x + 0.24*y + 0.44)
        else:
            x, y = (0.87*x + 0.04*y), (-0.04*x + 0.85*y + 1.6)    
        cx, cy = abs(int(x*w/5)), abs(int(y*h/10))
        im.putpixel((cx, cy), 0)
    im.show()
##fern(100000)

#-------------------------------------------------------------

''' A Complex Number has two parts,
  - the real part is a number (may be integer or float).
  - the imaginary part is a number multiplies with sqrt(-1).
Python represents the sqrt(-1) with j.
'''
m = 1 + 2j      ## 1 + 2*sqrt(-1)
n = 3 + 4j      ## 3 + 4*sqrt(-1)
##print(m+n, m-n, m*n, m/n)   # (4+6j) (-2-2j) (-5+10j) (0.44+0.08j)

# Suppose: x = a + bj   y = c + dj
#      x*y = (a*c - b*d) + (a*d + b*c)j
##print(m*n, (1*3 - 2*4) + (1*4 + 2*3)*1j)  # (-5+10j) (-5+10j)

#      x*x = (a*a - b*b) + (2*a*b)j
##print(m*m, (1*1 - 2*2) + (2*1*2)*1j)      # (-3+4j) (-3+4j)

#      abs(x) = sqrt(a**2 + b**2)
##print(abs(n))                             # 5.0

#---------------------------------------------------------

'''      Introducing Julia Set
Orbit Function:
Suppose a square function x = x**2, where x is any number.
The orbit of x is the sequence of applying the function repeatedly.
    ex. the orbit of 2 is 2, 4, 16, ....

For all x out of range [-1, 1] the orbit goes toward infinity.
For x in range [-1, 1], some orbits go to infinity but some do not.
The set of x that their orbits do not go to infinity is called Julia set.

To test whether an orbits go to infinity would take lot of time.
But if a number (integer or float) exceeds 1 its square would be larger.
So we can approximately test by iterating the x orbits for about 100 times
if no values go beyond 1 then x is in Julia set.
'''
def float_julia():
    def in_julia(x):
        for _ in range(100):
            x = x**2
            if x > 1:
                return False
        return True

    float_range = [ x/10 for x in range(-15, 15, 1)]  # from -1.5 to 1.5
    for x in float_range:
        print('%1.4e: %s' % (x, in_julia(x)))
##float_julia()

''' To test whether a complex number is in Julia, we can approximatly iterating
the orbit for 100 times if the value does not goes beyond a threshold (ex. 4)
then the number is in Julia set.

Suppose an orbit function is c = c**2 - z  where c and z are complex numbers. '''
def in_julia(c, z, threshold):
    for _ in range(100):
        c = c**2 - z
        if abs(c) > threshold:
            return False
    return True
##print(in_julia(1 + 2j, 0, 4), in_julia(0.2 - 0.57j, 0, 4))    # False True

''' Unlike floats(and integers), complex numbers do not have a clear cut rule
to determine if a number is in Julia set. '''

''' Drawing Julia Set:
A pixel (x,y) on a screen is mapped to a complex number,
     where  x is the real part and y is the imagine part.
If the complex number is in Julia set then the pixel is plotted.

For the orbit function: c = c**2 - z, the image is depended on
    'c' is the starting point and 'z' is the constant.  '''

# To simplify the mapping from width and height of screen to complex number.
# Suppose a screen size:
w, h = 600, 600

# Mapping from range (0, 600) to (-2, 2).
def map_range(x):  
    return (x - 300) * 2/300
##print(map_range(0), map_range(600))     ## -2.0 2.0

# Let define the 'z' constant.
##z = 0       # circle
##z = 1
z = 0.51 + 0.53j
##z = 0.1 + 0.73j
##z = 0.73 + 0.21j
##z = 0.81 + 0.16j
##z = -0.64j

def bw_julia():    
    ## Create a black/white image with white background.
    im = Image.new("L", (w, h), 255)   
    for x in range(w):
        for y in range(h):
            c = map_range(x) + map_range(y)*1j
            if in_julia(c, z, 4):
                im.putpixel((x, y), 0) ## Plot a black pixel at x, y
    im.show()       # The black image is the shape of Julia set.
##bw_julia()      # Try: other 'z' values.
                
#-------------------------------------------------------------#

# Color of non-julia set.
# Let define a list of colors.
rgb_range =  [0, 125, 255]
colors = [(i, j, k) for i in rgb_range
                    for j in rgb_range
                    for k in rgb_range ]
colors_len = len(colors)
##print(colors_len, colors)

# Mapping an integer 'i' to a color:
def map_color(i):
    return colors[i % colors_len]

''' If a complex number is not in Julia set, the orbit would excess
the threshold at some iteration. The number of that iteration is mapped
to a color and ploted at the pixel of the complex number.
All pixels in julia set have the same color. '''
def is_non_julia(c, z, threshold): # returns (<whether in Julis set>, <number of iteration>)
    for i in range(200):
        c = c*c - z
        if abs(c) > threshold:  # Not in Julia set
            return True, i
    return False, i

def color_non_julia():
    im = Image.new("RGB", (w, h), 255) 
    for x in range(w):
        for y in range(h):
            c = map_range(x) + map_range(y)*1j
            non_julia, i = is_non_julia(c, z, 4)
            if non_julia:
                im.putpixel((x, y), map_color(i))
    im.show()
##color_non_julia()   # Try: changing 'z'.

#-----------------------------------------------------------#

''' The Julia shapes are divided into connected and disconnected
depended on the value of z. Some regions that appear to be a connected
are actually disconnected upon closer examination.

Mandelbrot set: is the set of complex numbers 'z' which makes a Julia shape
connected, that starts orbiting from c = 0.
Testing if a Julia set is connected, is performed by set threshold to 2.

Mandelbrot ploted the set of 'z' (called Mandelbrot set)
The result is the most magnificent shape in mathematics and computer science.
'''
def mandelbrot():
    im = Image.new("RGB", (w, h), 255)
    for x in range(w):
        for y in range(h):
            z = map_range(x) + map_range(y)*1j  ## Try: using different map_range()
            non_julia, i = is_non_julia(0, z, 2)
            if non_julia:
                im.putpixel((x, y), map_color(i))
    im.show()
##mandelbrot()
'''
The shape of Julia sets are symmetry but the Mandelbrot sets are not.
When we zoom in on Julia sets we see exactly the same shapes on different scales.
For Mandelbrot sets we see similar shapes but not exactly the same.
'''
