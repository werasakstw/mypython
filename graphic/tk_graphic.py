import tkinter
'''
A Tk object must be create first.
Some kind of view, a canvas is created.
The canvas must be pack() to show of the screen.
The canvas provides create_<shape>() to draw on.
'''
tk = tkinter.Tk()
width, height = 500, 500
cv = tkinter.Canvas(tk, width=width, height=height)
cv.pack()

def create():
    ''' The origin (0, 0) is at the left-top most.
        x is to the right and y is downward.    '''
                #  x1,  y1,  x2,  y2
    cv.create_line(100, 100, 400, 400)

                #       x1,  y1,  x2,  y2
    cv.create_rectangle(200, 200, 300, 250, fill="blue")

                #   x1,  y1,  x2,  y2
    cv.create_oval(200, 300, 300, 400, outline="green", width=4)

                #  x1,  y1,  x2,  y2        angle
    cv.create_arc(100, 100, 200, 160, extent=180, style='arc')

                #     x1,  y1,  x2,  y2,  x3,  y3   
    cv.create_polygon(200, 100, 300, 50, 350, 200, fill="red", outline="black")

    cv.create_text(50, 50, text='Hello')

    # john = tkinter.PhotoImage(file='john.png')
    # cv.create_image(100, 300, image=john)
##create()

''' Colors are defined by:
     - name   e.g. red, green, blue etc.
          http://www.tcl.tk/man/tcl8.5/TkCmd/colors.htm
     - hex-string (like in HTML) '#RRGGBB'  e.g. '#FF0000'
'''
def color_test():
    def to_color(r, g, b):
        return '#' + format(r, '02x') + format(g, '02x') + format(b, '02x')

    cv.create_line(100, 100, 400, 100, width=5, fill='black')
    cv.create_line(100, 200, 400, 200, width=5, fill='#FF0000')
    cv.create_line(100, 300, 400, 300, width=5, fill=to_color(150, 50, 200))
##color_test()

def fill_outline():
    cv.create_rectangle(100, 100, 180, 160, fill='yellow')
    cv.create_rectangle(200, 200, 280, 260, outline='blue')
    cv.create_rectangle(300, 300, 380, 360, fill='red', outline='red')
##fill_outline()

#-----------------------------------------------------------------------------------

def icon():
    bitmaps = ["error", "gray75", "gray50", "gray25", "gray12",
               "hourglass", "info", "questhead", "question", "warning"]
    nsteps = len(bitmaps)
    step_x = width // nsteps

    #for i in range(0, nsteps):
    for i, b in enumerate(bitmaps):
        cv.create_bitmap((i+1)*step_x - step_x/2, 200, bitmap=b)
##icon()

#----------------------------------------------------------------------

import math
''' x = radius * cos(angle)
    y = radius * sin(angle)  '''
def circle1(cx, cy, radius, color):
    angle = 0
    while angle < 2*math.pi:
        x = radius*math.sin(angle) + cy
        y = radius*math.cos(angle) + cy
        cv.create_oval(x, y, x, y, outline=color, width=2)
        angle += 0.05
##circle1(width//2, height//2, 100, 'red')

#  x^2 + y^2 = radius^2
def circle2(cx, cy, r, color):
    rsq1 = r*r
    rsq2 = (r+1)*(r+1)
    for x in range(-r, r+1):
        for y in range(-r, r+1):
            rr = x*x + y*y
            if rr > rsq1 and rr < rsq2:
                cv.create_oval(x+cx, y+cy, x+cx, y+cy, outline=color, width=1)
##circle2(width//2, height//2, 100, 'blue')

#-----------------------------------------------------------------------

def sin_cos(scale_x, scale_y):
    def point(x, y, size, color):
        d = size // 2
        x1, y1 = (x - d), (y - d)
        x2, y2 = (x + d), (y + d)
        cv.create_oval(x1, y1, x2, y2, fill=color, outline=color)
    
    angle = 0.0
    cy = height // 2
    four_pi = 4*math.pi
    while angle < four_pi:
        x = scale_x*angle
        y = scale_y*math.sin(angle) + cy
        point(x, y, 4, 'red')
        y = scale_y*math.cos(angle) + cy
        point(x, y, 4, 'blue')       
        angle += 0.1
##sin_cos(40, 200)

#---------------------------------------------------------------------------

# r1 and r2 are radius of the outer and inner circles.
# p is pen position relative to the center of the rolling circle 
def spirograph(r1, r2, p):  
    d = math.pi / 90
    max = 10 * math.pi
    angle = 0.0
    cy = height // 2
    x1 = (r1+r2)* math.cos(angle)- p * math.cos((r1+r2)*angle/r2) + cy
    y1 = (r1+r2)* math.sin(angle)- p * math.sin((r1+r2)*angle/r2) + cy
    x2, y2 = 0, 0
    while angle < max:    
        x2 = (r1+r2)* math.cos(angle)- p * math.cos((r1+r2)*angle/r2) + cy
        y2 = (r1+r2)* math.sin(angle)- p * math.sin((r1+r2)*angle/r2) + cy
        cv.create_line(x1,  y1,  x2,  y2)
        x1, y1 = x2, y2
        angle += d

##spirograph(60, 50, 60)
##spirograph(70, 40, 70)

#-----------------------------------------------------------------------------------

def key_event():
    def do_hello(event):
        print('Hello', event.char)

    def do_hi(event):
        print('Hi')

    cv.focus_set()
    cv.bind("<Key>", do_hello)
    cv.bind("<Return>", do_hi)
##key_event()

def scriptlet(point, color):
    def do_dot(event):
       cv.create_oval((event.x - point), (event.y - point), 
                      (event.x + point), (event.y + point),
                      fill=color, outline=color)
    cv.focus_set()    
    cv.bind("<Button-1>", do_dot)     # Left Mouse Button
##    cv.bind("<Button-2>", do_dot)     # Middle Mouse Button
##    cv.bind("<Button-3>", do_dot)     # Right Mouse Button
##    cv.bind("<Double-1>", do_dot)    ## <Double-2>  <Double-3>
##    cv.bind("<B1-Motion>", do_dot)   ## <B2-Motion>  <B3-Motion>
##scriptlet(3, 'green')

def move_test():
    def do_move(event):
        cv.coords(r, event.x, event.y, event.x+100, event.y+50)

    def do_remove(event):
        cv.delete(r)
        
    def do_delete():
        cv.delete(r)

    r = cv.create_rectangle(50, 25, 150, 75, fill="blue")
    cv.bind("<B1-Motion>", do_move)
    cv.bind("<Double-1>", do_remove)
    tkinter.Button(text='Delete', command=do_delete).pack()
##move_test()

def tag_test():
    def do_move(event):
        ot = cv.find_withtag('blue_oval')
        cv.move(ot, 1, 0)
        ot = cv.find_withtag('red_oval')
        cv.move(ot, 0, 1)
        
    cv.create_oval(100, 100, 150, 150, fill='blue', tags=('blue_oval'))
    cv.create_oval(200, 100, 250, 150, fill='red', tags=('red_oval'))
    
    cv.bind('<Button-1>', do_move)
##tag_test()

tkinter.mainloop()
