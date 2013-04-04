#!/usr/bin/python
# Problem

# You want to print out the number represented by a given ASCII character, 
# or you want to print out an ASCII character given a number.

#
# Perl has the ord function to turn a char into a number and the chr
# function to turn a number into a character.
# The example in Perl has the number 101 be the character e
# This is very much the same in Python
#


firstchar = "e"
number = ord(firstchar)
char = chr(number)

print "Firstchar is " + firstchar
print "Number is " + str(number)
print "Char is " + char
