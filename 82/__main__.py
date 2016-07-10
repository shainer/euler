#!/usr/bin/python
# -*- coding: utf-8 -*-

import copy

def ReadFile(name):
	f = open(name)
	M = []

	for line in f:
		R = []

		for word in line.split(','):
			R.append(int(word))

		M.append(R)

	f.close()
	return M

def GetValue(M, y, x):
	try:
		return M[y][x]
	except:
		return 1e10000

def PrintMatrix(M):
	Ly = len(M)

	for y in range(Ly):
		Lx = len(M[y])

		for x in range(Lx):
			print "%6d" % (M[y][x]),

		print

def Elaborate(M):
	O = copy.deepcopy(M)

	#
	# Number of rows and columns.
	#
	n = len(M)

	for x in range((n - 1) - 1, (0 - 1), -1):
		for y in range(n):
			M[y][x] = M[y][x] + GetValue(M, y, x + 1)

		for y in range(n):
			M[y][x] = min(M[y][x], O[y][x] + GetValue(M, y - 1, x))

		for y in range((n - 1), (0 - 1), -1):
			M[y][x] = min(M[y][x], O[y][x] + GetValue(M, y + 1, x))

if __name__ == "__main__":
	M = ReadFile("matrix.txt")

	print " [=>] Original matrix:"
	PrintMatrix(M)

	#
	# Process the matrix and find the solution.
	#
	Elaborate(M)

	print
	print " [=>] Resulting matrix:"
	PrintMatrix(M)

	n = len(M)
	m = min([ M[y][0] for y in range(n) ])

	print
	print " [=>] The minimum path sums up to %d." % (m)
