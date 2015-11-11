"""
Error handling class

Author: kk3175
Date: 11/11/2015
Class: DSGA1007, Assignment 8
"""

class InvestmentEntryError:
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)
