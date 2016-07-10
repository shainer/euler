#!/usr/bin/python
# -*- coding: utf8 -*-

# FUNCTIONS
def Factorial(number):
	total = 1
	
	if number == 0:
		return 1
	
	for i in range(2, number+1):
		total *= i
	return total

def Combinatorics(n, k):
	result = 1
	
	for x in range(n, k, -1):
		result *= x
	
	result //= Factorial(n - k)
	return result
	

if __name__ == "__main__":
	count = 0
	
	print "+-----------------------------------------------------------+"
	print "| How many, not necessarily distinct, values of ^(n)C_(r),  |"
	print "| for 1 ≤ n ≤ 100, are greater than one-million?            |"
	print "+-----------------------------------------------------------+"
	
	for n in range(1, 101):
		for k in range(1, n+1):
			if Combinatorics(n, k) > 1000000:
				count += 1

	print count
