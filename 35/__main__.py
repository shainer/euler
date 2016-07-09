#!/usr/bin/python
# -*- coding: utf8 -*-

# FUNCTIONS
def PrimesUpTo(n):
	l = range(n + 1)
	for i in range(2, n+1):
		for j in range(2 * i, n+1, i):
			l[j] = 0
	return l
	
def IsCircularPrime(list, number):
	length = len(str(number))
	x = length-1
	count = 0
	
	if length == 1:
		return True
	
	for i in range(x):
		cifra = number % 10
		number //= 10
		number += cifra * (10 ** x)
		if list[number] != 0:
			 count += 1
	if count == x:
		return True
		
	return False
	
	

if __name__ == "__main__":
	print "+-----------------------------------------------------+"
	print "| How many circular primes are there below 1 million? |"
	print "+-----------------------------------------------------+"
	count = 0

	list = PrimesUpTo(1000000)
	
	for n in list:
		if n != 0 and IsCircularPrime(list, n) == True:
			count += 1
				
	print (count-1)
