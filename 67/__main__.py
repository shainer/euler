#!/usr/bin/python
# -*- coding: utf8 -*-

# FUNCTIONS

if __name__ == "__main__":
	trF = open("triangle.txt", "r")
	triangle = [range(1) * 100] * 100
	i = 0
	j = 0
	
	for line in trF:
		triangle[i] = line.split()
		i+=1
		
	for line in range(98, -1, -1):
		for single in range(line+1):
			sum1 = int(triangle[line][single]) + int(triangle[line+1][single])
			sum2 = int(triangle[line][single]) + int(triangle[line+1][single+1])
			if sum1 >= sum2:
				triangle[line][single] = str(sum1)
			else:
				triangle[line][single] = str(sum2)
				
	print triangle[0][0]
			
	trF.close()
