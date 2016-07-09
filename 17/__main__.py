#!/usr/bin/python
# -*- coding: utf8 -*-

# FUNCTIONS
def CountLetters(s):
	c = 0
	
	for s in s:
		if s != ' ' and s != '-':
			c += 1
	
	return c

if __name__ == "__main__":
	word = ""
	count = 0
	
	print "+---------------------------------------------------------------+"
	print "| If all the numbers from 1 to 1000 (one thousand) inclusive    |"
	print "| were written out in words, how many letters would be used?    |"
	print "+---------------------------------------------------------------+"
	
	units = [ "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen" ]
	tens = [ "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety" ]
	hundreds = [ "one hundred", "two hundred", "three hundred", "four hundred", "five hundred", "six hundred", "seven hundred", "eight hundred", "nine hundred" ]
	thousands = [ "one thousand" ]
	
	for i in range(20, 1000):
		si = str(i)
		
		if len(si) == 2:
			ten = int(si[0])
			unit = int(si[1])
			word = tens[ten - 2]
			if unit != 0:
				word += "-" + units[unit - 1]
		
		elif len(si) == 3:
			h = int(si[0])
			ten = int(si[1])
			unit = int(si[2])
			
			word = hundreds[h - 1]
			
			if ten == 1:
				word += " and " + units[unit + 9]
			else:
				if ten == 0 and unit != 0:
					word += " and " + units[unit - 1]
				elif tens != 0:
					word += " and " + tens[ten - 2]
					if unit != 0:
						word += "-" + units[unit - 1]
		
		count += CountLetters(word)

	for i in units:
		count += CountLetters(i)
	count += CountLetters("one thousand")
	
	print count
