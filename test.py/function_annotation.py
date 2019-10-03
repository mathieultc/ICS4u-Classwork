from typing import List
import math
# Write function headers and docstring for the following:

#sum
def sum(numbers: List[float]) -> float:

     """
     Args:
         param1: A list of float
     Returns:
          The sum of the list of numbers
     """
     return sum(numbers)

# math.ceil
def ceil(number: float) -> int:

     """ a function that rounds up a float

     Args:
          param1: a float
     Returns:
             Returns an integer from the float
     """
     return math.ceil(number)

# math.floor
def floor(number: float) -> int:
     """ a function that returns the closest value more or less to the given numeric value
     Args:
            param1: a float
     Returns:
            closest integer to the given value
             
     """
     return math.floor(number)

# function that takes a name and outputs a message
def message(name: str) -> str:
     """ a function that takes a name and outputs a message

     Args:
          param1: Someone's name
     Returns:
             A personalized message including the person's name
     """
     message = ("Good morning {0}".format(name))

     return message
# Function that takes two floats and finds their average
def avg(float1: float, float2: float) -> float:
     """A function that takes two floats and finds their average

     Args:
         param1: A number
         param2: Another number
     Returns:
            Average of two decimal numbers
     """
     return (float1+float2)/2
# Function that takes an age and returns True if they are of voting age
def voting_age(age: int) -> bool:
     """A function that determines whether someone is eligible to vote based on their age

     Args:
         param1; Age
     Returns:
            True if they can vote, False otherwise
     """

     if age >= 18:
          return True
     else:
          return False




