from mainTwo import getSingleMapping

def test_case1():
    sourceRange = [50, 10]
    mapping = [{
        "destination": 52, 
        "source": 49, 
        "range": 20}]
    output = [[53, 10]]
    assert getSingleMapping(sourceRange, mapping) == output, "test"

def test_case2():
    sourceRange = [50, 10]
    mapping = [{
        "destination": 57, 
        "source": 55, 
        "range": 20}]
    output = [[57, 5]]
    assert getSingleMapping(sourceRange, mapping) == output, "test"


def test_case3():
    sourceRange = [50, 10]
    mapping = [{
        "destination": 57, 
        "source": 55, 
        "range": 20}]
    output = [[57, 5]]
    assert getSingleMapping(sourceRange, mapping) == output, "test "