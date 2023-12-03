import re

def digit_name_convert(name):
    if name == "one":
        return 1
    if name == "two":
        return 2
    if name == "three":
        return 3
    if name == "four":
        return 4
    if name == "five":
        return 5
    if name == "six":
        return 6
    if name == "seven":
        return 7
    if name == "eight":
        return 8
    if name == "nine":
        return 9

def converNumber(numberStr):
    num = []
    for n in numberStr:
        newN = digit_name_convert(n)
        if newN == None:
            num.append(n)
        else:
            num.append(str(newN))
    return "".join(num)

with open('c:/code/advent-of-code/DayOne/input.txt') as inputFile:
    lines = inputFile.readlines()
    numbers = []
    
    for line in lines:
        line.strip()
        lineWithNumberOrWord=re.findall(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))",line)
        if(len(lineWithNumberOrWord) > 1):
            number=converNumber(lineWithNumberOrWord[::len(lineWithNumberOrWord)-1])
            numbers.append(int(number))
        else:
            number=converNumber([lineWithNumberOrWord[0], lineWithNumberOrWord[0]])
            numbers.append(int(number))
    print(sum(numbers))
    inputFile.close()
