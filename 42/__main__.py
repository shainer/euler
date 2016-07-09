#!/usr/bin/python
# -*- coding: utf8 -*-

# FUNCTIONS
def AlphValue(name):
	sumA = 0
	
	for c in name:
		sumA += ord(c) - ord('A') + 1
	return sumA
	
def TriangleNumbers(upper):
	list = []
	
	for i in range(upper+1):
		res = (i * (i+1)) // 2
		list.append(res)
	return list

if __name__ == "__main__":
	file = open("words.txt", "r")
	words = []
	values = []
	maxValue = 0
	count = 0
	
	for row in file:
		for word in row.split():
			words.append(word)
			
	for word in words:
		value = AlphValue(word)
		values.append(value)
		if value > maxValue:
			maxValue = value
			
	triangles = TriangleNumbers(maxValue * 26)
	
	for i in values:
		if i in triangles:
			count+=1
	print count
	file.close()
