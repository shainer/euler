#!/usr/bin/python
# -*- coding: utf8 -*-

# FUNCTIONS
def PrimesUpTo(n):
	l = [ x for x in range(n + 1) ]
	for i in range(2, n + 1):
		for j in range(2 * i, n + 1, i):
			l[j] = 0
	return l

def IsTruncRight(num, list):
	length = len(str(num))
	count = 0
	
	for i in range(1, length):
		num //= 10
		if num in list:
			count +=1
	
	if count == length - 1:
		return True
	return False
			
def IsTruncLeft(num, list):
	length = len(str(num))
	count = 0
		
	for i in range(1, length):
		cifra = num // (10 ** (length-i))
		num -= cifra * (10 ** (length-i))
		if num in list:
			count += 1
	
	if count == length - 1:
		return True
	return False
	
def HasOddDigits(num):
	for c in str(num):
		if int(c) % 2 == 0:
			return False
	return True

if __name__ == "__main__":
	count = 0
	result = 0
	
	print "+--------------------------------------------------------------+"
	print "| Find the sum of the only 11 primes that are both truncatable |"
	print "| from left to right and right to left.                        |"
	print "+--------------------------------------------------------------+"
	
	primes = PrimesUpTo(1000000)
	primes[1] = 0
	
	for number in range(11, 1000000):
		if primes[number] != 0 and HasOddDigits(number) == True and IsTruncRight(number, primes) == True and IsTruncLeft(number, primes) == True:
			print "Number " + str(number) + " is truncatable"
			count +=1
			result += number
			if count == 11:
				break
	
	print result
