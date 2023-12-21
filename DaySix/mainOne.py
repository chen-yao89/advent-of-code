import os
import re

__location__ = os.path.realpath(
		os.path.join(os.getcwd(), os.path.dirname(__file__)))

def getInfo(lines):
	time = re.findall(r'\d+',lines[0])
	distance = re.findall(r'\d+',lines[1])
	data = []
	for i, ti in enumerate(time):
		data.append([int(ti), int(distance[i])])
	return data

def checkWaysToBeatTheRecord(record):
	recordTime = record[0]
	recordDistance = record[1]
	count = 0
	for hold in range(recordTime):
		if hold == 0 or hold == recordTime:
			continue
		timeLeft = recordTime - hold
		minimumTimeRequired = recordDistance / hold
		if minimumTimeRequired < timeLeft:
			count += 1
	return count

with open(os.path.join(__location__, 'input.txt')) as inputFile:
		lines = inputFile.readlines()
		inputFile.close()
		records = getInfo(lines)
		
		totalCount = 1
		for record in records:
			totalCount *= checkWaysToBeatTheRecord(record)

		print(totalCount)
