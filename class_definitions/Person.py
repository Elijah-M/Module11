"""
Author: Elijah Morishita
elmorishita@dmacc.edu
11/2/2020
This program uses a Student class that derives from the Person class
and prints out student info to the screen
"""


class Person:
    """Person class"""
    def __init__(self, lname, fname, addy=''):
        self._last_name = lname
        self._first_name = fname
        self._address = addy

    def display(self):
        return self._last_name + ", " + self._first_name + ":" + self._address


class Student(Person):
    """ The Student Class, derived from Person"""
    def __init__(self, student_id, lname='UNK', fname='UNK', major="Computer Science", gpa='0.0'):
        super().__init__(lname, fname)
        self._student_id = student_id
        self._major = major
        self._gpa = gpa

    def display(self):
        stu_id_str = str(self._student_id)
        gpa_str = str(self._gpa)
        return self._last_name + ', ' + self._first_name + ':(' + stu_id_str + ') ' + self._major + ' gpa: ' + gpa_str


# Driver
my_student = Student(900111111, 'Song', 'River')
print(my_student.display())
my_student = Student(900111111, 'Song', 'River', 'Computer Engineering')
print(my_student.display())
my_student = Student(900111111, 'Song', 'River', 'Computer Engineering', 4.0)
print(my_student.display())
del my_student
