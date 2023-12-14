import os
import re

__location__ = os.path.realpath(
		os.path.join(os.getcwd(), os.path.dirname(__file__)))

def isWinningNumber(winningNumbers, myNumbers):
		result = 0
		for number in myNumbers:
				if number in winningNumbers:
						result += 1
		return result

def getCardIds(wonCards, Id):
		result = []
		for i in range(wonCards):
			result.append(int(Id) + i + 1)
		return result

with open(os.path.join(__location__, 'input.txt')) as inputFile:
		lines = inputFile.readlines()
		count = 0
		myCards = []
		for line in lines:
				id = int(line.split(": ")[0].split("Card ")[1])
				numbers = line.split(": ")[1].split(" | ")
				winningNumbers = re.findall(r'\d+', numbers[0])
				myNumbers = re.findall(r'\d+', numbers[1])
				wonCards = isWinningNumber(winningNumbers, myNumbers)
				myCards.append({
					"id": id,
					"cardIds": getCardIds(wonCards, id),
					"count": 1
				})
		for card in myCards:
				if len(card["cardIds"]) == 0:
					continue
				cardIds = card["cardIds"]
				if len(card["cardIds"]) > 0:
					for wonCard in cardIds:
						myCards[wonCard-1]["count"] += card["count"]
		for card in myCards:
			count += card["count"]
		print(count)
		inputFile.close()