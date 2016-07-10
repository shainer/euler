#!/usr/bin/python
# -*- coding: utf8 -*-

# FUNCTIONS

# The well-known sieve
def PrimesUpTo(n):
	l = range(n + 1)
	
	for i in range(2, n + 1):
		for j in range(2 * i, n + 1, i):
			l[j] = 0
			
	return l

# Makes an array with all the primes one after another
# without uncomfortable zeros in the middle
def CatPrimes(p):
	new = []
	
	for i in range(len(p)):
		if p[i] != 0:
			new.append(p[i])
	
	return new

def Phi(num, primes, pConcat):
	product = float(1.0)
	
	if primes[num] != 0:
		return (num - 1)
	
	for p in pConcat:
		if p == 1:
			continue
		if p > (num // 2):
			break
		
		if num % p == 0:
			rec = float(1) / float(p)
			product *= float(1 - rec)
	
	return (num * product)
	

if __name__ == "__main__":
	# MAIN CODE
	BIG = 10 ** 6
	
	maxValue = 0
	maxN = 0
	
	primes = PrimesUpTo(BIG)
	pConcat = CatPrimes(primes)
	
	for n in range(2, BIG):
		print n    
		y = Phi(n, primes, pConcat)
		result = float(n) / float(y)
		
		if result > maxValue:
			maxValue = result
			maxN = n
	
	print maxN
