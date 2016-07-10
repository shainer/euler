#!/usr/bin/python
# -*- coding: utf8 -*-

# FUNCTIONS

# Calculate primes using the sieve of Erathosten
def PrimesUpTo(n):
	l = range(n+1)
	for i in range(2, n + 1):
		for j in range(2 * i, n + 1, i):
			l[j] = 0
	return l

# Returns an array of squares
def SquaresUpTo(n):
	l = [0] * (n+1)
	
	for i in range(1, (n ** 0.5) + 1):
		l[i ** 2] = i ** 2

	return l
	
def GoldbachWasWrong(number, pr, sq):
	i = 0
		
	for i in pr:
		temp = number
		if i >= number:
			break
		if pr[i] == 0:
			continue
		
		temp -= i
		temp //= 2
		if sq[temp] != 0:
			return False
	
	return True # yes he was! ;)
 

if __name__ == "__main__":
	limite = 10000

	primes = PrimesUpTo(limite)
	primes[2] = 0
	squares = SquaresUpTo(limite)

	print "+---------------------------------------------------+"
	print "| What is the smallest odd composite that cannot be |"
	print "| written as the sum of a prime and twice a square? |"
	print "+---------------------------------------------------+"

	for i in range(35, limite, 2):
		if primes[i] != 0: # composite means it cannot be prime itself
			continue
		if GoldbachWasWrong(i, primes, squares) == True:
			break

	print i
