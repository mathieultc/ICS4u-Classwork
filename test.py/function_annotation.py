
import math
# Write function headers and docstring for the following:

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
          param1: a string 
     Returns:
             a message or a string
     """
     message = ("Good morning {0}".format(name))

     return message
# Function that takes two floats and finds their average
def avg(float1: float, float2: float) -> float:
     """A function that takes two floats and finds their average

     Args:
         param1: A float
         param2: A float
     Returns:
            Average of two floats
     """
     return (float1+float2)/2
# Function that takes an age and returns True if they are of voting age
def voting_age(age: int) -> bool:
     """A function that takes an age and returns True if they are of voting age

     Args:
         param1; Age
     Returns:
            A boolean
     """

     if age >= 18:
          return True


