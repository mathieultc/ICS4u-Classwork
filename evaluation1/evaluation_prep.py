from typing import List, Dict


# exmaple 1
def add(num1: int, num2: int) -> int:
    """A function that returns the sum of two integers
    Args:
        num1: A number
        num2: another number
    Returns:
        sum of two integers
    """
    return num1 + num2


#example 2
def sum_list(numbers: List[int]) -> int:
    """A function that returns the sum of numbers in a list
    Args:
        numbers: A list of numbers
    Returns:
        The sum of the numbers from the list

    """

    return sum(numbers)


#example 3
def word_count(words: List[str]) -> Dict:
    """ A function that takes a list of words and returns a dictionary where the key
    is the word and the value is the number of times the word appeaers
    Args:
        words: A list of words
    Returns:
        A dictionary where the key is the word and the value is the number of times it appears in the list
    """
    
    word_dict = dict()
    
    for word in words:
        count = words.count(word)
        word_dict[word] = count

    return word_dict



