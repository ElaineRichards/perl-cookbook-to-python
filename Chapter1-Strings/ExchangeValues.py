#!/usr/bin/python
#
# Exchanging values without using temporary variables
#
# In the Perl book, you can use a list assignment to reorder the
# variables.
# ( $var1, $var2 ) = ( $var2, $var1 );

varone = "one"
vartwo = "two"

print "varone is " + varone
print "vartwo is " + vartwo

[ varone, vartwo ] = [ vartwo, varone ]

print "After the switch:"
print "varone is " + varone
print "vartwo is " + vartwo


