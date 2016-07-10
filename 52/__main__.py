#!/usr/bin/python
# -*- coding: utf8 -*-

# FUNCTIONS

def ExtractDigits(number):
	s = []
	
	for char in str(number):
		s.append(char)
	
	return sorted(s)

def CheckMultiples(number, digarray):
	
	if ExtractDigits(number*2) == digarray and ExtractDigits(number*3) == digarray and ExtractDigits(number*4) == digarray and ExtractDigits(number*5) == digarray and ExtractDigits(number*6) == digarray:
		return True
	return False

if __name__ == "__main__":
	
	print "+-------------------------------------------------+"
	print "| Find the smallest positive integer x, such that |"
	print "| 2x, 3x, 4x, 5x and 6x contain the same digits   |"
	print "+-------------------------------------------------+"

	for i in xrange(100000, 199999):
		digits = ExtractDigits(i)
		if CheckMultiples(i, digits) == True:
			print i
			break
	
