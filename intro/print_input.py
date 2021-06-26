			# Output
##print('Hello')
##print()	# Output an empty line.

# print() evaluates its arguments then converts to string and send to standard output.
##print(1+2)

# Python allows newline(\n), return(\r) and semicolon(;) as statements separator.
# A semicolon at the end of line is not needed but not an error.
# A semicolon is need to separate statements in the same line.
##print('Hello'); print('Bye')

# print() accepts more than one parameters using ',' as the separator.
# All parameters are printed in the same line, with an extra space between items.
##print('Hello', 'John')

# To print without newline, define the attribute 'end' to be null.
##print('Hello', end=''); print('Bye')

# Consecutive strings (no separators) are combined into a string.
##print('Hello' 'John')       # HelloJohn

#-----------------------------------------------------------

		# Input
# input(<str>) shows the <str> and waits for an input to be entered.
##s = input("Enter a name.\n"); print("Hello " + s)

# input() alway returns a string.
# An explicit type conversion is needed for other types.
##n = int(input("Enter a number. ")); print(n, type(n))
