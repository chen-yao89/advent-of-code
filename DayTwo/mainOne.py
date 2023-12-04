import re

red = 12
green = 13
blue = 14

def isPossible(sets):
    result = True
    for set in sets:
        colors = set.split(", ")
        for colorSet in colors:
            colorCount = colorSet.split(" ")
            if colorCount[1] == "red" and int(colorCount[0]) > red:
                result = False
            elif colorCount[1] == "green" and int(colorCount[0]) > green:
                result = False
            elif colorCount[1] == "blue" and int(colorCount[0]) > blue:
                result = False
    return result

with open('c:/code/advent-of-code/DayTwo/input.txt') as inputFile:
    lines = inputFile.readlines()
    count = 0
    for line in lines:
        sets = re.sub(r'^.*?: ', '', line).strip().split("; ")
        id = line.split(": ")[0].split("Game ")[1]
        if (isPossible(sets) != False):
            count += int(id)
    print(count)
    inputFile.close()