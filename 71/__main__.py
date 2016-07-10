#!/usr/bin/python
# -*- coding: utf8 -*-

# FUNCTIONS

if __name__ == "__main__":
	# MAIN CODE
  a = 2
  b = 5

  c = 3
  d = 7

  print "+------------------------------------------------------------------+"
  print "| By listing the set of reduced proper fractions for d ≤ 1,000,000 |"
  print "| in ascending order of size, find the numerator of the fraction   |"
  print "| immediately to the left of 3/7.                                  |"
  print "+------------------------------------------------------------------+"


  # While there's another neighbour in a Faray sequence...
  while (b*c - a*d) == 1:
    # Calculate the neighbour, which is the mediant
    e = a + c
    f = b + d

    if f > (10 ** 6): # exceeding limits for the denominator
      break

    a = e
    b = f

  # In no Faray sequence another proper reduced fraction nearer to 3/7 is present
  print a
