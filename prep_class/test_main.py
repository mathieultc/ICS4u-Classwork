from datetime import date
from main import Person, Student, Classroom
import pytest

def test_student():
    student = Student("john", "smith", date(2002, 7, 8), 1234)
    assert student.get_age() == 17
    assert student._email_k12 == "johnsmith20@ycdsbk12.ca"
    student.set_first_name("John")
    assert student.get_first_name() == "John"

    for i in range(20):
        Student("", "", date(2002, 8, 2), i)

    assert Student.student_count == 21
    

def test_student_add_class():
    student = Student("john", "smith", date(2002, 8, 7), 1234)
     
    for i in range(5):
         classroom = Classroom("Math")
         student.add_class(classroom)

    warning = Student.classroom_warning[0]
    assert warning == "too many classes"

def student_exception():
    student = Student("john", "smith", date(2002, 8, 7), 1234)
    classroom = Classroom("math")

    student.add_class(classroom)
    with pytest.raises(Exception):
        student.add_class(classroom)








