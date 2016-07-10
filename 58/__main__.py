#!/usr/bin/python
# -*- coding: utf8 -*-

from math import sqrt

# FUNCTIONS

def primes(n): 
	if n==2: return [2]
	elif n<2: return []
	s=range(3,n+1,2)
	mroot = n ** 0.5
	half=(n+1)/2-1
	i=0
	m=3
	while m <= mroot:
		if s[i]:
			j=(m*m-3)/2
			s[j]=0
			while j<half:
				s[j]=0
				j+=m
		i=i+1
		m=2*i+3
	return [2]+[x for x in s if x]

def IsPrime(aNumber):
  if aNumber < 2:
    return False
  if aNumber == 2:
    return True

  if (( aNumber / 2 ) * 2 == aNumber):
    return False
  else:
    klist = primes(int(sqrt(aNumber+1)))
    for k in klist[1:]:
      if (( aNumber / k ) * k == aNumber ):
        return False
  return True

def PrimesInDiagonals(d):
  count = 0
  
  for i in d:
    if IsPrime(i):
      count += 1

  return count

if __name__ == "__main__":
	# MAIN CODE

  l = 3
  perimeter = l * 4 - 4
  first = 2

  diagonals = []
  layer = []

  nprimes = 0
  ndiagonals = 1

  print "+----------------------------------------------------------------+"
  print "| If one complete new layer is wrapped around the number spiral, |"
  print "| a square spiral with side length 9 will be formed.             |"
  print "| If this process is continued, what is the side length of       |"
  print "| the square spiral for which the ratio of primes along both     |"
  print "| diagonals first falls below 10%?                               |"
  print "+----------------------------------------------------------------+"

  while True:
    layer = range(first, first + perimeter)
    
    diagonals.append(layer[l-2])
    diagonals.append(layer[2*l - 3])
    diagonals.append(layer[3*l - 4])

    ndiagonals += 4
    nprimes += PrimesInDiagonals(diagonals)

    if float(nprimes) / float(ndiagonals) < 0.1:
      break

    l += 2
    perimeter = l * 4 - 4
    first = layer[-1] + 1
    diagonals = []

  print l
