#!/usr/bin/python
# -*- coding: utf8 -*-

# FUNCTIONS
numbers = range(1000001)

def HailstoneSequence(num):
	copia = num
	counter = 0
	
	while copia != 1:
		if copia % 2 == 0:
			copia //= 2
		else:
			copia = 3 * copia + 1
		
		# If a number appears in a determine sequence, it would never produce
		# a longer chain, so it's not controlled	
		if copia <= 1000000:
			numbers[copia] = 0
		counter += 1
	
	return counter

if __name__ == "__main__":
	maxchain = 0
	chain = 0
	maxstart = 0

	print "+--------------------------------------------------+"
	print "| Which starting number, under 1 million, produces |"
	print "| the longest Hailstone sequence?                  |"
	print "+--------------------------------------------------+"
	
	for i in numbers:
		if numbers[i] != 0:
			chain = HailstoneSequence(i)
			if chain > maxchain:
				maxchain = chain
				maxstart = i
				
	print maxstart
