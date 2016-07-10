#!/usr/bin/python
# -*- coding: utf8 -*-

from player import *

# FUNCTIONS

####################################################
# If, for example, both players have a pair of 8s, #
# it finds out who has the highest card at all     #
####################################################
def CompareHighest(pl1, pl2):
	pNums1 = pl1.GetNumsFromHand()
	pNums2 = pl2.GetNumsFromHand()
	
	pNums1.sort()
	pNums2.sort()
	
	for i in range(4, 0, -1):
		if pNums1[i] > pNums2[i]:
			return 1
		elif pNums1[i] < pNums2[i]:
			return 2
	
	# I didn't include any other possibility (no winner at all)
	# because the Euler problem told me every hand has a clear winner
	
if __name__ == "__main__":
	fstHand = []
	secHand = []
	fp = open ("poker.txt", "r")
	c = 0
	win1 = 0
	win2 = 0
	
	print "+-----------------------------------+"
	print "| How many hands does Player 1 win? |"
	print "+-----------------------------------+"
	
	for line in fp:
		for sCard in line.split():
			# First 5 cards are for the first hand
			if c < 5:
				fstHand.append(sCard)
			else:
				secHand.append(sCard)
			c += 1
		c = 0
	
		fstPlayer = Player()
		fstPlayer.SetNewHand(fstHand)
		fstPlayer.SolveHand()
	
		secPlayer = Player()
		secPlayer.SetNewHand(secHand)
		secPlayer.SolveHand()
	
		# Who has the most important combination?
		if fstPlayer.GetResult() > secPlayer.GetResult():
			win1 += 1
		elif fstPlayer.GetResult() < secPlayer.GetResult():
			win2 += 1
		
		# Okay...who has the most important cards in his combination?	
		else:
			type1 = fstPlayer.GetType()
			type2 = secPlayer.GetType()
			if type1 != 0 and type1 > type2:
				win1 += 1
			elif type1 != 0 and type1 < type2:
				win2 += 1
			
			# Last hope
			else:
				if CompareHighest(fstPlayer, secPlayer) == 1:
					win1 += 1
				else:
					win2 += 1
					
		fstHand = []
		secHand = []

	print win1
	fp.close()
