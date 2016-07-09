#!/usr/bin/python
# -*- coding: utf8 -*-

import psyco
psyco.full()

# FUNCTIONS
def PrimesUpTo(n):
	l = range(n + 1)
	for i in range(2, n + 1):
		for j in range(2 * i, n + 1, i):
			l[j] = 0
	return l

if __name__ == "__main__":
	print "+--------------------------------------------+"
	print "| Find the sum of all primes below 2 million |"
	print "+--------------------------------------------+"
	
	primes = PrimesUpTo(2000000)
	print sum(primes)
	
