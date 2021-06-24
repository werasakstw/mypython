import turtle

''' Speed up drawing by omit animation.
Must be paired with turtle.update() at the end. '''
turtle.tracer(0, 0) 

''' Create a canvas
The x and y axis is to the right and up.
Initially, the turtle is at the center of the frame (0, 0)
and it look towards the x-axis.'''
t = turtle.Pen()

def move_to(x, y):
    t.up(); t.goto(x, y); t.down()

#-----------------------------------------------------

def square(width):
    for _ in range(4):
        t.forward(width)
        t.left(90)
##square(100)

def squareR(width):
    def _sqaure(width, side):
        if side > 0:
            t.forward(width)
            t.left(90)
            _sqaure(width, side-1)
    _sqaure(width, 4)
##squareR(100)

#------------------------------------------------------

def polygon(width, angle, step):
    for x in range(step):
        t.forward(width)
        t.left(angle)
def polygon_test():
    turtle.setup(width=700, height=700)
    move_to(-300, 200); polygon(100, 120, 3)
    move_to(-150, 200); polygon(90, 90, 4)
    move_to(0, 200); polygon(70, 72, 5)
    move_to(150, 200); polygon(60, 60, 6)
    
    move_to(-300, 0); polygon(100, 144, 10)
    move_to(-150, 0); polygon(40, 51, 7)
    move_to(0, 0); polygon(65, 102.857, 14)
    move_to(150, 0); polygon(80, 154.28, 14)

    move_to(-300, -200);  polygon(100, 127, 17)
    move_to(-150, -200); polygon(100, 100, 18)
    move_to(0, -200);  polygon(100, 150, 12)
    move_to(150, -200); polygon(100, 175, 35)
##polygon_test()
   
#--------------------------------------------------------------

''' The interior angle of an n-points star is
180(point-2k)/point degrees where k is less than point
and be a relative prime to point.
The turn angle is 180 - interior angle.
'''
def start(width, point, k):
    for _ in range(point):
        t.forward(width)
        t.left(180 - 180*(point-2*k)/point)
        
def start_test():
    turtle.setup(width=900, height=700)
    left = -550
    yr = [220, 50, -180]
    for point in range(3, 6): 
        for k in range(1, point):         
            move_to(left+ k*200, yr[point-3]); start(70, point, k)
##start_test()

def seven_point_stars():
    turtle.setup(width=900, height=400)
    left = -500
    for k in range(1, 7):         
        move_to(left+ k*130, 0); start(50, 7, k)
##seven_point_stars()

#--------------------------------------------------------

