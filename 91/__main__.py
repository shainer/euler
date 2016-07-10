#!/usr/bin/python
# -*- coding: utf8 -*-

# FUNCTIONS
# Compute the dot product of two vectors
# Called also "scalar product", because the result is a real number
def DotProduct(v1, v2):
	product = 0
	
	for i in range(len(v1)):
		product += (v1[i] * v2[i])
	
	return product

if __name__ == "__main__":
	count = 0
	limit = 51
	
	print "+----------------------------------------------------------+"
	print "| Given that 0 ≤ x_(1), y_(1), x_(2), y_(2) ≤ 50, how many |"
	print "| right triangles can be formed?                           |"
	print "+----------------------------------------------------------+"
	
	for x1 in range(limit):
		for y1 in range(limit):
			for x2 in range(limit):
				for y2 in range(limit):
					if (x1 == 0 and y1 == 0) or (x2 == 0 and y2 == 0) or (x2 == x1 and y2 == y1):
						continue

                    # Avoids counting the same triangle twice.					
					if (y2 - x2 < y1 - x1):
						l1 = [x1, y1]
						l2 = [x2, y2]
						l3 = [x2 - x1, y2 - y1]
						if DotProduct(l1, l2) == 0 or DotProduct(l1, l3) == 0 or DotProduct(l2, l3) == 0:
							count += 1
	
	print count
					
					
