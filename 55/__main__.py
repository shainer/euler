#!/usr/bin/python
# -*- coding: utf8 -*-

# FUNCTIONS
def IsPalindromic(num):
	strS = str(num)
	
	return (strS == strS[::-1])

def IsLychrel(number):
	list = [number]
	
	for j in range(50):
		s = str(number)
		num2 = int(s[::-1])
		somma = number + num2
		if IsPalindromic(somma) == True:
			return list
		if num2 < 10000 and somma < 10000:
			list.append(num2)
			list.append(somma)
		number = somma
	
	del list[::]
	return list
		

if __name__ == "__main__":
	count = 0
	array = range(10001)
	ret = []
	
	print "+--------------------------------------------------------+"
	print "| How many Lychrel numbers are there below ten thousand? |"
	print "+--------------------------------------------------------+"
	
	
	for i in range(10, 10001):
		if array[i] != 0:
			ret = IsLychrel(i)
			if len(ret) == 0:
				count += 1
			else:
				for x in ret:
					array[x] = 0
				
	print count
