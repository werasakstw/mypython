# Enum is a type which specified possible values.
from enum import Enum
class Color(Enum):
    red = 1
    green = 2
    blue = 3

# Enum values can be accessed by symbol, value and indexing with symbol str.
print(Color.red, Color(1), Color['red']) # Color.red Color.red Color.red

# Enum values can be assigned to variable.
c = Color.green
print(c)                    # Color.green

# Enum values can be equality compared.
print(c == Color.green)     # True

# But not relative compared.
##print(c < Color.blue)     # error

# Enum can be iterated.
print([c for c in Color])   # [<Color.red: 1>, <Color.green: 2>, <Color.blue: 3>]



