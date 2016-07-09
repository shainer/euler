#!/usr/bin/python
# -*- coding: utf8 -*-

# FUNCTIONS
def Factorial(n):
	
	if n==1 or n==2:
		return n
	else:
		return n * (Factorial(n-1))

if __name__ == "__main__":
	sum = 0
	
	print "+-------------------------------------------+"
	print "| Find the sum of digits in the number 100! |"
	print "+-------------------------------------------+"
	
	num = Factorial(100)
	
	for n in str(num):
		sum += int(n)
	print "The sum of digits in 100! is " + str(sum)
