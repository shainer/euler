#!/usr/bin/python
# -*- coding: utf8 -*-

# FUNCTIONS

if __name__ == "__main__":
	triangles = []
	pentagonals = []
	hexagonals = []
	
	print "+----------------------------------------------------------------------------------+"
	print "| After 40755, find the next triangle number that is also hexagonal and pentagonal |"
	print "+----------------------------------------------------------------------------------+"
	
	
	for i in range(2, 100001):
		next = (i * (i+1)) // 2
		triangles.append(next)
		next = (3 * i**2 - i) // 2
		pentagonals.append(next)
		next = i * ((2*i) - 1)
		hexagonals.append(next)
		
	for n in triangles:
		if n != 40755 and n in pentagonals and n in hexagonals:
			break

	print n
