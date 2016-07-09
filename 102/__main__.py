#!/usr/bin/python
# -*- coding: utf8 -*-

import psyco
psyco.full()

# FUNCTIONS

# The new vector contains the difference of the correspondent elements in v1 and v2
def DiffVectors(v1, v2):
	d = []
	
	for i in range(len(v1)):
		d.append(v1[i] - v2[i])
	
	return d

# Compute the dot product of two vectors
# Called also "scalar product", because the result is a real number
def DotProduct(v1, v2):
	product = 0
	
	for i in range(len(v1)):
		product += (v1[i] * v2[i])
	
	return product

# Vectorial formula
def ContainsOrigin(A, B, C, O):
	v0 = DiffVectors(C, A)
	v1 = DiffVectors(B, A)
	v2 = DiffVectors(O, A)

	dot00 = DotProduct(v0, v0)
	dot01 = DotProduct(v0, v1)
	dot02 = DotProduct(v0, v2)
	dot11 = DotProduct(v1, v1)
	dot12 = DotProduct(v1, v2)
	invDenom = float(1) / float((dot00 * dot11) - (dot01 * dot01))
	
	u = ((dot11 * dot02) - (dot01 * dot12)) * invDenom
	v = ((dot00 * dot12) - (dot01 * dot02)) * invDenom
	
	return (u > 0 and v > 0 and (u + v) < 1)

if __name__ == "__main__":
	A = [0, 0]
	B = [0, 0]
	C = [0, 0]
	O = [0, 0]
	
	print "+--------------------------------------------------------------------------+"
	print "| Find the number of triangles for which the interior contains the origin. |"
	print "+--------------------------------------------------------------------------+"
	
	fptr = open("triangles.txt", "r")
	count = 0
	
	for line in fptr:
		list = line.split(",")
		A[0] = int(list[0])
		A[1] = int(list[1])
		B[0] = int(list[2])
		B[1] = int(list[3])
		C[0] = int(list[4])
		C[1] = int(list[5])
			
		if ContainsOrigin(A, B, C, O):
			count += 1
			
	print count
	fptr.close()
