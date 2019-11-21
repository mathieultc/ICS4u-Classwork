from datetime import date
from typing import List


class Person:
    def __init__(self, first_name: str, last_name: str, DOB: date, email: str =None):
        self._first_name = first_name
        self._last_name = last_name
        self._DOB = DOB
        self._email = email

    def get_first_name(self) -> str:
        return self._first_name

    def set_first_name(self, value: str) -> None:
        self._first_name = value

    def get_last_name(self) -> str:
        return self._last_name

    def set_last_name(self, value: str):
        self._last_name = value

    def get_DOB(self) -> date:
        return self._DOB

    def get_age(self) -> int:
        today = date.today()
        age = today.year - self._DOB.year
        return age

    def get_email(self) -> str:
        return self._email

    def set_email(self, value: str) -> None:
        self._email = value

    def __str__(self) -> str:
        return f"Hi my name is {self._first_name} {self._last_name}, email: {self._email}"


class Student(Person):
    student_count = 0
    classroom_warning = []
    def __init__(self, first_name: str, last_name: str, DOB: date, student_id: int, email = None):
        super().__init__(first_name, last_name, DOB, email)
        self._email_k12 = Student.generate_email(self)
        self._student_id = student_id
        Student.student_count += 1
        self._classes = []

    def generate_email(self) -> str:
        grad_yr = (self._DOB.year % 100) + 18
        return f"{self._first_name}{self._last_name}{grad_yr}@ycdsbk12.ca"

    def get_student_id(self) -> int:
        return self._student_id

    def set_student_id(self, value: int) -> None:
        self._student_id = value

    def get_classes(self) -> List[str]:
        return self._classes
    
    def set_classes(self, value) -> None:
        self._classes = value

    def __str__(self):
        return super().__str__() + " Hi I'm a good student"

    def add_class(self, classroom: "Classroom"):
        if classroom in self._classes:
            raise Exception("Can't enroll in two similar classes")
        self._classes.append(classroom)
        if len(self._classes) > 4:
            warning = "too many classes"
            Student.classroom_warning.append(warning)
            

class Classroom:
    def __init__(self, name):
        self._name = name

    def get_name(self) -> str:
        return self._name
    
    def set_name(self, value) -> None:
        self._name = value



