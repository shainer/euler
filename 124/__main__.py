#!/usr/bin/python
# -*- coding: utf8 -*-

from math import sqrt

def SquareFree(n, squares):
  # A little optimization: if n is a perfect square, it's not square-free
  a = sqrt(n)
  if a == int(a):
    return False  

  # Check for square divisors
  for sq in squares:
    if sq > (n/2):
      return True

    if n % sq == 0:
      return False

def GetRadical(n, squares):
  rad = 1

  if SquareFree(n, squares):
    return n

  for i in range(n/2, 1, -1):
    if (n % i == 0) and SquareFree(i, squares):
      rad = i
      break  
  
  return rad

def SquaresUpTo(lim):
  sq = []

  for i in range(2, lim+1):
    sq.append(i**2)

  return sq
  
if __name__ == "__main__":
	# MAIN CODE
  radicals = []
  UPLIMIT = 10 ** 5
  squares = SquaresUpTo(UPLIMIT)

  print "+--------------------------------------------------------+"
  print "| Let E(k) be the kth element in the sorted n column.    |"
  print "| If rad(n) is sorted for 1 ≤ n ≤ 100000, find E(10000). |"
  print "+--------------------------------------------------------+"

  for n in range(1, UPLIMIT + 1):
    tupla = (GetRadical(n, squares), n)
    radicals.append(tupla)

  radicals = sorted(radicals)
  print radicals[9999][1]

  
