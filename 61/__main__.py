#!/usr/bin/python
# -*- coding: utf8 -*-

# FUNCTIONS

def GeneratePolygonal(lowLimit, upLimit, side):
  a = []

  for n in range(lowLimit):
    if side == 0:
      polygon = (n * (n+1)) / 2
    elif side == 1:
      polygon = n ** 2
    elif side == 2:
      polygon = (n * (3*n - 1)) / 2
    elif side == 3:
      polygon = n * (2*n - 1)
    elif side == 4:
      polygon = (n * (5*n - 3)) / 2
    elif side == 5:
      polygon = n*(3*n - 2)

    if polygon >= upLimit:
      break

    if polygon >= lowLimit and LastTwoDigits(polygon) >= 10:
      a.append(polygon)

  return a

def LastTwoDigits(n):
  return (n % 100)

def LastTwoDigitsStr(n):
  return str(n % 100)

if __name__ == "__main__":
	# MAIN CODE

  triangles = GeneratePolygonal(1000, 10000, 0)
  squares = GeneratePolygonal(1000, 10000, 1)
  pentagonals = GeneratePolygonal(1000, 10000, 2)
  hexagonals = GeneratePolygonal(1000, 10000, 3)
  heptagonals = GeneratePolygonal(1000, 10000, 4)
  octagonals = GeneratePolygonal(1000, 10000, 5)

  
  
