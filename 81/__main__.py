#!/usr/bin/python
# -*- coding: utf8 -*-


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
	if (y == 0) and (x < 0):
		return 0
	elif (y < 0) or (x < 0):
		return 1e10000
	else:
		return M[y][x]

if __name__ == "__main__":
	M = ReadFile("matrix.txt")
	Ly = len(M)
	Lx = len(M[0])
	
	print "+-----------------------------------------------------------------------------------------+"
	print "| Find the minimal path sum, in matrix.txt, a 31K text file containing a 80 by 80 matrix, |"
	print "| from the top left to the bottom right by only moving right and down.                    |"
	print "+-----------------------------------------------------------------------------------------+"

	for y in range(0, Ly):
		for x in range(0, Lx):
			T = GetValue(M, y - 1, x)
			L = GetValue(M, y, x - 1)

			M[y][x] = min(T, L) + M[y][x]

	print M[79][79]
