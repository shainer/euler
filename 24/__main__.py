#!/usr/bin/python
# -*- coding: utf8 -*-

import sys

# FUNCTIONS
def swap(v, i , j):
	t = v[i]
	v[i] = v[j]
	v[j] = t


def rotateLeft(v, start, n):
	tmp = v[start]
	
	for i in range(start, n-1):
		v[i] = v[i+1]
	
	v[n-1] = tmp

def permute(v, start, n):
	print v
	
	if start < n:
		for i in range(n-2, start - 1, -1):
			for j in range(i+1, n):
				swap(v, i, j)
				permute(v, i+1, n)
			rotateLeft(v, i, n)

if __name__ == "__main__":
	
	if len(sys.argv) < 3:
		print "Insufficient argument list."
		print "Usage:"
		print sys.argv[0] + " <start number> <number of elements>"
		exit(-1)

	n = int(sys.argv[2])
	v = range(int(sys.argv[1]), n)
	
	permute(v, int(sys.argv[1]), n)
