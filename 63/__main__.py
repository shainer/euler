#!/usr/bin/python
# -*- coding: utf8 -*-

# FUNCTIONS

if __name__ == "__main__":
	# MAIN CODE
  UPLIMIT = 1000
  count = 0

  print "+-----------------------------------------------------------------------+"
  print "| How many n-digit positive integers exist which are also an nth power? |"
  print "+-----------------------------------------------------------------------+"

  for exp in range(1, UPLIMIT):
    for base in range(1, 10):
      power = base ** exp

      if (power / (10 ** (exp-1))) > 0:
        count += 1

  print count
