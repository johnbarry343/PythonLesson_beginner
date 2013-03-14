# You can see how to use "argv".
# argv is the list of command line arguments passed to a Python script.


from turtle import *
# charm to use argv
import sys

# sys.argv is the list.
s = sys.argv

# argv[0] is the script name.
# argv[1] is the words you typed.
print 'you ran %s.' % s[0]
print 'And drow the triangle %s times' % s[1]

# drowing - if you couldn't understand the following, check the FirstStep.py.
loop = int(s[1])
l = 100
s1 = 120
s2 = 60

for i in range(loop):
    for i in range(3): 
        forward(l)
        left(s1)

    l = l + 20
