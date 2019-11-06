from typing import List
from datetime import date

class Person:
    """class person
    Attrs:
         first_name(str): The person's first name
         last_name(str): The person's last name
         DOB(datetime): Date of birth
         email(str): None
    """
    def __init__(self, first_name: str, last_name: str, DOB: int, email = None):
        """Creates a person class
        Args:
             first_name: The person's first name
             last_name: The person's last name
             DOB: The person's date of birth
        """
        self._first_name = first_name
        self._last_name = last_name
        self._DOB = DOB
        self._email = email

    def get_first_name(self):
        return self._first_name

    def set_first_name(self, value: str):
        self._first_name = value
        
    def get_last_name(self):
        return  self._last_name

    def set_last_name(self, value: str):
        self._last_name = value

    def get_email(self):
        return self._email

    def set_email(self, value: str):
        self._email = value

    def get_DOB(self):
        return self._DOB

    def greet(self) -> str:
        return f"Hello, my name is {self._first_name} {self._last_name}."

    def get_age(self) -> int:
        today = date.today()
        age = today.year - self._DOB.year
        return age




        