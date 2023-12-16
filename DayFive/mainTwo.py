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
						seeds.append([number, ranges[i+1]])
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

def getMappedDestination(sourceRange, map):
		destinationRange = []
		unMappedSource = []
		for source in sourceRange:
			start = map["source"]
			end = map["source"] + map["range"] - 1
			sourceStart = source[0]
			sourceEnd = source[0] + source[1] - 1
			if sourceStart > end:
					unMappedSource.append(source)
			elif sourceEnd < start:
					unMappedSource.append(source)
			elif sourceEnd <= end:
					if sourceStart >= start:
							destinationRange.append([map["destination"] + (sourceStart - start), source[1]])
					elif sourceStart < start:
							destinationRange.append([map["destination"], sourceEnd - start + 1])
							unMappedSource.append([sourceStart, start - sourceStart])
			elif sourceEnd > end:
					if sourceStart < start:
							destinationRange.append([map["destination"], map["range"]])
							unMappedSource.append([sourceStart, start - sourceStart])
							unMappedSource.append([end + 1, sourceEnd - end])
					elif sourceStart >= start:
							destinationRange.append([map["destination"] + (sourceStart - start), end - sourceStart + 1])
							unMappedSource.append([end + 1, sourceEnd - end])
		return {
				"destination": destinationRange,
				"unmappedSource": unMappedSource
		}

def getDestinationPerSource(source, mapping):
		destinationRange = []
		unMappedSource = []
		sourceRange = [source]
		for i, map in enumerate(mapping):
				result = getMappedDestination(sourceRange, map)
				destinationRange += result["destination"]
				if (len(sourceRange) != 0):
					sourceRange.pop(0)
				if i < (len(mapping) - 1):
					for unmapped in result["unmappedSource"]:
						if unmapped in sourceRange:
							continue
						else:
							sourceRange.append(unmapped)
				else:
					unMappedSource += result["unmappedSource"]
		return {
				"destination": destinationRange,
				"unmappedSource": unMappedSource
		}

def getDestination(sourceRange, mapping):
		destinationRange = []
		unmappedRange = []
		for source in sourceRange:
				mappingResult = getDestinationPerSource(source, mapping)
				destinationRange += mappingResult["destination"]
				unmappedRange += mappingResult["unmappedSource"]
		destinationRange += unmappedRange
		return destinationRange

with open(os.path.join(__location__, 'input.txt')) as inputFile:
		lines = inputFile.readlines()

		seeds = getSeeds(lines)
		soilMapping = getMappingRange(lines, seedToSoil)
		fertilizerMapping = getMappingRange(lines, soilToFertilizer)
		waterMapping = getMappingRange(lines, fertilizerToWater)
		lightMapping = getMappingRange(lines, waterToLight)
		temperatureMapping = getMappingRange(lines, lightToTemperature)
		humidityMapping = getMappingRange(lines, temperatureToHumidity)
		locationMapping = getMappingRange(lines, humidityToLocation)

		locations = []
		soil = getDestination(seeds, soilMapping)
		fertilizer = getDestination(soil, fertilizerMapping)
		water = getDestination(fertilizer, waterMapping)
		light = getDestination(water, lightMapping)
		temperature = getDestination(light, temperatureMapping)
		humidity = getDestination(temperature, humidityMapping)
		location = getDestination(humidity, locationMapping)
		for x in location:
			locations.append(x[0])

		print(min(locations))
		inputFile.close()