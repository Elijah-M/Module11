"""
Author: Elijah Morishita
elmorishita@dmacc.edu
11/4/2020
This program is used for creating an example of multiple inheritance
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


class Employee:

    def __init__(self, last_name="Morishita", first_name="Elijah", address="123 Main St.\nDes Moines, IA 50265",
                 phone_number="(555) 555-5555"):

        self._last_name = last_name
        self._first_name = first_name
        self._address = address
        self._phone_number = phone_number

    def display(self):

        return "Name: " + self._last_name + ', ' + self._first_name + '\n'\
        + "Address: " + self._address + '\n'\
        + "Phone Number: " + self._phone_number


class SalariedEmployee(Employee):
    """The SalariedEmployee class which derives from Employee"""
    def __init__(self, start_date, salary=40000):
        super().__init__()
        self._start_date = start_date
        self._salary = salary

    def give_raise(self, salary):
        self._salary = salary

    def display(self):
        salary = str(self._salary)
        return "Name: " + self._last_name + ', ' + self._first_name + '\n'\
        + "Start Date: " + self._start_date + '\n'\
        + "Salary: $" + salary


class HourlyEmployee(Employee):
    """The HourlyEmployee class which derives from Employee"""
    def __init__(self, start_date, hourly_pay=10.00):
        super().__init__()
        self._start_date = start_date
        self._hourly_pay = hourly_pay

    def give_raise(self, hourly_pay):
        self._hourly_pay = hourly_pay

    def display(self):
        hourly_pay = str(self._hourly_pay)
        return "Name: " + self._last_name + ', ' + self._first_name + '\n'\
        + "Start Date: " + self._start_date + '\n'\
        + "Hourly Pay: $" + hourly_pay


class Manager(Employee, Person):
    """The Manager class, which derives from the employee and Person class"""



    def __init__(self, last_name="Morishita", first_name="Elijah", start_date="11/4/2020", salary="40000"):

        self._last_name = last_name
        self._first_name = first_name
        self._start_date = start_date
        self._salary = salary

    direct_reports = []

    direct_reports.append(Employee("Smith", "John", "111 2nd St.\nDes Moines, IA 50265", "(555) 555-5555"))
    direct_reports.append(Employee("Williams", "Jane", "222 3rd St.\nChicago, IL 54032", "(555) 555-5555"))
    direct_reports.append(Employee("Johnson", "Jim", "333 4th St.\nMinniapolis, MN 52455", "(555) 555-5555"))
    direct_reports.append(Employee("Wilson", "Jones", "444 5th St.\nOmaha, NE 60988", "(555) 555-5555"))
    direct_reports.append(Employee("O'Brien", "Jeffrey", "555 6th St.\nKansas City, MO 45433", "(555) 555-5555"))

    def __repr__(Employee):
        return Employee.direct_reports

    def __repr__(Manager):
        return Manager.direct_reports

    def department(self, index):
        """
        The department attribute returns the department #
        :param: index
        :return: index
        """
        return index

    def display(self, index):
        """
        this function displays the direct reports based on department #
        :param: index
        :return:
        """
        print(self.direct_reports[index])

# Driver
team_coordinator = Manager()
team_coordinator.display(0)  # displays direct_reports
Manager("Jane", "Doe", "234 Main St", "42000")  # salary change
team_coordinator.display(3)  # displays direct_reports

# Garbage collection
del team_coordinator

