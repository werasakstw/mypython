from tkinter import *

# 'root' is the toplevel window, which is created
#   and returned when Tk is initialized.
root = Tk()

# Setting 'root' window options.
def root_option():
    root.title('This is a Title')
    root.minsize(width=200, height=200)
##    root.resizable(0, 0)	# Prevent resizing
##root_option()

# Setting 'root' window size and location.
def root_geometry():
    root.geometry('700x500')
##    root.geometry('700x500+50+20')
##root_geometry()

from tkinter import ttk
# Widgets are things that can be drawn on creen. e.g. label, 
#  button, text areas, checkboxes, scrollbars, frame and so on.
# A widget is created with a parent is passed as a parameter.
def widget_test():
    root.minsize(width=200, height=200)
    
    # There are two sets of widgets.
    # A widget must be rendered with pack() or grid().
    # A widget is not garbage collected even no referenced.
    # pack() put the widget is the middle of the frame.
    Button(root, text='Hello').pack()
    ttk.Button(root, text='Hello').pack()
##widget_test()

def position_test():
    root.minsize(width=400, height=300)
    
    Button(root, text='John').pack()
    Button(root, text='Jack').pack(pady=20) # add and set default to 20
    Button(root, text='Joe').place(x=100, y=100)
##position_test()

def side_pack():
    root.minsize(width=200, height=200)
    
    Label(text='top').pack(side=TOP)
    Label(text='left').pack(side=LEFT)
    Label(text='right').pack(side=RIGHT)
    Button(text='Hello').pack() # Try: Move to before 'top'.
    Label(text='bottom').pack(side=BOTTOM)
##side_pack()

def grid_test():
    root.minsize(width=200, height=200)
    Button(root, text='John').grid(row=0, column=0)
    Button(root, text='Jack').grid(row=0, column=1)
    Button(root, text='Joe').grid(row=1, column=1)

    Button(root, text='Jame').grid(row=2, column=0, padx=20, pady=20)
    Button(root, text='Jim').grid(row=3, column=0, stick='W')
    Button(root, text='Judy').grid(row=4, column=0, stick='E')
##grid_test()
                                  
def color_test():
    root.minsize(width=200, height=200)
    Label(text='Hello', fg='blue', bg='yellow').pack(pady=30)
    Button(text='Hello', fg='blue', bg='yellow').pack(pady=30)
##color_test()

# Event handling:
def doHello():
    print("Hello!")

def event_test():
    def doHi():
        print("Hi!")

    root.minsize(width=200, height=200)    
    ttk.Button(root, text='Hello', command=doHello).pack()
    ttk.Button(root, text='Hi', command=doHi).pack()
    
    # An event handling function may be a lambda.
    ttk.Button(root, text='What up', command=lambda : print("What's up?")).pack()
##event_test()

# Mouse Events:
def mouse_events():
    root.minsize(width=200, height=200)
    
    l =ttk.Label(root, text='Hello')
    l.pack(padx=50, pady=50)
    
    l.bind('<Enter>', lambda e: l.configure(text='Enter'))
    l.bind('<Leave>', lambda e: l.configure(text='Leave'))
    l.bind('<1>', lambda e: l.configure(text='Single left clicked'))
    l.bind('<Double-1>', lambda e: l.configure(text='Double left clicked'))
    l.bind('<B1-Motion>', lambda e: l.configure(text='Left button drag to %d,%d' % (e.x, e.y)))
##mouse_events()

def button_test():
    root.minsize(width=300, height=150)

    john = PhotoImage(file='john.png')
    b = Button(root, image=john)
    b.pack(padx=50, pady=50)
##button_test()


def login_test():
    root.title("Login")
    root.minsize(width=300, height=150)

    # 'ttk' widgets can be used with grid().
    ttk.Label(root, text="Name").grid(row=0, column=0, padx=10, pady=10)
    ttk.Entry(root, None).grid(row=0, column=1)
    ttk.Label(root, text="Password").grid(row=1, column=0, padx=10, pady=10)
    ttk.Entry(root, None).grid(row=1, column=1)
    ttk.Button(root, text="Cancel").grid(row=2, column=0, padx=20, pady=10)
    ttk.Button(root, text="Ok").grid(row=2, column=1, padx=20, pady=10)
##login_test()

## StringVar: is a variable for storing input string.
def string_var_test():
    sv = StringVar()
    ttk.Entry(root, textvariable=sv).pack()
    ttk.Label(root, textvariable=sv).pack()
##string_var_test()

def entry_test():
    def doHello():
        l.config(text='Hello ' + name.get())
