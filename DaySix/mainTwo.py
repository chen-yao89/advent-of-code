import os
import re

__location__ = os.path.realpath(
		os.path.join(os.getcwd(), os.path.dirname(__file__)))

def getInfo(lines):
	time = "".join(re.findall(r'\d+',lines[0]))
	distance = "".join(re.findall(r'\d+',lines[1]))
	return [int(time), int(distance)]

def checkWaysToBeatTheRecord(record):
	recordTime = record[0]
	recordDistance = record[1]
	minimum = 0
	maximum = 0
	for hold in range(recordTime):
		if hold == 0 or hold == recordTime:
			continue
		timeLeft = recordTime - hold
		minimumTimeRequired = recordDistance / hold
		if minimumTimeRequired < timeLeft:
			minimum = hold
			break
	for hold in reversed(range(recordTime)):
		if hold == 0 or hold == recordTime:
			continue
		timeLeft = recordTime - hold
		minimumTimeRequired = recordDistance / hold
		if minimumTimeRequired < timeLeft:
			maximum = hold
			break
	return maximum - minimum + 1

with open(os.path.join(__location__, 'input.txt')) as inputFile:
		lines = inputFile.readlines()
		inputFile.close()
		record = getInfo(lines)
		
		totalCount = checkWaysToBeatTheRecord(record)

		print(totalCount)
