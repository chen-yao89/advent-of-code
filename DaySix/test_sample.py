from mainTwo import getMappedDestination, getDestination

def test_allSeedsAreMapped():
    sourceRange = [[50, 10]]
    mapping = {
        "destination": 52, 
        "source": 49, 
        "range": 20}
    output = {
        "destination": [[53, 10]],
        "unmappedSource": []
		}
    assert getMappedDestination(sourceRange, mapping) == output, "all seeds from source are mapped to destination"

def test_partialSeedsAreMapped_endOverlap():
    sourceRange = [[50, 10]]
    mapping = {
        "destination": 57, 
        "source": 55, 
        "range": 20}
    output = {
        "destination": [[57, 5]],
        "unmappedSource": [[50, 5]]
		}
    assert getMappedDestination(sourceRange, mapping) == output, "part of the seeds from source are mapped to destination"

def test_partialSeedsAreMapped_startOverlap():
    sourceRange = [[50, 10]]
    mapping = {
        "destination": 37, 
        "source": 35, 
        "range": 20}
    output = {
        "destination": [[52, 5]],
        "unmappedSource": [[55, 5]]
		}
    assert getMappedDestination(sourceRange, mapping) == output, "part of the seeds from source are mapped to destination"

def test_partialSeedsAreMapped_midOverlap():
    sourceRange = [[50, 10]]
    mapping = {
        "destination": 54,
        "source": 52,
        "range": 5
		}
    output = {
        "destination": [[54, 5]],
        "unmappedSource": [[50, 2], [57, 3]]
		}
    assert getMappedDestination(sourceRange, mapping) == output, "part of the seeds from source are mapped to destination"

def test_noSeedsAreMapped():
    sourceRange = [[40, 10]]
    mapping = {
        "destination": 57, 
        "source": 55, 
        "range": 20}
    output = {
        "destination": [],
        "unmappedSource": [[40, 10]]
		}
    assert getMappedDestination(sourceRange, mapping) == output, "none of the seeds from source are mapped to destination"
    
def test_unMappedSourceReturnedCorrectly():
    sourceRange = [[40, 10], [50, 10], [60, 10]]
    mapping = [
        {
            "destination": 47,
            "source": 45,
            "range": 5
				},
        {
            "destination": 52,
            "source": 50,
            "range": 8
				},
        {
            "destination": 62,
            "source": 60,
            "range": 12
				},
		]
    output = [[47, 5], [52, 8], [62, 10], [40, 5], [58, 2]]
    assert getDestination(sourceRange, mapping) == output, "returns correct mapped destination"