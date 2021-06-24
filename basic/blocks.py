'''
A block is a sequence of statements in a namespace(or scope).
Python uses indentation to define blocks.
Statements in the same block must be equally indented.
Statements at top level are in the 'global' namespace.
'''
print('Hello')
print('Bye')
##    print('Error')     # error

'''
Controls must have thier own block that begins with colon(:).
Statements in the body must be properly indentated.
'''
# Condition (If statement)
if True:
    print('Hello')
else:
    print('Hi')

# Iteration (For and While statements)
for i in [1, 2, 3]:
    print(i)

n = 0
while n < 3:
    print(n)
    n += 1

'''
Functions have thier own body block that begins with colon(:).
Statements in the body must be properly indentated.
Function definitions are not executed, they are must be called explicitly.
A function must be defined before it can be invoked.
'''
def greet():
    print('Hello')
    print('Hi')
greet()

'''
Functions abstract the complexity of the computation.
Callers need to know the function name, arguments and type of
the returned result but may not need to know how the task is computed.
'''

#-------------------------------------------------------------

# 'Expression' is a literal, variable, function call that return a value.
def hello():
    return 'Hello'

def expression():
    x = 1
    a = [1, 2, 3]

    # Expressions may appear at statement context, its value just ignored.
    0
    x
    x + 1
    a[0]
    a[:1]
    
    # Arguments may be literal, variable or expression. e.g. print(<expression>...)
    print(0, x, x+1)

    # A function call may or may not return a value.
    # Function calls may appear in expression or statement context.
    hello()
    x = hello()
    print(hello())

    # 'for' loop is a control statement.
    # Comprehension is an expression.
    print([x for x in range(3)])
##expression()

''' 'Statement' is a unit of execution that may appear in a block.
Assignment statements are of the form:
            <variable> = <expression>
The value of <expression> is assigned to the <variable>.
'''
def statement():
    # Assignments and controls are statement.
    x = 1 + 2
    if x > 0:
        print(x)
        
    # Statements do not return values, not even a None.
##    print(x = 1)                  # error
    
    # Assinments cannot be coerced for conditions.
##    while s = input('Enter: '):   # error
##        print(s)

    # So a commonly used loop is so clumsy.
    s = input('Enter: ')
    while s != '':
        print(s)
        s = input('Enter: ')

    # Python 3.8 introduced Assignment Expression (:=).
    while s := input('Enter: '):
        print(s)
        if s == '':
            break    
##statement()

