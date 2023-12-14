import os
import re

__location__ = os.path.realpath(
		os.path.join(os.getcwd(), os.path.dirname(__file__)))

def isWinningNumber(winningNumbers, myNumbers):
		result = 0
		for number in myNumbers:
				if number in winningNumbers:
						result += 1
		return 2 ** (result - 1) if result != 0 else result

with open(os.path.join(__location__, 'input.txt')) as inputFile:
		lines = inputFile.readlines()
		points = 0
		for line in lines:
				numbers = line.split(": ")[1].split(" | ")
				winningNumbers = re.findall(r'\d+', numbers[0])
				myNumbers = re.findall(r'\d+', numbers[1])
				points += isWinningNumber(winningNumbers, myNumbers)
		print(points)
		inputFile.close()