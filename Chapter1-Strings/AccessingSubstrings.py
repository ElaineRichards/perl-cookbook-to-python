#!/usr/bin/python
#
# AccessingSubstrings.py
#
# Problem: 
# You want to access or modify just a portion of a string, not the whole 
# thing. For instance, you've read a fixed-width record and want to 
# extract the individual fields.
#
# usage:
# AccessingSubstrings.py 

#
# We'll substitute the word 'robin' that appears
# in lower case with the word 'bluejay' in lowercase.
# This will not look at 'Robin' or "ROBIN'
#
# To use regular expressions in Python, import the "re" module
#
import re

robin = 'robin'
bluejay = 'bluejay'
samplestring = "A robin was sitting high up in a tree, And was happy as ever a robin could be"

# Access instances of the word 'robin'

findallobject = re.findall(robin,samplestring)
print findallobject

# Replace instances of the word 'robin' with the word 'bluejay'

# There is a string replace function, which is why we love python
# so much!

replacedstring = samplestring.replace(robin,bluejay)
print replacedstring
