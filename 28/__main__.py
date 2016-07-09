#!/usr/bin/python
# -*- coding: utf8 -*-

# FUNCTIONS

if __name__ == "__main__":
	somma = 1
	x = 3
	
	print "+----------------------------------------------------------+"
	print "| What is the sum of both diagonals in a 1001x1001 spiral? |"
	print "+----------------------------------------------------------+"
	
	for i in range(500):
		somma += (4 * (x**2)) - (6 * (x-1))
		x+=2
		
	print somma
	
