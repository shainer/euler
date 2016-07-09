#!/usr/bin/python
# -*- coding: utf8 -*-

# FUNCTIONS

def UpdateDay(g):
	if g == 6:
		return 0
	
	return (g+1)

def UpdateNumDay(ng, m, isleap):
	mesi30 = [3, 5, 8, 10]
	
	if m in mesi30 and ng == 30:
		return 1
	if m == 1: # Febbraio
		if isleap == 1 and ng == 29:
			return 1
		if isleap == 0 and ng == 28:
			return 1
	if m not in mesi30 and ng == 31:
		return 1
	
	return (ng + 1)

def UpdateMonth(ng, m):
	if (ng == 1):
		if m == 11: # dicembre
			return 0
		return (m + 1)
	
	return m

def IsLeap(a):
	return (a % 4 == 0)
	
def UpdateYear(ng, m, a):
	if ng == 1 and m == 0:
		return (a + 1)
	
	return a

if __name__ == "__main__":
	leap = 0
	mese = 0
	giorno = 0
	anno = 1900
	count = 0
	
	print "+--------------------------------------------------------+"
	print "| How many Sundays fell on the first of the month during |" 
	print "| the twentieth century (1 Jan 1901 to 31 Dec 2000)?     |"
	print "+--------------------------------------------------------+"
	
	while anno <= 2000:
		leap = IsLeap(anno)
	
		numgiorno = 1	
		for x in range(1, 365 + 1 + leap):
			if giorno == 6 and numgiorno == 1 and anno != 1900:
				count += 1
		
			giorno = UpdateDay(giorno)
			numgiorno = UpdateNumDay(numgiorno, mese, leap)
			mese = UpdateMonth(numgiorno, mese)
			anno = UpdateYear(numgiorno, mese, anno)
		
	print count
