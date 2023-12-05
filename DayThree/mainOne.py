from itertools import filterfalse
import re

with open('c:/code/advent-of-code/DayThree/input.txt') as inputFile:
    lines = inputFile.readlines()
    allSymbols = ''.join(''.join(''.join(filterfalse(str.isalnum, ''.join(lines))).split('.')).split('\n'))
    symbols = []
    for s in allSymbols:
        if s in symbols:
            pass
        else:
            symbols.append(s)
    sum = 0
    for i, currentLine in enumerate(lines):
        previousLine = None if i == 0 else lines[i - 1]
        nextLine = None if (i+1) == len(lines) else lines[i + 1]

        for number in re.finditer(r'\d+', currentLine):
            start = 0 if number.start() == 0 else number.start() - 1
            end = number.end() + 1
            if (currentLine[start] in symbols) or (currentLine[number.end()] in symbols):
                sum += int(number.group())
                continue
            if previousLine != None:
                numberSpan = previousLine[start:end]
                for character in numberSpan:
                    if character in symbols:
                        sum += int(number.group())
                        continue
            if nextLine != None:
                numberSpan = nextLine[start:end]
                for character in numberSpan:
                    if character in symbols:
                        sum += int(number.group())
                        continue
    print(sum)
    inputFile.close()

