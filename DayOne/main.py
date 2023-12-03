with open('c:/code/advent-of-code/DayOne/input.txt') as inputFile:
    lines = inputFile.readlines()
    numbers = []
    for line in lines:
        line.strip()
        lineWithNumberOnly="".join(n for n in line if n.isdecimal())
        if(len(lineWithNumberOnly) > 1):
            number=lineWithNumberOnly[::len(lineWithNumberOnly)-1]
            numbers.append(int(number))
        else:
            number="".join([lineWithNumberOnly,lineWithNumberOnly])
            numbers.append(int(number))
    print(sum(numbers))
    inputFile.close()