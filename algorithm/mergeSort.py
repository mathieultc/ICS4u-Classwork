from typing import List

def mergeSort(numbers: List[int]) -> int:
    if len(numbers) == 1:
        return numbers

    midpoint = len(numbers)//2

    #two recursive steps
    #mergesort left
    left_side = mergeSort(numbers[:midpoint])

    #mergesort right
    right_side = mergeSort(numbers[midpoint:])

    #merge the two together
    sorted_list = []

    #loop through the list with two markers
    left_marker = 0
    right_marker = 0
    while left_marker < len(left_side) and right_marker < len(right_side):
        if left_side[left_marker] < right_side[right_marker]:
            sorted_list.append(left_side[left_marker])
            left_marker += 1

        else:
            sorted_list.append(right_side[right_marker])
            right_marker += 1
        
    
    #if marker 1 is smaller, append that first, move marker over
    #if marker 2 is smaller, append that, move marker over

    
    #if one marker goes off the list, add the rest of the other list
    while right_marker < len(right_side):
        sorted_list.append(right_side[right_marker])
        right_marker += 1

    while left_marker < len(left_side):
        sorted_list.append(left_side[left_marker])
        left_marker += 1

    return sorted_list


numbers = [4, 2, 5, 2, 3, 1]
print(mergeSort(numbers))


