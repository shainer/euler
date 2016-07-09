#!/usr/bin/python
# -*- coding: utf8 -*-

# FUNCTIONS
def IsFifthNumber(n):
	fifthsum = 0
	
	for j in str(n):
		fifthsum += int(j)**5
		
	return (fifthsum == n)

if __name__ == "__main__":
	sum = 0
	
	print "+-------------------------------------------------+"
	print "| Find the sum of all numbers that can be written |"
	print "| as the sum of the 5th powers of their digits    |"
	print "+-------------------------------------------------+"
	
	for i in xrange(3, 1000000):
		if IsFifthNumber(i):
			sum +=i
			
	print sum
