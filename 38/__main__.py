#!/usr/bin/python
# -*- coding: utf8 -*-

# FUNCTIONS
def IsPandigital(p):
	length = len(p)
	
	for d in range(1, length+1):
		if str(d) not in p:
			return False
	
	return True

if __name__ == "__main__":
	k = 14
	product = ""
	
	print "+-----------------------------------------------------------+"
	print "| What is the largest 1 to 9 pandigital 9-digit number that |"
	print "| can be formed as the concatenated product of an integer   |"
	print "| with (1,2, ... , n) where n > 1?                          |"
	print "+-----------------------------------------------------------+"
	
	while True:
		n = 1
		
		while len(product) < 9:
			product += str(n * k)
			n += 1
		
		if IsPandigital(product):
			print product
		product = ""
		k += 1
