from typing import List

def bubbleSort(numbers: List) -> List:
    n = len(numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

    return numbers


array = [1, 3, 5, 4, 2]
print(bubbleSort(array))