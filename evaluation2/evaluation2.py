
# Evaluation 2 prep quiz
class Food:
    """
    Attrs:
         name: a string
         cost: a number
         nutrition: a number
    """
    def __init__(self, name: str, cost: int, nutrition: int):
        """init method
        Args:
            self: reference to object
            name: a string
            cost: a number
            nutrition: another number
        Returns:
            None
        """
        self.name = name
        self.cost = cost
        self.nutrition = nutrition

class Dog:
    """
    Attrs:
         breed: str
         name: str
         happiness: int
    """
    #init method
    def __init__(self, breed: str, name: str, happiness: int):
        """init method for class Dog
        Args:
            self: reference to object
            breed: a string
            name: a string
            happiness: an integer
        Returns: 
            None
        """
        self.breed = breed
        self.name = name
        self.happiness = 0
    
    #__str__ method
    def __str__(self) -> str:
        """__str__ method
        Args:
            None
        Returns:
            a string
        """
        return f"{self.name}'s happiness increases by {self.happiness}%"

    def bark(self):
        """Bark method
        Args:
            None
        Returns:
            a string
        """

        return "RUFF RUFF!"

    def eat(self, food:Food):
        self.happiness += 0.1 * food.nutrition


