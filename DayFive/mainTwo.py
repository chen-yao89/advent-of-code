import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

seedToSoil = "seed-to-soil"
soilToFertilizer = "soil-to-fertilizer"
fertilizerToWater = "fertilizer-to-water"
waterToLight = "water-to-light"
lightToTemperature = "light-to-temperature"
temperatureToHumidity = "temperature-to-humidity"
humidityToLocation = "humidity-to-location"

def getSeeds(lines):
    seeds = []
    ranges = []
    for line in lines:
        if line.startswith("seeds"):
            ranges = [int(i) for i in line.strip().split(": ")[1].split(" ")]
    for i, number in enumerate(ranges):
        if (i % 2) == 0:
            seeds.append([number, [ranges[i+1]]])
    return seeds
        
def getMappingRange(lines, category):
    result = []
    rawResult = []
    startLine = 0
    for i, line in enumerate(lines):
        if line.startswith(category):
            startLine += i + 1
    for line in lines[startLine:len(lines)]:
        if line.startswith("\n"):
            break
        else:
            rawResult.append([int(i) for i in line.strip().split(" ")])
    for r in rawResult:
        result.append({
            "destination": r[0],
            "source": r[1],
            "range": r[2]
        })
    return result

def getMappedDestination(source, mapping):
    destinationRange = []
    for map in mapping:
        start = map["source"]
        end = map["source"] + map["range"] - 1
        sourceStart = source[0]
        sourceEnd = source[0] + source[1] - 1
        if sourceStart > end:
            continue
        if sourceEnd < start:
            continue
        if sourceEnd <= end:
            if sourceStart >= start:
                destinationRange.append([map["destination"] + (sourceStart - start), source[1]])
            if sourceStart < start:
                destinationRange.append([map["destination"], sourceEnd - start + 1])
    return destinationRange

def getDestination(sourceRange, mapping):
    destinationRange = []
    for source in sourceRange:
        unMappedSource = source
        getSingleMapping(source, mapping)
        destinationRange += unMappedSource
    return destinationRange

# with open(os.path.join(__location__, 'input.txt')) as inputFile:
#     lines = inputFile.readlines()

#     seeds = getSeeds(lines)
#     soilMapping = getMappingRange(lines, seedToSoil)
#     fertilizerMapping = getMappingRange(lines, soilToFertilizer)
#     waterMapping = getMappingRange(lines, fertilizerToWater)
#     lightMapping = getMappingRange(lines, waterToLight)
#     temperatureMapping = getMappingRange(lines, lightToTemperature)
#     humidityMapping = getMappingRange(lines, temperatureToHumidity)
#     locationMapping = getMappingRange(lines, humidityToLocation)

#     locations = []
#     for seed in seeds:
#         soil = getDestination(seed, soilMapping)
#         fertilizer = getDestination(soil, fertilizerMapping)
#         water = getDestination(fertilizer, waterMapping)
#         light = getDestination(water, lightMapping)
#         temperature = getDestination(light, temperatureMapping)
#         humidity = getDestination(temperature, humidityMapping)
#         location = getDestination(humidity, locationMapping)
#         locations.append(location)

#     print(min(locations))
#     inputFile.close()