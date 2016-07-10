#!/usr/bin/python
# -*- coding: utf-8 -*-

from math import *

class LongNumber:
	def __init__(self, b, e):
		self.base = b
		self.exponent = e

	def __cmp__(self, other):
		if not isinstance(other, LongNumber):
			raise "Not implemented!"

		e = log(self.base, other.base) * self.exponent

		if (e < other.exponent):
			return -1
		elif (e > other.exponent):
			return +1

		return 0

	def __str__(self):
		return "%d**%d" % (self.base, self.exponent)

def ReadFile(name):
	f = open(name)
	r = []

	for line in f:
		a = line.strip().split(',')

		b = int(a[0])
		e = int(a[1])

		t = LongNumber(b, e)
		r.append(t)

	f.close()
	return r

if __name__ == "__main__":
	r = ReadFile("base_exp.txt")
	n = len(r)
	m = 0

	for i in range(1, n):
		if (r[m] < r[i]):
			m = i

	print "The maximum is on line %d (0-based)." % (m)
