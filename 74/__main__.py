#!/usr/bin/python
# -*- coding: utf8 -*-

def FactorialSum(n):
	factsum = 0
	factorials = [0, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880 ]
	
	for j in str(n):
		factsum += factorials[int(j)]
		
	return (factsum)
	
# FUNCTIONS
def LenChain(st, ar):
	occurrences = []
	conteggio = 1
	
	while True:
		n = FactorialSum(st)
		if n in occurrences:
			return conteggio
		
		occurrences.append(n)
		
		if n < 1000000:
			ar[n] = 0
		st = n
		conteggio += 1

if __name__ == "__main__":

	array = range(1000000)
	count = 0
	
	print "+------------------------------------------------------------+"
	print "| How many chains, with a starting number below one million, |"
	print "| contain exactly sixty non-repeating terms?                 |"
	print "+------------------------------------------------------------+"
	
	for starting in array:
		if array[starting] == 0:
			continue
		
		if LenChain(starting, array) == 60:
			count += 1
	
	print count
