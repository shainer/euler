#!/usr/bin/python
# -*- coding: utf8 -*-

# FUNCTIONS

def IsAbundant(num):
	divisors = []
	
	for div in range(1, (num // 2) + 1):
		if (num % div) == 0:
			divisors.append(div)
	
	return (sum(divisors) > num)

if __name__ == "__main__":
	abundants = []
	final = range(20162)
	
	print "+---------------------------------------------------------+"
	print "| Find the sum of all the positive integers which cannot  |"
	print "| be written as the sum of two abundant numbers           |"
	print "+---------------------------------------------------------+"
	
	for i in range(12, 28124):
		if IsAbundant(i) == True:
			abundants.append(i)
	
	for i in abundants:
		for j in abundants:
			if (i+j) <= 20161:
				final[i+j] = 0
	
	print sum(final)
