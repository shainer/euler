#!/usr/bin/python
# -*- coding: utf8 -*-

import sys
	
# The main function
# @arguments: v is the array containing the number
# Return True if it satisfies the property, False otherwise
def IsInteresting(v):
	sum3 = v[2] + v[3] + v[4]
	isFiveDiv = (v[5] == 0) or (v[5] == 5)
	sum11 = v[5] - v[6] + v[7]
	
	concat7 = int(str(v[4]) + str(v[5]))
	isSevenDiv = (concat7 - (2 * v[6])) % 7 == 0
	
	concat13 = int(str(v[6]) + str(v[7]))
	isThirteenDiv = (concat13 - (9 * v[8])) % 13 == 0
	
	concat17 = int(str(v[7]) + str(v[8]))
	isSeventeenDiv = (concat17 - (5 * v[9])) % 17 == 0
	
	return ((v[3] % 2 == 0) and (sum3 % 3 == 0) and isFiveDiv and isSevenDiv and (sum11 % 11 == 0) and isThirteenDiv and isSeventeenDiv)
		
def swap(v, i , j):
	t = v[i]
	v[i] = v[j]
	v[j] = t


def rotateLeft(v, start, n):
	tmp = v[start]
	
	for i in range(start, n-1):
		v[i] = v[i+1]
	
	v[n-1] = tmp


# Recursive lexicographic permutation
def permute(v, start, n):
	if IsInteresting(v):
		print v # actually we just print all the numbers
			
	if start < n:
		for i in range(n-2, start - 1, -1):
			for j in range(i+1, n):
				swap(v, i, j)
				permute(v, i+1, n)
			rotateLeft(v, i, n)

if __name__ == "__main__":
	n = 10
	v = range(n)
	
	print "+-------------------------------------------------------------------+"
	print "| Find the sum of all 0 to 9 pandigital numbers with this property. |"
	print "+-------------------------------------------------------------------+"

	permute(v, 0, n)
