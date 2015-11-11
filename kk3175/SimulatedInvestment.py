"""
Class that takes the number of positions and number of trials to simulate investment outcomes and statistically analyze these outcomes.

Author: kk3175
Date: 11/11/2015
Class: DSGA1007, Assignment 8
"""


import matplotlib.pyplot as plt
import numpy as np

class SimulatedInvestment:
	# Set the probability of the value doubling or being lost
	probabilityValueDoubles = 0.51
	probabilityValueLost = 1 - probabilityValueDoubles
	probabilitiesOfPossibleOutcomes = [probabilityValueDoubles, probabilityValueLost]

	# Attributes of class object
	outcomes = None
	cumu_ret = None
	daily_ret = None
	expectedValue = None
	standardDeviation = None
	
	# Assumes the position and num_trials arguments are valid inputs.
	def __init__(self, position, num_trials):
		self.position = position
		self.num_trials = num_trials
		self.__simulateOutcomes()
		self.__calculateCumulativeReturns()
		self.__calculateDailyReturns()
		self.__calculateExpectedValue()
		self.__calculateStandardDeviation()

	# Creates an array of simulated outcomes by trial and position number.
	def __simulateOutcomes(self):
		# Keeps track of the outcome of each simulation by trial number (rows) and position number (columns)
		self.outcomes = np.zeros((self.num_trials, self.position))
		# Sets a value to represent the monetary value of each position
		position_value = 1000 / self.position

		for trial in range(self.num_trials):
			for positionNum in range(self.position):
				# Per assignment instructions, the position value is either doubled or lost.
				possibleOutcomes = ([(position_value * 2), 0])
				self.outcomes[trial][positionNum] = np.random.choice(possibleOutcomes, p = self.probabilitiesOfPossibleOutcomes)

	# Calculates the cumulative return for each trial based on the array containing the outcomes of 
	# the trials and positions.
	def __calculateCumulativeReturns(self):
		self.cumu_ret = np.zeros((self.num_trials, 1))

		for trial in range(self.num_trials):	
			self.cumu_ret[trial] = self.outcomes[trial].sum()
		
	# Calculates the daily return for each trial based on the array containing the cumulative returns
	# for each trial.
	def __calculateDailyReturns(self):
		self.daily_ret = np.zeros((self.num_trials, 1))

		for trial in range(self.num_trials):	
			self.daily_ret[trial] = (self.cumu_ret[trial]/1000) - 1	

	# Calculates the expected value of the daily return for each position
	def __calculateExpectedValue(self):	
		self.expectedValue = np.mean(self.daily_ret)

	# Calculates the standard deviation of the daily return for each position
	def __calculateStandardDeviation(self):
		self.standardDeviation = np.std(self.daily_ret)
		
		
	# PUBLIC FUNCTIONS
	# Plots a histogram of the daily returns. Saves the histogram to a file (file naming scheme
	# specified in assignment).	
	def saveHistogram(self):
		plt.hist(self.daily_ret, 100, range = [-1, 1], color=['orange'])
		plt.xlim(-1,1)
		plt.suptitle("Daily Returns for %r share(s) and %r trials" %(self.position, self.num_trials))
		plt.xlabel('Daily Returns')
		plt.ylabel('Number of Occurrences')
		partialFileName = str(self.position).zfill(4)
		plt.savefig("histogram_%s_pos.pdf" %partialFileName)
		plt.close()

	# Saves (by appending) the expected values results to the file name specified in the argument.
	def saveExpectedValue(self, outputFile):
		with open(outputFile, 'a') as file:
			file.write("\nDAILY RETURN STATISTICS FOR %s POSITION(S) and %s TRIAL(S): \n" % (self.position, self.num_trials))
			file.write("Expected value of the daily return: %s \n" % self.expectedValue)
		file.closed

	# Saves (by appending) the standard deviation results to the file name specified in the argument.
	def saveStandardDeviation(self, outputFile):
		with open(outputFile, 'a') as file:
			file.write("Standard deviation of the daily return : %s \n" % self.standardDeviation)
		file.closed
