import math
import function_annotation


"""
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
"""


def test_ceil():
    assert function_annotation.ceil(6.01) == 7

def test_floor():
    assert function_annotation.floor(6.01) == 6

def test_avg():
    assert function_annotation.avg(4.0, 8.0) == 6

def test_voting_age():
    assert function_annotation.voting_age(18) == True

def test_message():
    assert function_annotation.message("frank") == "Good morning frank"
