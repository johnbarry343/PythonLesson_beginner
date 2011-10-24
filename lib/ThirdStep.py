# You can see how to use "def" and "if".
# def makes function.
# syntax of def is
#    def function_name :
#        do something
# if is statements for decision making
# syntax of if is
#    if assumption :
#        do something

from turtle import *
import sys

s = sys.argv

print 'you ran %s.' % s[0]

def function1():
    print 'you typed 1'
def function2():
    # drowing - if you couldn't understand the following, check the FirstStep.py.
    loop = int(s[1])
    l = 100
    s1 = 120
    s2 = 60
    if loop <= 10:
        for i in range(loop):
            for i in range(3): 
                forward(l)
                left(s1)

            l = l + 20
    else :
        for i in range (loop/2):
            for i in range(6):
                forward(l)
                left(s2)
            l = l + 20

# s[1] has list. int() makes module integer number.
if int(s[1]) == 1:
    # run function1()
    function1()
else :
    # run function2()
    function2()
