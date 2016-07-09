#!/usr/bin/python
# -*- coding: utf8 -*-

# FUNCTIONS
def PrimesUpTo(n):
	l = [ x for x in range(n + 1) ]
	for i in range(2, n + 1):
		for j in range(2 * i, n + 1, i):
			l[j] = 0
	return l

if __name__ == "__main__":
	primes = PrimesUpTo(100000)
	maxcount = 0
	maxproduct = 0
	
	# n² + an + b
	
	for a in range(-1000, 1001):
		for b in range(-1000, 1001):
			if abs(b) in primes:
				n = 1
				count = 0
				while 1:
					result = n**2 + a*n + b
					if primes[result] != 0:
						count += 1
						n+=1
					else:
						break
				if count > maxcount:
					maxcount = count
					maxproduct = a*b
	
	print maxproduct
