#!/usr/bin/python
# -*- coding: utf8 -*-

# FUNCTIONS

if __name__ == "__main__":
	list = []
	
	print "+-------------------------------------------------------+"
	print "| How many distinct terms are in the sequence generated |"
	print "| by a^b for 1<a<101 and 1<b<101?                       |"
	print "+-------------------------------------------------------+"
	
	for a in range(2, 101):
		for b in range(2, 101):
			list.append(a**b)
	
	list2 = set(list)
	print len(list2)
