#!/usr/bin/python
# -*- coding: utf8 -*-

import psyco
psyco.full()

# FUNCTIONS

def FibonacciSequence(n1, n2, end):
	list = [n1, n2]
	n3 = 0
	
	while n3 <= end:
		if n3 % 2 == 0:
			list.append(n3)
		n3 = n1 + n2
		n1 = n2
		n2 = n3
		
	return list
	

if __name__ == "__main__":
	print "+---------------------------------------------------------+"
	print "| Find the sum of all the even-valued terms               |"
	print "| in the Fibonacci sequence which do not exceed 4 million |"
	print "+---------------------------------------------------------+"
	
	EvenFibonacci = FibonacciSequence(1, 2, 4000000)
	print sum(EvenFibonacci)
	
