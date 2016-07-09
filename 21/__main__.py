#!/usr/bin/python
# -*- coding: utf8 -*-

# FUNCTIONS
def SumDivisors(num):
	sum = 0
	
	for i in range(1, num // 2 + 1):
		if num % i == 0:
			sum += i
	return sum

if __name__ == "__main__":
	print "+----------------------------------------------------------+"
	print "| Evaluate the sum of all the amicable numbers under 10000 |"
	print "+----------------------------------------------------------+"
	
	array = range(10000)
	
	for n in array:
		dn = SumDivisors(n)
		
		# Delete perfect numbers like 6
		if dn == n:
			array[n] = 0
			continue
		
		elif SumDivisors(dn) != n:
			array[n] = 0
			
	print str(sum(array))