##        b.config(state='disable')

    root.minsize(width=200, height=100)
    
    name = StringVar()
    e = ttk.Entry(root, textvariable=name)
    e.grid(column=0, row=0, padx=10, pady=10)   ## grid() returns None.
    e.focus()
    
    b = ttk.Button(root, text="Hello", command=doHello)
    b.grid(column=  1, row=0, padx=10, pady=10)
    
    l = ttk.Label(root, text="")
    l.grid(column=0, row=1, padx=10, pady=10)
##entry_test()

def check_button_test():
    def doGet():
        l.config(text=str(v1.get())+ "," + str(v2.get()))

    root.minsize(width=200, height=100)

    v1 = IntVar()
    cb1 = ttk.Checkbutton(root, text="Enabled", variable=v1, state='disable')
    cb1.grid(column=1, row=0, sticky='w', padx=10, pady=10)

    v2 = IntVar()
    cb2 = ttk.Checkbutton(root, text="Enabled", variable=v2, state='enable',
                          command=lambda:print("Checked"))
    cb2.grid(column=2, row=0, sticky='w', padx=10, pady=10)

    b = ttk.Button(root, text="Get", command=doGet)
    b.grid(column=2, row=2, padx=10, pady=10)
    
    l = ttk.Label(root, text="")
    l.grid(column=1, row=2, padx=10, pady=10)
##check_button_test()

## Radio Button:
def radio_button():
    def doGet():
        l.config(text=str(v.get()))

    root.minsize(width=200, height=100)
    
    v = IntVar()
    rb1 = ttk.Radiobutton(root, text='Hello', variable=v, value=1,command=doGet)
    rb1.grid(column=0, row=0, padx=10, pady=10)
    rb2 = ttk.Radiobutton(root, text='Hi', variable=v, value=2, command=doGet)
    rb2.grid(column=1, row=0, padx=10, pady=10)
    rb3 = ttk.Radiobutton(root, text='What up?', variable=v, value=3, command=doGet)
    rb3.grid(column=2, row=0, padx=10, pady=10)
    
    l = ttk.Label(root, text="")
    l.grid(column=1, row=2, padx=10, pady=10)
##radio_button()

## Combobox:
def combobox_test():
    def doGet():
        l.config(text=name.get()+ ", " + str(number.get()))

    root.minsize(width=200, height=100)
    
    ttk.Label(root, text="Name").grid(column=0, row=0, padx=10, pady=10)
    name = StringVar()
    n = ttk.Combobox(root, width=10, textvariable=name)
    n.grid(column=1, row=0, padx=10, pady=10)
    n['values'] = ('John', 'Jack', 'Joe')
    n.current(0)
    
    ttk.Label(root, text="Number").grid(column=0, row=1, padx=10, pady=10)
    number = IntVar()
    v = ttk.Combobox(root, width=10, textvariable=number)
    v.grid(column=1, row=1, padx=10, pady=10)
    v['values'] = (0, 1, 3, 6)
    v.current(0)

    b = ttk.Button(root, text="Get", command=doGet)
    b.grid(column=3, row=2, padx=10, pady=10)
    
    l = ttk.Label(root, text="")
    l.grid(column=1, row=2, padx=10, pady=10)
##combobox_test()

## Label Frame:
def label_frame_test():
   def do_login():
      print(name.get() + ',' + pwd.get())
      
   lf = ttk.LabelFrame(root, text='Login Frame ')
   lf.grid(column=0, row=0, padx=20, pady=20)

   ttk.Label(lf, text="Name").grid(column=0, row=0, padx=4, pady=4)
   name = StringVar()
   ne = ttk.Entry(lf, width=12, textvariable=name)
   ne.grid(column=2, row=0, sticky='w')
   
   ttk.Label(lf, text="Password").grid(column=0, row=1, padx=8, pady=4)
   pwd = StringVar()
   pe = ttk.Entry(lf, width=12, textvariable=pwd)
   pe.grid(column=2, row=1, sticky='w')

   b = ttk.Button(lf, text='Login', command=do_login)
   b.grid(column=2, row=31, sticky='w')
##label_frame_test()

# Scrollbar:
def scrollbar_test():
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)
    
    l = Listbox(root, height=5)
    l.grid(column=0, row=0, sticky=(N,W,E,S))
    for i in range(1,101):
        l.insert('end', 'Item %d' % i)

    s = ttk.Scrollbar(root, orient=VERTICAL, command=l.yview)
    s.grid(column=1, row=0, sticky=(N,S))
    l['yscrollcommand'] = s.set
        
    ttk.Sizegrip().grid(column=1, row=1, sticky=(S,E))
##scrollbar_test()

