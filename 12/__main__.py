#!/usr/bin/python2
# -*- coding: utf8 -*-

import sys
import math
import psyco
psyco.full()

# FUNCTIONS
def Divisors(number):
	count = 2 # 1 and the number itself
	
	for i in range(2, int(number **0.5) + 1):
		if number % i == 0:
			count += 2
	
	return count

	
print "+--------------------------------------------------------+"
print "| What is the value of the first triangle number to have |"
print "| over five hundred divisors?                            |"
print "+--------------------------------------------------------+"
	
n = 8
while True:
	triangle = (n * (n+1)) // 2
	if Divisors(triangle) > 500:
		break
		n += 1
	
print triangle
