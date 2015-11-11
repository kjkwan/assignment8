"""
Main program for running the investment simulator. Prompts the user for their desired positions and
number of trials.

Author: kk3175
Date: 11/11/2015
Class: DSGA1007, Assignment 8
"""


import matplotlib.pyplot as plt
import numpy as np
from errorHandling import InvestmentEntryError
from SimulatedInvestment import SimulatedInvestment


# Set the name of the output file for saving statistics results
outputFile = 'results.txt'

# Set the valid position denominations	
validDenominations = [1, 10, 100, 1000]


def printWelcome():
	print("This program simulates your $1000 investment, which you can break up into 1, 10, 100, or 1000 positions.")
	print("Find out how much you could make on your investment on the first day.\n")

def printInstructions():
	print("You will be prompted for a list of the number of positions you want to buy in parallel.")	
	print("An example of an acceptable entry of positions: 10, 100, 1")
	print("Please note that you cannot enter duplicate positions.\n")
	print("You will also be prompted for the number of trials you want to repeat the investment simulation.")
	print("The number of trials must be greater than zero.\n")

def printStatusUpdate():
	print("\nAll of your inputs are valid. The positions will be statistically analyzed now.")
	print("The results will be saved in your current directory.\n")
		

# Asks the user for their positions. If the positions are valid, a list of positions (as integers) is returned.
# If duplicate positions were entered or the positions are invalid, errors are raised.
def handleUserPositionsInput():
	userPositionsInput = raw_input("List of positions? ")
	
	# Converts the string of user position input into a list of positions inputs.
	intermediateInput = userPositionsInput.split(',')
	
	# If there are any duplicate position inputs, an error is raised.
	if hasDuplicates(intermediateInput):
		raise InvestmentEntryError('You entered duplicate positions.\n')

	# If the positions entered are valid, a positions list of integers is returned. Otherwise, an error is raised.
	if areValidPositions(intermediateInput):
		return makePositionsList(intermediateInput)
	else:
		raise InvestmentEntryError('You entered an invalid position denomination.\n')

# Helper function that checks if the user entered any duplicate positions.
# Credit to Denis Otkidach via http://stackoverflow.com/questions/1541797/in-python-how-to-check-if-there-are-any-duplicates-in-list
def hasDuplicates(intermediateInput):
	if len(intermediateInput) != len(set(intermediateInput)):
		return True
	else:
		return False
	
# Helper function that checks each position entered by the user.
# If the position is not an integer, an error is raised. 
# If all positions are valid integers and valid position denominations, true is returned.
def areValidPositions(intermediateInput):
	for item in intermediateInput:
		# If the item cannot be cast as an integer, a ValueError exception is thrown.		
		position = int(item)
		
		# If the position is not a valid position denomination, false is returned.
		if not position in validDenominations:
			return False
	return True 

# Converts the list of positions from a list of strings to a list of integers. Returns the list of integers.
def makePositionsList(intermediateInput):
	positions = []

	for item in intermediateInput:
		position = int(item)
		positions.append(position)

	return positions


# Asks the user for the number of trials. If the input is valid, the number of trials is returned.
# If the number of trials is invalid, an error is raised.
def handleUserNumTrialsInput():
	userNumTrialsInput = raw_input("Number of trials? ")
	
	if isValidNumTrialsInput(userNumTrialsInput):
		return int(userNumTrialsInput)
	else:
		raise InvestmentEntryError('You entered an invalid number of trials.\n')

# Helper function that checks the validity of the user's input of the number of trials.
# If the input is not an integer, an error is raised.
# If the input is a valid integer and a valid number of trials, true is returned.
def isValidNumTrialsInput(userNumTrialsInput):
	# If the item cannot be cast as an integer, a ValueError error is raised.		
	num_trials = int(userNumTrialsInput)
	
	# Number of trials must be greater than 0.
	if num_trials > 0:
		return True
	else:
		return False


# Each position is statistically analyzed, with results saved to files in the current directory.
def analyzePositions(positions, num_trials):
	for position in positions:
		# Converts the position into a SimulatedInvestment class object
		investmentPosition = SimulatedInvestment(position, num_trials)
		
		# Save histogram of daily returns for the position
		investmentPosition.saveHistogram()
	
		# Save the expected value of the daily return
		investmentPosition.saveExpectedValue(outputFile)

		# Save the standard deviation of the daily return
		investmentPosition.saveStandardDeviation(outputFile)




def main():
	printWelcome()
	printInstructions()
	
	try:
		positions = handleUserPositionsInput()	
		num_trials = handleUserNumTrialsInput()
		
		printStatusUpdate()
		
		analyzePositions(positions, num_trials)
		
	except InvestmentEntryError as e:
		print 'An Investment Entry error occured: ', e.value
	except SyntaxError:
		print 'Incorrect format. Use this format for entering positions: [1, 10, 100].'
	except KeyboardInterrupt:
		print 'Good bye!'
	except ValueError:
		print 'You entered a non-integer.'

main()
