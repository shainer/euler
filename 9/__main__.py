#!/usr/bin/python
# -*- coding: utf8 -*-

from math import sqrt
import psyco
psyco.full()

# FUNCTIONS

if __name__ == "__main__":
	print "+--------------------------------------------------+"
	print "| There exists exactly one Pythagorean triplet for |"
	print "| which a+b+c=1000. Find the product abc           |"
	print "+--------------------------------------------------+"
	
	for n in range(2, 1000):
		for m in range(n, 1000):
			if m == n:
				continue
			a = m**2 - n**2
			b = 2 * m * n
			c = m**2 + n**2
			
			if (a + b + c) == 1000:
				print str(a*b*c)
				break
