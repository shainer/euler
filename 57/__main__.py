#!/usr/bin/python
# -*- coding: utf8 -*-

# FUNCTIONS

def CountDigits(n):
  digits = 0

  while n != 0:
    digits += 1
    n /= 10

  return digits

if __name__ == "__main__":
	# MAIN CODE
  count = 0
  p = 3
  q = 2

  print "+----------------------------------------------------------+"
  print "| In the first one-thousand expansions for the square root |"
  print "| of two, how many fractions contain a numerator with more |"
  print "| digits than denominator?                                 |"
  print "+----------------------------------------------------------+"

  for i in range(1, 1000):
    p1 = p + (2 * q)
    q1 = p + q

    if CountDigits(p) > CountDigits(q):
      count += 1

    p = p1
    q = q1

  print count
