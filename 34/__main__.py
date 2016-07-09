#!/usr/bin/python
# -*- coding: utf8 -*-

# FUNCTIONS

def Factorial(num):
	if num == 0 or num == 1:
		return 1
		
	else:
		return num * Factorial(num-1)

def IsCuriousNumber(n):
	factsum = 0
	
	for j in str(n):
		factsum += Factorial(int(j))
		
	return (factsum == n)

if __name__ == "__main__":
	sum = 0
	
	print "+-------------------------------------------------+"
	print "| Find the sum of all numbers that can be written |"
	print "| as the sum of the factorials of their digits    |"
	print "+-------------------------------------------------+"
	
	for i in xrange(3, 1000000):
		if IsCuriousNumber(i) == True:
			sum +=i
			
	print sum
