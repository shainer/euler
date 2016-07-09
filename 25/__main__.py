#!/usr/bin/python
# -*- coding: utf8 -*-

# FUNCTIONS
def CountDigits(number):
	count = 0
	
	for n in str(number):
		count += 1
	return count

def FibonacciSequenceNoLimits(n1, n2):
	n3 = 0
	counter = 2
	
	while CountDigits(n3) != 1000:
		n3 = n1 + n2
		n1 = n2
		n2 = n3
		counter = counter + 1
	return counter

if __name__ == "__main__":
	print "+--------------------------------------------------+"
	print "| What is the first term in the Fibonacci sequence |"
	print "| to contain 1000 digits?                          |"
	print "+--------------------------------------------------+"
	
	result = FibonacciSequenceNoLimits(1,1)
	print "It's the term number " + str(result)
