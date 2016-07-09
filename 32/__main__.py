#!/usr/bin/python
# -*- coding: utf8 -*-

from sets import Set

def IsPandigital(s):
	s = ''.join(sorted(s))
	return (s == '123456789')

def IsValidLength(s):
	return (len(s) == 9)

if __name__ == "__main__":
	PanProducts = []
	
	print "+-----------------------------------------------------+"
	print "| Find the sum of all products whose                  |"
	print "| multiplicand/multiplier/product identity can be     |"
	print "| written as a 1 through 9 pandigital.                |"
	print "+-----------------------------------------------------+"

	for a in range(1, 10000):
		for b in range(a+1, 10000):
			if a == b:
				continue
			p = (a * b)
			s = str(a) + str(b) + str(p)

			if IsValidLength(s) and IsPandigital(s):
				PanProducts.append(p)
	
	PanProducts = Set(PanProducts)
	print sum(PanProducts)
