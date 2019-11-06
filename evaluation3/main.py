from typing import List
from datetime import date

class Person:
    """class Person

    Attrs:
         first_name(str): The person's first_name
         last_name(str): The person's last_name
         email(str): The person's email
         DOB(str): The date of birth of the person
    """
    def __init__(self, first_name: str, last_name: str, DOB: str):
        """creates a person object
        Args:
            first_name: the person's first name
            last_name: the person's last name
            DOB: the person's date of birth
        """
        self._first_name = first_name
        self._last_name = last_name
        self._email = None
        self._DOB = DOB

    def get_first_name(self):
        return self._first_name

    def set_first_name(self, value: str):
        self._first_name = value

    def get_last_name(self):
        return self._last_name
    
    def set_last_name(self, value: str):
        self._last_name = value

    def get_email(self):
        return self._email

    def set_email(self, value: str):
        self._email = value

    def get_DOB(self):
        return self._DOB

    def greet(self) -> str:
        """get the person to greet"""
        return "Good morning!"

    def get_age(self) -> int:
        today = date.today()
        age = today.year - self._DOB.year
        return age

class Teacher(Person):
    """class teacher
     Attrs:
           OCT_PIN(int): The teacher's oct pin
           school(str): The school at which the teacher teaches
           email_k12(str): The teacher's k12 email
           classes(List): A list of classes
    """
    def __init__(self, OCT_PIN: int, school: str, email_k12: str):
        """Creates a teacher object
        Args:
            OCT_PIN: teacher's pin
            school: teacher's school
            email_k12: teacher's k12 email
        """
        self.OCT_PIN = OCT_PIN
        self.school = school
        super().__init__(email_k12)
        self.classes = []

    def assign_work(self, classroom: Classroom):
        """get the teacher to assign a work"""
        print(f"Ms {self._first_name} assigns work to {classroom.name}")

    def greet(self):
        """get the teacher to greet the class"""
        print("good morning class")

    def add_class(self, classroom: Classroom):
        """add class to the list"""
        if len(self.classes) < 6:
            self.classes.append(classroom)
        
    def remove_class(self, classroom: Classroom):
        """remove class from the list"""
        self.classes.remove(classroom)

    @classmethod
    def search_teacher_pin(cls, pin: int):
        pass

    @classmethod
    def search_teacher_lname(cls, last_name: str):
        pass
        

class Classroom:
    """Classroom class
    Attrs:
         subject_name(str): The course name of the class
         students(List): List of students in the class
    """
    def __init__(self, subject_name: str):
        """Creates a classroom object"""

        self._subject_name = subject_name
        self.students = []

    def get_subject_name(self):
        return self._subject_name

    def set_subject_name(self, value):
        self._subject_name = value

    def add_student(self):
        """add student to a class"""
        self.students.append(student)

    def remove_student(self):
        """remove a student from a class"""
        self.students.remvoe(student)

class Student(Person):
    """Student class
    Attrs:
         email_k12(str): The student's email
         student_id(int): Student identification
    """
    def __init__(self, email_k12: str, student_id: int):
        """Creates a student object
        Args:
            email_k12: The student's email
            student_id: The student identification
        """
        super().__init__(email_k12)
        self._student_id = student_id

    def get_student_id(self):
        return self._student_id

    def set_student_id(self, value):
        self._student_id = value
        
    def greet(self):
        """get the student to greet"""
        print("Hi, everyone!")

