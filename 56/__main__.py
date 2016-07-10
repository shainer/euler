#!/usr/bin/python
# -*- coding: utf8 -*-

# FUNCTIONS

def SumDigits(pot):
	total = 0
	
	for x in str(pot):
		total += int(x)
	
	return total

if __name__ == "__main__":
	maxsum = 0
	power = 0
	
	
	print "+----------------------------------------------------+"
	print "| Considering natural numbers of the form, a^(b),    |"
	print "| where a, b < 100, what is the maximum digital sum? |"
	print "+----------------------------------------------------+"
	
	for a in range(100):
		for b in range(100):
			power = a**b
			if '9' not in str(power):
				continue
			
			dsum = SumDigits(power)
			if dsum > maxsum:
				maxsum = dsum
	
	print maxsum
