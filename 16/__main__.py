#!/usr/bin/python
# -*- coding: utf8 -*-

# FUNCTIONS

if __name__ == "__main__":
	total = 0
	
	print "+-----------------------------------------------------+"
	print "| What is the sum of the digits of the number 2^1000? |"
	print "+-----------------------------------------------------+"
	
	for i in str(2**1000):
		total += int(i)
	print total
