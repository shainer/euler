#!/usr/bin/python
# -*- coding: utf8 -*-

import psyco
psyco.full()

# FUNCTIONS

def HasProperty(num):
	sumDigits = 0
	
	for dig in str(num):
		sumDigits += int(dig)
	
	if sumDigits > num or num % sumDigits != 0 or sumDigits == 1:
		return False
	
	if sumDigits == num:
		return True
	
	pow = sumDigits
	while pow < num:
		pow *= sumDigits
		if pow == num:
			return True
	
	return False

if __name__ == "__main__":
	# MAIN CODE
	i = 0
	num = 10
	
	while True:
		if HasProperty(num):
			i += 1
			print "a(" + str(i) + ") = " + str(num)
		
		num += 1
