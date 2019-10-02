import math



#test sum(numbers: List[float]) -> float


def test_sum():
    some_list = [1, 2, 3]
    assert sum(some_list) == 6
    assert sum([]) == 0
    assert sum([5, 5, 5]) == 15

# test math.ceil(float) -> int
def test_ceil(): 
    assert math.ceil(6.00001) == 7
    assert math.ceil(6.0) == 6

# test math.floor(float) -> int
def test_floor():
    assert math.floor(-5.95) == -6
    
# test f strings
# test .format()