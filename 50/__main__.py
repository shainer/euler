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
	

if __name__ == "__main__":
	# MAIN CODE
	MAXIMUM = 10 ** 6
	primes = PrimesUpTo(MAXIMUM)
	pConcat = CatPrimes(primes)
	primeLen = len(pConcat)
	
	sum = 0
	mPrime = 0
	mOperations = 0
	
	beginning = 1
	end = beginning
	
	print "+---------------------------------------------------+"
	print "| Which prime, below one-million, can be written as |"
	print "| the sum of the most consecutive primes?           |"
	print "+---------------------------------------------------+"
	
	while beginning < primeLen:
		while fine < primeLen:
			sum += pConcat[end]
			
			# As you note, you need to stop only the most internal cycle here
			if sum > MAXIMUM:
				break

			if primes[sum] != 0 and (end - beginning + 1) > mOperations:
				mPrime = sum
				mOperations = (end - beginning + 1) # this indicates the number of primes in the sum
				
			end += 1
		
		# Start again, but from the next prime in pConcat
		sum = 0
		beginning += 1
		end = beginning
	
	print mPrime
	

