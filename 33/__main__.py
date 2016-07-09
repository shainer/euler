#!/usr/bin/python
# -*- coding: utf8 -*-

# FUNCTIONS
def IsCurious(num, den):
	yes = 0
	digits = [0, 0]
	
	for c in str(num):
		if c in str(den):
			yes = 1
			break	
	if yes == 0:
		return False
	
	for x in str(num):
		if x != c:
			digits[0] = int(x)
	
	for x in str(den):
		if x != c:
			digits[1] = int(x)
			
	res1 = float(num) / float(den)
	res2 = float(digits[0]) / float(digits[1])
	
	if res1 == res2:
		return True
	return False	
	

if __name__ == "__main__":
	
	for den in range(12, 100):
		for num in range(11, den):
			if den % 10 == 0 or num % 10 == 0 or den % 11 == 0:
				continue
			
			if IsCurious(num, den):
				print str(num) + "/" + str(den)
