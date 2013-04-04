#!/usr/bin/python
#
# The Perl book covers sending arguments in different ways. There's the
# default @_ for all arguments going in.
#
# Differences: I had to import math to get the math.sqrt function
#		Python wants the variables in the parentheses.
#
import math
def hypotenuse(x,y):
	z = ((x**2) + (y**2))
	return math.sqrt(z)

diag =  hypotenuse(4,5)
print diag

def hypotenusetwo(*args):
	z = args[0]**2 + args[1]**2
	return math.sqrt(z)

diag =  hypotenusetwo(4,5)
print diag


