#!/usr/bin/python
# -*- coding: utf8 -*-

import math

# FUNCTIONS

# The well-known sieve
def PrimesUpTo(n):
	l = range(n + 1)
	
	for i in range(2, n + 1):
		for j in range(2 * i, n + 1, i):
			l[j] = 0
			
	return l

def CountPrimeDivisors(num, primes):
	count = 0
	div = 2
	
	if primes[num] != 0:
		return count
	
	while div <= (num // 2):
		if primes[div] != 0 and num % div == 0:
			count += 1
		
		div += 1
	
	return count
	
def rotateLeft(array, next):
	
	for index in range(len(array) - 1):
		array[index] = array[index + 1]
	
	array[index + 1] = next
	return array

if __name__ == "__main__":

	primes = PrimesUpTo(10 ** 6)
	fNumbers = [644, 645, 646, 647]
	fDivisors = [3, 3, 3, 3]
	
	print "+--------------------------------------------------------------------------------+"
	print "| Find the first four consecutive integers to have four distinct primes factors. |"
	print "| What is the first of these numbers?                                            |"
	print "+--------------------------------------------------------------------------------+"
	
	cNum = 648
	while 1:
		fNumbers = rotateLeft(fNumbers, cNum)
		fDivisors = rotateLeft(fDivisors, CountPrimeDivisors(cNum, primes))
	
		if fDivisors[0] == 4 and fDivisors[1] == 4 and fDivisors[2] == 4 and fDivisors[3] == 4:
			break
				
		cNum += 1
		
	print fNumbers[0]
