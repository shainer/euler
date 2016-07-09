#!/usr/bin/python
# -*- coding: utf8 -*-

if __name__ == "__main__":
	print "+---------------------------------------------+"
	print "| Work out the first ten digits of the sum of |"
	print "| one-hundred 50-digit numbers                |"
	print "+---------------------------------------------+"
		
	f = open("numbers", "r")
	result = 0
	
	for row in f:
		for num in row.split():
			result += int(num)
			
	for i in range(len(str(result)) - 10):
		result //= 10
	
	print result			
	f.close()
