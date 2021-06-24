'''
Controls are statements that effect execution flows.
             if <condition>:
                 <body>
<body> is executed if the <condition> is True and it will
creates a new namespace.
<condition> does not require to surround in (), but not an error.
'''
def simp_if(x):
    if x == 1:
        print('One', end=',')
    print('End')
##simp_if(1)        #  One,End
##simp_if(2)        #  End

''' If with Else.
               if <condition>:
                   <if body>
               else:
                   <else body>
<else body> also creates a new namespace.
'''
def if_else(x):
    if x == 1:
        print('One', end=',')
    else:
        print('Else', end=',')
    print('End')
##if_else(1)        #  One,End
##if_else(2)        #  Else,End

'''
If statements can be nested and 'else' are options.
Python uses indentation to determine how 'if' and 'else' are paired.
'''
def nest_if(x, y):
    if x == 1:
        if y == 2:
            print('One, Two')
        else:
            print('Else y == 2')
    else:
        print('Else x == 1')
##nest_if(1, 2)		#  One, Two
##nest_if(1, 3)		#  Else y == 2
##nest_if(2, 3)		#  Else x == 1

'''
Multiple if-else create new namespaces in each nested namespaces.
That can be a lot of namespaces.
'''
def if_else(x):
    if x == 1:
        print('One')
    else:
        if x == 2:
            print('Two')
        else:
            if x == 3:
                print('Three')
            else:
                print('Else')
##if_else(2)

#  'elif' allows 'else' and 'if' without intermediate blocks.
def if_elif(x):
    if x == 1:
        print('One')
    elif x == 2:
        print('Two')
    elif x == 3:
        print('Three')
    else:
        print('Else')
##if_elif(2)

#----------------------------------------------------------

'''
A 'conditional' is an expression that its result is depended on a condition.
   <true returned> if <condition> else <false returned>
'''
def condidtional():
    def f(x):
        print('Few' if x <= 3 else 'Many')
        
    f(1)            #  Few
    f(5)            #  Many
##condidtional()

#----------------------------------------------------------

''' Python performs coercion with the following rules.
        1. The following are coerced to False:
           None
           zero integer 0
           zero float   0.0
           empty string ''
           empty list   []
           empty tuple  ()
           empty dict   {}
           empty set    ()
        Other values are True.
'''
