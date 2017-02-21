#!/usr/bin/env python

"""
Sample test script.

"""

# use print function so this script works in Python 2 or 3:
from __future__ import print_function

x = 3.
y = 1.
z = x + y
expected_sum = 2.

assert z==expected_sum, 'x = %g, y = %g, expect sum = %g' % (x,y,expected_sum)

print("Runs fine!")

