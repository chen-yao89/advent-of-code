from mainTwo import getMappedDestination

def allSeedsAreMapped():
    sourceRange = [50, 10]
    mapping = [{
        "destination": 52, 
        "source": 49, 
        "range": 20}]
    output = [[53, 10]]
    assert getMappedDestination(sourceRange, mapping) == output, "all seeds from source are mapped to destination"

def partialSeedsAreMapped():
    sourceRange = [50, 10]
    mapping = [{
        "destination": 57, 
        "source": 55, 
        "range": 20}]
    output = [[57, 5]]
    assert getMappedDestination(sourceRange, mapping) == output, "part of the seeds from source are mapped to destination"


def noSeedsAreMapped():
    sourceRange = [40, 10]
    mapping = [{
        "destination": 57, 
        "source": 55, 
        "range": 20}]
    output = []
    assert getMappedDestination(sourceRange, mapping) == output, "none of the seeds from source are mapped to destination "