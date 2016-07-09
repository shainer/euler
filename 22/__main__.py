#!/usr/bin/python
# -*- coding: utf8 -*-

# FUNCTIONS

def AlphValue(name):
	sumA = 0
	
	for c in name:
		sumA += ord(c) - ord('A') + 1
	return sumA

if __name__ == "__main__":
	names = []
	sum = 0
	
	print "+----------------------------------------------------+"
	print "| What is the total of all name scores in names.txt? |"
	print "+----------------------------------------------------+"
	
	f = open("names.txt", "r")
	
	for row in f:
		for name in row.split():
			names.append(name)
	names.sort()
	
	for n in xrange(len(names)):
		sum += (n+1) * AlphValue(names[n])
	
	print sum
	f.close()
