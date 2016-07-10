#!/usr/bin/python
# -*- coding: utf8 -*-

D = dict()	

def PentagonalsUpTo(max):
	list1 = []
	
	for n in range(max+1):
		result = (n * (3 * n - 1)) // 2
		list1.append(result)
		D[result] = True
	
	return list1


if __name__ == "__main__":
	print "+----------------------------------------------------------+"
	print "| Find the pair of pentagonals number Pj and Pk for which  |"
	print "| their sum and difference is pentagonal and D = |Pk - Pj| |"
	print "| is minimised; what is the value of D?                    |"
	print "+----------------------------------------------------------+"
	minD = 100000000
	
	pentagonals = PentagonalsUpTo(1000000)
	
	for pj in range(10001):
		for pk in range(pj + 1, 10001):
			
			sum1 = pentagonals[pj] + pentagonals[pk]
			diff = pentagonals[pk] - pentagonals[pj]
			
			if D.get(sum1, False) == True and D.get(diff, False) == True:
				if diff < minD:
					minD = diff
	
	print minD
