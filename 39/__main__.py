#!/usr/bin/python
# -*- coding: utf8 -*-

# FUNCTIONS

if __name__ == "__main__":
	MaxSolutions = 0
	MaxP = 0
	
	print "+-------------------------------------------------------------+"
	print "| If p is the perimeter of a right angle triangle, {a, b, c}, |"
	print "| which value, for p ≤ 1000, has the most solutions?          |"
	print "+-------------------------------------------------------------+"
	
	for p in range(1001):
		Solutions = 0
		
		for a in range(1, p // 4):
			for b in range(a+1, (p-a) // 2):
				c = (a**2 + b**2) ** 0.5
				if (a + b + c) == p:
					Solutions +=1
		
		if Solutions > MaxSolutions:
			MaxSolutions = Solutions
			MaxP = p
	
	print MaxP
