from typing import List

def linearSearch(numbers: List[int], target: int) -> int:
    for i, num in enumerate(numbers):
        if num == target:
            return i

    return -1


numbers = [1, 2, 3, 4, 5]

print(linearSearch(numbers, 5))