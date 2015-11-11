"""
Unit tests for the SimulatedInvestment class.
Performs sanity checks of size and range for the attributes in the class that are arrays.

Author: kk3175
Date: 11/11/2015
Class: DSGA1007, Assignment 8
"""

import numpy as np
from unittest import TestCase
from SimulatedInvestment import SimulatedInvestment

class SimulatedInvestmentTest(TestCase):
	position = 10
	num_trials = 10
	position_value = 1000 / position

	# test size of outcomes array
	def test_outcomes_attribute_size(self):
		testInvestment = SimulatedInvestment(self.position, self.num_trials)
	
		testResult = testInvestment.outcomes.shape
		expectedResult = (self.num_trials, self.position)
		self.assertEqual(testResult, expectedResult)

	# test range of outcomes array
	def test_outcomes_attribute_range(self):
		testInvestment = SimulatedInvestment(self.position, self.num_trials)
		
		for element in np.nditer(testInvestment.outcomes):
			self.assertTrue(element == 0 or element == ((self.position_value)*2))

	# test size of cumu_ret array
	def test_cumu_ret_attribute_size(self):
		testInvestment = SimulatedInvestment(self.position, self.num_trials)
	
		testResult = testInvestment.cumu_ret.shape
		expectedResult = (self.num_trials, 1)
		self.assertEqual(testResult, expectedResult)

	# test range of cumu_ret array
	def test_cumu_ret_attribute_range(self):
		testInvestment = SimulatedInvestment(self.position, self.num_trials)
		
		for element in np.nditer(testInvestment.cumu_ret):
			self.assertTrue(element >= 0 and element <= (self.position_value * 2 * self.position))

	# test size of daily_ret array
	def test_daily_ret_attribute_size(self):
		testInvestment = SimulatedInvestment(self.position, self.num_trials)
	
		testResult = testInvestment.daily_ret.shape
		expectedResult = (self.num_trials, 1)
		self.assertEqual(testResult, expectedResult)

	# test range of daily_ret array
	def test_daily_ret_attribute_range(self):
		testInvestment = SimulatedInvestment(self.position, self.num_trials)
		
		for element in np.nditer(testInvestment.daily_ret):
			self.assertTrue(element >= -1 and element <= 1)
