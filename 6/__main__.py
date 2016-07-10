#!/usr/bin/python
# -*- coding: utf8 -*-

# FUNCTIONS
def SumOfSquares(end):
	total = 0
	
	for i in xrange(end+1):
		total += i**2
	return total
	
def SquareOfSum(end):
	sum = (end * (end+1)) / 2
	
	return sum**2

if __name__ == "__main__":
	print "+-----------------------------------------------------------+"
	print "| Find the difference between the sum of the squares of the |"
	print "| first 100 natural numbers and the square of sum           |"
	print "+-----------------------------------------------------------+"
	
	SumQ = SumOfSquares(100)
	SquareS = SquareOfSum(100)
	print "The difference is " + str(SumQ - SquareS)
