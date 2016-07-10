#!/usr/bin/python
# -*- coding: utf8 -*-

# FUNCTIONS
def SqSeries(end):
	total = 0
	
	for i in xrange(1, end + 1):
		total += i**i
	return total	

if __name__ == "__main__":
	print "The number is " + str(SqSeries(1000))
