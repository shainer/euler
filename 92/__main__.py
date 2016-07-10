#!/usr/bin/python
# -*- coding: utf8 -*-

# FUNCTIONS

def Product(num):
	Sn = str(num)
	p = 0
	
	for i in Sn:
		p += int(i)** 2
	
	return p
		
	

def Sequence(number):
	seq = [number]
	total = 0
		
	while total != 1 and total != 89:
		total = Product(number)
		if total < 10000000:
			seq.append(total)
		number = total
	
	if total == 1:
		return seq
	else:
		del seq[::]
		return seq
	

if __name__ == "__main__":
	# MAIN CODE
	array = range(10000000)
	count = 0
	list = []
	
	for x in array:
		if array[x] != 0:
			list = Sequence(x)
			if len(list) == 0:
				count += 1
			else:
				for i in list:
					array[i] = 0
	
	print count
