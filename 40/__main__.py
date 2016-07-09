#!/usr/bin/python
# -*- coding: utf8 -*-

import psyco
psyco.full()

# FUNCTIONS

if __name__ == "__main__":
	fr = "0123456789"
	i = 10
	
	while len(fr) < 1000001:
		fr += str(i)
		i+=1

	result = int(fr[1]) * int(fr[10]) * int(fr[100]) * int(fr[1000]) * int(fr[10000]) * int(fr[100000]) * int(fr[1000000])
	print result
