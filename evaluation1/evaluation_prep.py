from typing import List

# exmaple 1
def add(num1:int ,num2:int) -> int:
    """A function that returns the sum of two integers
    Args:
        param1: A number
        param2: another number
    Returns:
        sum of two integers
    """
    return num1 + num2


#example 2
def sum_list(numbers: List[float]) -> float:
    """A function that returns the sum of numbers in a list
    Args:
        param1: A list of numbers
    Returns:
        The sum of the numbers from the list

    """

    return sum(numbers)

