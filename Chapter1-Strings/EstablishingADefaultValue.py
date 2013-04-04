#!/usr/bin/python

# Problem

# You would like to give a default value to a scalar variable, but only if 
# it doesn't already have one. It often happens that you want a hard-coded 
# default value for a variable that can be overridden from the command-line
# or through an environment variable.

# Use b if b is true, else use c

a = "" # This initializes an empty variable, not "nil" or "null"
b = "The letter b"
c = "The letter c"

if a:
	print "Use a"
else:
	print "No a, use c"
	a = c

print "a is " + a
