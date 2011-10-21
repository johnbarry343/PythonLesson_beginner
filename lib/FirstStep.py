# You can see the syntax for "substitution" and "for loop".


# charm to make a drowing
from turtle import *

# put a value into the variable
# example: l is a valuable and 100 is a value.
l = 100
s1 = 120
s2 = 60

# for loops are the most complex loops in python.
# the syntax of a for loop is
#   for element in iterable:
# range(3) means 3 times.
for i in range(3):
    # drow triangle shape
    for i in range(3): 
        forward(l)
        left(s1)
    # this concludes one for loop instruction.
    # the instruction is writtern with indent.
    # Plese carefully.

    for i in range(3):
        forward(l)
        right(s1)

    # drow hexagonal shape
    for i in range(6):
        forward(l)
        left(s2)
    for i in range(6):
        forward(l)
        right(s2)

    l = l + 20
