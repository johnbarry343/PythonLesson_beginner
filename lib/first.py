from turtle import *

l = 100
s1 = 120
s2 = 60

for i in range(100):
	for i in range(3):
		forward(l)
		left(s1)
	for i in range(3):
		forward(l)
		right(s1)

	for i in range(6):
		forward(l)
		left(s2)
	for i in range(6):
		forward(l)
		right(s2)
	
	l = l + 20
