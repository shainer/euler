#!/usr/bin/python
# -*- coding: utf8 -*-

# FUNCTIONS
def PrimesUpTo(n):
	l = range(n + 1)
	for i in range(2, n + 1):
		for j in range(2 * i, n + 1, i):
			l[j] = 0
	return l

def CountDivisors(number):
	count = 2 # 1 and the number itself
	rad = number ** 0.5
	
	for i in range(2, int(rad) + 1):
		if number % i == 0:
			count += 2
	
	if (number % rad) == 0:
		count -= 1
	
	return count


if __name__ == "__main__":
	# MAIN CODE

	primes = PrimesUpTo(10 ** 7)
	numbers = [3, 4]
	divisors = [2, 3]
	count = 1 # counts 2 and 3
	
	print "+-------------------------------------------------------------------+"
	print "| Find the number of integers 1 < n < 10^(7), for which n and n + 1 |"
	print "| have the same number of positive divisors.                        |"
	print "+-------------------------------------------------------------------+"
	
	while numbers[1] <= (10 ** 7):
		n1 = numbers[0]
		n2 = numbers[1]
		
		if primes[n1] != 0:
			numbers[0] = n2
			numbers[1] = n2 + 1
			divisors[0] = divisors[1] = 0
			continue
		
		if primes[n2] != 0:
			numbers[0] = n2 + 1
			numbers[1] = n2 + 2
			divisors[0] = divisors[1] = 0
			continue
		
		if divisors[0] == 0:
			divisors[0] = CountDivisors(n1)
		if divisors[1] == 0:
			divisors[1] = CountDivisors(n2)
		
		if divisors[0] == divisors[1]:
			count += 1
		
		numbers[0] = numbers[1]
		numbers[1] = n2 + 1
		divisors[0] = divisors[1]
		divisors[1] = 0
	
	print count
