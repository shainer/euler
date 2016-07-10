#!/usr/bin/python
# -*- coding: utf8 -*-

# FUNCTIONS

# RULES TO FOLLOW
# Numerals must be arranged in descending order of size.
#   1. Only I, X, and C can be used as the leading numeral in part of a subtractive pair.
#   2. I can only be placed before V and X.
#   3. X can only be placed before L and C.
#   4. C can only be placed before D and M.

def ToDigits(numS):
	res = 0
	
	for ch in range(len(numS)):
		if numS[ch] == 'M':
			res += 1000
		
		elif numS[ch] == 'D':
			res += 500
		
		elif numS[ch] == 'C':
			if ch == len(numS) - 1:
				res += 100
				continue
			
			if numS[ch + 1] == 'D' or numS[ch + 1] == 'M':
					res -= 100		
			else:
				res += 100
		
		elif numS[ch] == 'L':
			res += 50
		
		elif numS[ch] == 'X':
			if ch == len(numS) - 1:
				res += 10
				continue
			
			if numS[ch + 1] == 'L' or numS[ch + 1] == 'C':
				res -= 10
			else:
				res += 10
		
		elif numS[ch] == 'V':
			res += 5
		
		elif numS[ch] == 'I':
			if ch == len(numS) - 1:
				res += 1
				continue
			
			if numS[ch + 1] == 'V' or numS[ch + 1] == 'X':
				res -= 1
			else:
				res += 1
	
	return res
			

def ToMinimalForm(num):
	number = []
	tmpS = ""
	specials = [[0, "I", 0, 0, "IV", "V", 0, 0, 0, "IX", 0], [0, "X", 0, 0, "XL", "L", 0, 0, 0, "IL", 0], [0, "C", 0, 0, "CD", "D", 0, 0, 0, "CM", 0]]
	
	for i in range(4):
		cifra = num % 10
		
		if i == 3:
			for s in range(cifra):
				tmpS += "M"
			number.append(tmpS)
			break
		
		if cifra == 4 or cifra == 9:
			tmpS = specials[i][cifra]
		else:
			if cifra >= 5:
				tmpS += specials[i][5]
				cifra -= 5
				
			for s in range(cifra):
				tmpS += specials[i][1]
					
		
		num /= 10
		number.append(tmpS)
		tmpS = ""
		
		if num == 0:
			break
	
	return ''.join(reversed(number))
	

if __name__ == "__main__":
	
	print "+----------------------------------------------------------------------+"
	print "| Find the number of characters saved by writing all the Roman numbers |"
	print "| in their minimal form                                                |"
	print "+----------------------------------------------------------------------+"
	
	romans = open("roman.txt", "r")
	saved = 0
	
	for rNumber in romans:
		newRoman = ToMinimalForm(ToDigits(rNumber))
		print newRoman
		saved += (len(rNumber) - 2 - len(newRoman))
		
	print saved
	romans.close()
