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


result = binary_search(3, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(result)

