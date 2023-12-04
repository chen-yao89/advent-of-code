import re

def setsPower(sets):
    red = 0
    blue = 0
    green = 0
    for set in sets:
        colors = set.split(", ")
        for colorSet in colors:
            colorCount = colorSet.split(" ")
            if colorCount[1] == "red" and int(colorCount[0]) > red:
                red = int(colorCount[0])
            elif colorCount[1] == "green" and int(colorCount[0]) > green:
                green = int(colorCount[0])
            elif colorCount[1] == "blue" and int(colorCount[0]) > blue:
                blue = int(colorCount[0])
    return red * blue * green

with open('c:/code/advent-of-code/DayTwo/input.txt') as inputFile:
    lines = inputFile.readlines()
    sum = 0
    for line in lines:
        sets = re.sub(r'^.*?: ', '', line).strip().split("; ")
        sum += setsPower(sets)
    print(sum)
    inputFile.close()