#!/usr/bin/python
# -*- coding: utf8 -*-

import psyco
psyco.full()

#############################
# LEGEND                    #
# 1: Pair                   #
# 2: Two pairs              #
# 3: Tris (three of a kind) #
# 4: Straight               #
# 5: Flush                  #
# 6: Full House             #
# 7: Poker (four of a kind) #
# 8: Straight flush         #
# 9: Royal flush            #
#############################

class Player:
	plHand = []
	
	##################################################################
	# This variable helps recognize what cards originated the score: #
	# for example if you score a pair of 5, type will be equal to 5. #
	# It's useful when both players have the same combination.       #
	##################################################################
	type = 0
	
	# See legend above
	result = 0
	
	Combs = { "Royal flush" : False, "Straight flush" : False, "Poker" : False, "Full" : False, "Flush" : False, "Straight" : False, "Tris" : False, "Two pairs" : False, "Pair" : False }
	
	# This list is necessary because when you iterate through a dictionary,
	# elements are not presented in the same order as you declared them (!)
	Scores = ["Royal flush", "Straight flush", "Poker", "Full", "Flush", "Straight", "Tris", "Two pairs", "Pair"]
	
	# It works like a constructor
	def SetNewHand(self, newHand):
		self.plHand = newHand
		for i in self.Combs:
			self.Combs[i] = False
	
	def GetCurHand(self):
		return self.plHand
	
	def DecideResult(self):
		nav = 9
		
		for i in self.Scores:
			if self.Combs[i] == True:
				self.result = nav
				break
			nav -= 1
				
	def GetResult(self):
		return self.result
	
	def GetType(self):
		return self.type
	
	def GetNumsFromHand(self):
		nums = []
		
		for i in range(5):
			if self.plHand[i][0] == 'T':
				value = 10
			elif self.plHand[i][0] == 'J':
				value = 11
			elif self.plHand[i][0] == 'Q':
				value = 12
			elif self.plHand[i][0] == 'K':
				value = 13
			elif self.plHand[i][0] == 'A':
				value = 14
			else:
				value = int(self.plHand[i][0])
			nums.append(value)
			
		return nums
	
	def GetSuitsFromHand(self):
		suits = []
		
		for i in range(5):
			suits.append(self.plHand[i][1])
		return suits
	
	def IsFlush(self, hand):
		
		example = hand[0]
	
		for element in hand:
			if element != example:
				return False

		return True
		
	def CountOccurrences(self, sCard, plNums):
		
		count = 0
	
		for e in plNums:
			if e == sCard:
				count += 1
	
		return count
	
	def IsStraight(self, hand):
		
		hand.sort()
		
		for i in range(1, 5):
			if int(hand[i]) != int(hand[i-1]) + 1:
				return False
		
		return True
	
	def IsRoyalStraight(self, hand):
		hand.sort()
		rights = [10, 11, 12, 13, 14]
		
		return (hand == rights)

	def SolveHand(self):
		plNums = self.GetNumsFromHand()
		plSuits = self.GetSuitsFromHand()
		card = 0
		
		plNums.sort()
		
		while card < 5:
			occs = self.CountOccurrences(plNums[card], plNums)
			if occs == 2:
				if self.Combs["Pair"] == True:
					self.Combs["Two pairs"] = True
					self.type = plNums[card] # The second pair is surely higher (because of sorting) so it overwrites the first one
					break
				else:
					self.Combs["Pair"] = True
					self.type = plNums[card]
					card += 2 # Avoids looking twice for the same number
					continue
			
			elif occs == 3:
				self.Combs["Tris"] = True
				self.type = plNums[card]
				card += 3
			
			elif occs == 4:
				self.Combs["Poker"] = True
				self.type = plNums[card]
				break
			
			card += 1	
		
		self.Combs["Full"] = self.Combs["Pair"] and self.Combs["Tris"]
		self.Combs["Flush"] = self.IsFlush(plSuits)
		self.Combs["Straight"] = self.IsStraight(plNums)
		self.Combs["Straight flush"] = self.Combs["Flush"] and self.Combs["Straight"]
		self.Combs["Royal flush"] = self.IsRoyalStraight(plNums) and self.Combs["Flush"]
		self.DecideResult()
