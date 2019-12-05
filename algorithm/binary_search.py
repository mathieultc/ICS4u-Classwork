from typing import List

def binary_search(target: int, numbers: int) -> int:
    start = 0
    end = len(numbers) - 1
    
    while end >= start:
        mid = (start + end)//2

        if numbers[mid] == target:
            return mid

        elif target > numbers[mid]:
            start = mid + 1

        elif target < numbers[mid]:
            end = mid - 1

        else:
            return -1

#recursion
def binarySearch(numbers: List[int], start: int, end: int, target: int) -> int:
    if start <= end: #base case
        mid = (start + end)//2
        if numbers[mid] == target:
            return mid

        elif numbers[mid] < target:
            return binarySearch(numbers, mid + 1, end, target)

        elif numbers[mid] > target:
            return binarySearch(numbers, start, mid - 1, target)

    return -1


numbers = [1, 2, 3, 4, 5]
print(binarySearch(numbers, numbers[0], len(numbers)-1, 4))
