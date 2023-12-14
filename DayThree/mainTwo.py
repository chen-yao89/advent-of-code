from functools import reduce
import re

with open('c:/code/advent-of-code/DayThree/input.txt') as inputFile:
    lines = inputFile.readlines()
    symbol = "*"
    sum = 0
    for i, currentLine in enumerate(lines):
        previousLine = None if i == 0 else lines[i - 1]
        nextLine = None if (i+1) == len(lines) else lines[i + 1]
        stars = [(si, star) for si, star in enumerate(currentLine) if (star == symbol)]

        crtNumbers = [number for number in re.finditer(r'\d+', currentLine)]
        otherNumbers = ([] if previousLine == None else [number for number in re.finditer(r'\d+', previousLine)]) + ([] if nextLine == None else [number for number in re.finditer(r'\d+', nextLine)])

        for star in stars:
            numbers = []
            for number in crtNumbers:
                if number.end() == star[0] or number.start()-1 == star[0]:
                    numbers.append(int(number.group()))
            for number in otherNumbers:
                if number.start() <= star[0] <= number.end():
                    numbers.append(int(number.group()))
                elif number.start() != 0:
                    if number.start()-1 == star[0]:
                        numbers.append(int(number.group()))      
                elif number.end() != len(currentLine):
                    if number.end()+1 == star[0]:
                        numbers.append(int(number.group()))
            if len(numbers) > 1:
                print(numbers)
                sum += reduce((lambda x, y: x * y), numbers)
    print(sum)
    inputFile.close()
