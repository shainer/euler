#!/usr/bin/python
# -*- coding: utf8 -*-

# FUNCTIONS

def PrimesUpTo(n):
	l = range(n + 1)
	for i in range(2, n + 1):
		for j in range(2 * i, n + 1, i):
			l[j] = 0
	return l

def FullReptend(p):
  if (10 ** (p-1)) % p != 1:
    return False

  for k in range(1, p-1):
    if (10 ** k % p) == 1:
      return False

  return True

if __name__ == "__main__":
  primes = PrimesUpTo(1000)

  print "+---------------------------------------------------+"
  print "| Find the value of d < 1000 for which 1/d contains |"
  print "| the longest recurring cycle in its decimal        |"
  print "| fraction part.                                    |"
  print "+---------------------------------------------------+"

  for i in primes[::-1]:
    if primes[i] != 0 and FullReptend(i):
      print i
      break

