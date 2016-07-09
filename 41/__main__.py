#!/usr/bin/python
# -*- coding: utf8 -*-

# FUNCTIONS
def PrimesUpTo(n):
	l = [ x for x in range(n + 1) ]
	for i in range(2, n + 1):
		for j in range(2 * i, n + 1, i):
			l[j] = 0
	return l
	
def IsPandigital(number):
	length = len(str(number))
	
	for d in range(1, length+1):
		if str(d) not in str(number):
			return False
	
	return True

if __name__ == "__main__":	
	print "+-----------------------------------------------------------+"
	print "| What is the largest n-digit pandigital prime that exists? |"
	print "+-----------------------------------------------------------+"
		
	primes = PrimesUpTo(7654321)
	for x in range(7654321, 2143, -1):
		if primes[x] != 0 and IsPandigital(primes[x]) == True:
			break
	
	print x
