#!/usr/bin/python
# -*- coding: utf8 -*-

# FUNCTIONS
def PrimesUpTo(n):
	l = [ x for x in range(n + 1) ]
	for i in range(2, n + 1):
		for j in range(2 * i, n + 1, i):
			l[j] = 0
	return l

def ArePermutation(n1, n2):
	sn1 = ''.join(sorted(str(n1)))
	sn2 = ''.join(sorted(str(n2)))
	
	return (sn1 == sn2)

if __name__ == "__main__":

	primes = PrimesUpTo(10000)

	for first in xrange(1001, 9973):
		if primes[first] == 0 or first == 1487:
			continue
		
		second = first + 3330
		third = second + 3330
		
		if primes[second] != 0 and primes[third] != 0 and ArePermutation(first, second) and ArePermutation(first, third):
			break
	
	print str(first) + str(second) + str(third)