def rotate_square(width, angle):
    for i in range((360 // angle) + 1):
        square(width)
        t.left(angle)
def rotate_square_test():
    move_to(-150, 150); rotate_square(70, 60)
    move_to(-150, -150); rotate_square(70, 45)
    move_to(150, 150); rotate_square(70, 15)
    move_to(150, -150); rotate_square(70, 5)
##rotate_square_test()

def rotate_circle(width, angle):
    steps = (360 // angle) + 1
    for i in range(steps):
        t.circle(width)
        t.left(angle)
def rotate_circle_test():
    move_to(-150, 150); rotate_circle(40, 90)
    move_to(-150, -150); rotate_circle(40, 60)
    move_to(150, 150); rotate_circle(40, 30)
    move_to(150, -150); rotate_circle(40, 15)
##rotate_circle_test()

def rotate_square_dif(width, angle, dif):
    for i in range(360 // angle):
        square(width)
        t.left(angle)
        width -= dif
def rotate_square_dif_test():
    move_to(-150, 150); rotate_square_dif(80, 35, 5)
    move_to(150, 150); rotate_square_dif(100, 13, 4)
    move_to(-150, -150); rotate_square_dif(100, 9, 4)
    move_to(150, -150); rotate_square_dif(80, 10, 5)
##rotate_square_dif_test()

def rotate_line(width, angle, dif, step):
    for i in range(step):
        t.forward(width)
        t.right(angle)
        angle += dif
def rotate_line_test():
    move_to(-200, 150); rotate_line(30, 2, 20, 120)
    move_to(200, 100); rotate_line(20, 50, 30, 80)
    move_to(-150, -150); rotate_line(5, 2, 5, 720)
    move_to(150, -100); rotate_line(7, 0, 7, 600)
##rotate_line_test()

def rose(steps, angle, dif):
    width = dif
    for i in range(steps):
       t.forward(width)
       t.left(angle)
       width += dif
def rose_test():
    move_to(-150, 100); rose(27, 65, 3)
    move_to(-150, -100); rose(40, 113, 5)
    move_to(100, 100); rose(35, 85, 4)
    move_to(100, -100); rose(90, 143, 2)
##rose_test()

def roseR(width, angle, dif):
    if width > 0:
        t.forward(width)
        t.left(angle)
        roseR(width-dif, angle, dif)
def roseR_test():
    move_to(-200, 50); roseR(70, 41, 1)
    move_to(50, 70); roseR(100, 67, 2)
    move_to(-70, -200); roseR(120, 85, 2)
    move_to(250, -100); roseR(150, 110, 3)
##roseR_test()

def spiral(steps, angle):
    for i in range(steps):
       t.forward(i*2)
       t.left(angle)
def spiral_test():
    move_to(-200, 150); spiral(60, 70)
    move_to(0, 150); spiral(60, 91)
    move_to(200, 150); spiral(100, 123)
    move_to(-200, -150); spiral(53, 79)
    move_to(-10, -150); spiral(70, 100)
    move_to(200, -150); spiral(110, 151)
##spiral_test()

import random
colors = ["red", "yellow", "blue", "green", "orange", "purple", "gray"]
def spiral_art():
    for _ in range(130):
        t.pencolor(random.choice(colors))
        x = random.randrange(-turtle.window_width()//2, turtle.window_width()//2)
        y = random.randrange(-turtle.window_height()//2, turtle.window_height()//2)
        move_to(x,y)
        steps = random.randint(15,55)
        angle = random.randint(70,160)
        spiral(steps, angle)
##spiral_art()

#---------------------------------------------------------------

def rosette(sides):
    for m in range(5,75):
        t.left(360/sides + 5)
        t.width(m//25 + 1)
        t.penup()
        t.forward(m*4) # Move to next corner
        t.pendown()
        t.pencolor(random.choice(colors))
        if (m % 2 == 0):
            for n in range(sides):
                t.circle(m/3)
                t.right(360/sides)
        else:
            for n in range(sides):
                t.forward(m)
                t.right(360/sides)
##rosette(5)
##rosette(7)

#-----------------------------------------------------------
                
def nest1():
    for _ in range(10):
        t.right(36)
        for _ in range(5):
            t.forward(60)
            t.left(72)
def nest2():
    for _ in range(10):
        for _ in range(8):
            t.forward(42)
            t.right(45)
        t.right(36)
def nest3():
    for _ in range(5):
        for i in range(1, 9):
            t.forward(17*i)
            t.right(144)      
def nest_test():
    turtle.setup(width=900, height=400)
    move_to(-300, 0); nest1()
    move_to(0, 0); nest2()
    move_to(220, 0); nest3()
##nest_test()

#----------------------------------------------------------------

# Repeated Figure
def figure(width):
    t.forward(width); t.right(90)
    t.forward(width); t.right(90)
    t.forward(width/2); t.right(90)
    t.forward(width/2); t.right(90)
    t.forward(width); t.right(90)
    t.forward(width/4); t.right(90)
    t.forward(width/4); t.right(90)
##figure(100)
    
def figure_test():
    for _ in range(9):
        figure(60)
        t.right(10)
        t.forward(50)
##figure_test()

#-------------------------------------------------------------
   
# Closed Objects
def cobject(width, angle, max, steps):
    for i in range(steps):
        for i in range(1, max+1):    
            t.forward(width*i)
            t.right(angle)
        
def cobject_test():
    turtle.setup(width=900, height=400)
    move_to(-300, 100); cobject(5, 90, 10, 1)   
    move_to(-150, 100); cobject(5, 90, 10, 2)
    move_to(0, 100); cobject(3, 45, 10, 4)
    move_to(150, 100); cobject(5, 60, 10, 3)
    
    move_to(-300, -100); cobject(3, 45, 11, 9)
    move_to(-170, -100); cobject(2, 60, 13, 7)
    move_to(20, -40); cobject(4, 90, 15, 4)
    move_to(150, -80); cobject(10, 144, 8, 5)    
##cobject_test()

#--------------------------------------------------------------

def tree(width, angle):
    if width < 3:
        return
    t.right(-angle); t.forward(width)
    tree(width // 1.61803, angle)
    t.right(180); t.forward(width); t.right(180)
    t.right(2*angle); t.forward(width)
    tree(width // 1.61803, angle)
    t.right(180); t.forward(width); t.right(180)
    t.left(angle)
def tree_test():
    turtle.setup(width=900, height=700)
    move_to(-300, 100); t.left(90); tree(60, 13)
    move_to(-100, 100); tree(60, 25)
    move_to(200, 100); tree(60, 45)
    move_to(-300, -100); tree(60, 90)
    move_to(-50, -100); tree(70, 120)
    move_to(200, -100); tree(140, 145)
##tree_test()

#-------------------------------------------------------------------

def koch(width, steps):
    if steps == 0:
        t.forward(width);
        return
    koch(width/3, steps-1); t.left(60)
    koch(width/3, steps-1); t.right(120)
    koch(width/3, steps-1); t.left(60)
    koch(width/3, steps-1)
def koch_test():
    move_to(-250, 100); koch(200, 1)
    move_to(-250, -100); koch(200, 2)
    move_to(50, 100); koch(200, 3)
    move_to(50, -100); koch(200, 4)
##koch_test()

#--------------------------------------------------------------

def c(width, steps):
    if steps == 0:
        t.backward(width)
        return
    c(width, steps-1); t.left(90)
    c(width, steps-1); t.left(90)
def c_test():
    turtle.setup(width=800, height=600)
    move_to(-250, 200); c(5, 4)
    move_to(100, 200); c(5, 6)
    move_to(-250, 0); c(5, 8)
    move_to(100, -100); c(5, 10)
##c_test()

#-----------------------------------------------------------------

def left_dragon(width, steps):
    if steps == 0:
        t.forward(width); return
    left_dragon(width, steps-1); t.left(90)
    right_dragon(width, steps-1)
def right_dragon(width, steps):
    if steps == 0:
        t.forward(width); return
    left_dragon(width, steps-1); t.right(90)
    right_dragon(width, steps-1)
def dragon_test():
     move_to(-150, 200); left_dragon(3, 6)
     move_to(-150, -150); left_dragon(3, 8)
     move_to(50, 200); left_dragon(3, 10)
     move_to(50, -200); left_dragon(3, 12)
##dragon_test()

def left_hilbert(width, steps):
    if steps == 0:
        return
    t.left(90); right_hilbert(width, steps-1); t.forward(width)
    t.right(90); left_hilbert(width, steps-1)
    t.forward(width)
    left_hilbert(width, steps-1); t.right(90);
    t.forward(width); right_hilbert(width, steps-1); t.left(90)

def right_hilbert(width, steps):
    if steps == 0:
        return
    t.right(90); left_hilbert(width, steps-1); t.forward(width)
    t.left(90); right_hilbert(width, steps-1)
    t.forward(width)
    right_hilbert(width, steps-1); t.left(90)
    t.forward(width); left_hilbert(width, steps-1); t.right(90)
def hilbert_test():
    move_to(-150, 150); left_hilbert(10, 1)
    move_to(-150, -50); left_hilbert(10, 2)
    move_to(50, 150); left_hilbert(10, 3)
    move_to(50, -150); left_hilbert(10, 4)
##hilbert_test()

#################################################################

'''
                Turtle Moves
      forward(<distance>))    fd
      backward(<distance>))   bk
      left(<angle>)           lt
      right(<angle>)          rt
'''
##t.forward(50)

'''             Turtle Controls
      up()                     penup
      down()                   pendown
      goto(<x>, <y>)
      position()               returns current position (x,y)
      hideturtle()             ht
      showturtle()             st
      width(<size>)            set pen width
      pencolor('color')        set pen color
      color(red, green, blue)
'''
def move_to(x, y):
    t.up(); t.goto(x, y); t.down()
    print(t.position())
##move_to(100, 100)

def turtle_config():
    t.width(5)
    t.fd(100); t.left(90)
    t.width(10)
    t.pencolor('red')
    t.fd(100); t.left(90)
    t.width(15)
    t.color(0, 1, 0)
    t.fd(100)
##turtle_config()

'''             Screen Reset
      reset() clears the screen and back to the starting position
      clear() clears the screen and leaves the turtle where it is.

                Simple Figures (draw at current position)
      circle(<radius>)
      dot(<size>)
      shape(<shape>)
         'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'

      begin_fill(), end_fill()   fill current color in a closed figure.
'''
def fill_test():
    t.begin_fill()
    t.circle(100)
    t.end_fill()
##fill_test()

# Event Handling:
# To registerevents, the turtle must have focus by listen().
def key_event():
    def hello():        ## no parameter
        print('Hello')
        
    turtle.onkeypress(hello, 'h')
    ## 'space', 'Up', Down', 'Left', 'Right'
    turtle.listen()
##key_event()

def mouse_test():
    def hello(x, y):    ## two parameters
        print('Hello', x, y)
        
    turtle.onscreenclick(hello)
    # turtle.onscreenclick(hello, btn=3)
##mouse_test()

# textinput() open a prompt window and returns the input string.
# write(<string>) show the <string> at the current turtle.
def text_input():
    x = turtle.textinput('Title', 'Enter a number:')
    t.write(x)
##text_input()


turtle.update()
