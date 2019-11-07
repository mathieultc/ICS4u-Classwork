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
    
    def get_first_name(self) -> None:
        return self._first_name
        
    def set_first_name(self, value: str):
        self._first_name = value
        
    def get_last_name(self) -> None:
        return  self._last_name

    def set_last_name(self, value: str):
        self._last_name = value

    def get_email(self) -> None:
        return self._email

    def set_email(self, value: str):
        self._email = value

    def get_DOB(self) -> None:
        return self._DOB

    def greet(self) -> str:
        """Get the person to greet"""
        return f"Hello, my name is {self._first_name} {self._last_name}."

    def get_age(self) -> int:
        """Get the person's age"""
        today = date.today()
        age = today.year - self._DOB.year
        return age
        

class Teacher(Person):
    """Teacher class
    Attrs:
         OCT_PIN(int): The teacher's oct pin
         school(str): The teacher's school
         email_k12(str): The teacher's k12 email
         classes(List): A list of classes
    """
    
    def __init__(self, first_name: str, last_name: str, DOB, OCT_PIN: int, email = None):
        """Creates a teacher object"""
        super().__init__(first_name, last_name, DOB, email)
        self._OCT_PIN = OCT_PIN
        self._classes = []
        self._email_k12 = Teacher.generate_email(self)
        self._school = None
        
    def generate_email(self):
        """generate k12 email"""
        return f"{self._first_name.lower()}.{self._last_name.lower()}@ycdsb.ca"

    def get_OCT_PIN(self) -> int:
        return self._OCT_PIN
    
    def set_OCT_PIN(self, value: int):
        self._OCT_PIN = value

    def get_school(self) -> str:
        return self._school

    def set_school(self, value: str):
        self._school = value

    def greet(self) -> str:
        """Get the teacher to greet"""
        return f"Hello, my name is {self._first_name} {self._last_name} and I'm a teacher."

class Student(Person):
    """class student
    Attrs:
         email_k12(str): The student's k12 email
         student_number(int): The student identification number
    """
    def __init__(self, first_name: str, last_name: str, DOB: date, student_number: int, email = None):
        super().__init__(first_name, last_name, DOB, email)
        self._email_k12 = Student.generate_email(self)
        self._student_number = student_number

    def get_student_number(self) -> int:
        return self._student_number
    
    def set_student_number(self, value):
        self._student_number = value

    def generate_email(self) -> str:
        grad_year = (self._DOB.year % 100) + 18

        return f"{self._first_name.lower()}.{self._last_name.lower()}{grad_year}@ycdsbk12.ca"

    def greet(self) -> str:
        """Get the student to greet"""
        return f"Hello, my name is {self._first_name} {self._last_name} and I'm a student."


class Classroom:
    """Class Classroom
    Attrs:
         subject_name(str): The classroom's subject name
         students(list): A list od students
    """
    def __init__(self, subject_name: str):
        """create classroom object
        Args:
            subject_name: The classroom's subject name
            students: The list of students in the class
        """
        self._subject_name = subject_name
        self._students = []

    def get_subject_name(self) -> str:
        return self._subject_name
    
    def set_subject_name(self, value: str):
        self._subject_name = value

    def get_students(self) -> List:
        return self._students

    def set_students(self, value: List):
        self._students = value

    def add_student(self, student: Student):
        """Add student to the student list"""
        if student in self._students:
            raise Exception
        else:
            self._students.append(student)
        
    def remove_student(self, student: Student):
        """Remove student from the student list"""
        if student not in self._students:
            raise Exception
        else:
            self._students.remove(student)




    
    
