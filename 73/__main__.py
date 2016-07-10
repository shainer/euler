#!/usr/bin/python
# -*- coding: utf8 -*-

# FUNCTIONS

# Euclidean algorithm - no recursion employed just to see which is faster
def mcd(a, b):
	c = 0
	
	while a > 0:
		c = b % a
		b = a
		a = c
	
	return b

# The well-known sieve
def PrimesUpTo(n):
	l = range(n + 1)
	
	for i in range(2, n + 1):
		for j in range(2 * i, n + 1, i):
			l[j] = 0
			
	return l

# A little trick to improve timing (but it doesn't work so well)
def Euclide(num, den, primes):
	if (primes[den] != 0) or (num == 1):
		return 1
	
	return mcd(num, den)

if __name__ == "__main__":
	third = float(1) / float(3)
	half = float(1) / float(2)
	primes = PrimesUpTo(12000)
	count = 0
	
	print "+--------------------------------------------------------------+"
	print "| How many fractions lie between 1/3 and 1/2 in the sorted set |"
	print "| of reduced proper fractions for d ≤ 12,000?                  |"
	print "+--------------------------------------------------------------+"
	
	for den in range(2, 12001):		
		for num in range((den // 3) + 1, ((den-1) // 2) + 1):
			decimal = float(num) / float(den)
			
			if (decimal > third) and (decimal < half) and Euclide(num, den, primes) == 1:
				count += 1
			
	print count
