#!/usr/bin/python
# -*- coding: utf-8 -*-

def Combinations(n, combos, i):
	if (n <= 1) or (i == 0):
		return 1

	x = (n // combos[i])
	count = 0

	for c in range(x, (0 - 1), -1):
		count += Combinations(n - c * combos[i], combos, i - 1)

	return count

if __name__ == "__main__":
	C = [1, 2, 5, 10, 20, 50, 100, 200]

	print "There are", Combinations(200, C, len(C) - 1), "different ways."
