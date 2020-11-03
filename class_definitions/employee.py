"""
Author: Elijah Morishita
elmorishita@dmacc.edu
11/2/2020
This program is used for creating an example of multiple derived classes
"""


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


# The Driver
supervisor = SalariedEmployee("11/2/2020")
print(supervisor.display())  # printing the SalariedEmployee object
divider = '=' * 40  # just a divider
print(divider)  # ===================
CEO = Employee()
print(CEO.display())  # Displaying the Employee object
print(divider)  # ===================
supervisor.give_raise(45000)
print(supervisor.display())  # printing the SalariedEmployee object
print(divider)  # ===================
CEO = Employee()
print(CEO.display())  # Displaying the Employee object again
print(divider)  # ===================
assembler = HourlyEmployee("11/2/2020")
print(assembler.display())  # printing the HourlyEmployee object
print(divider)  # ===================
CEO = Employee()
print(CEO.display())  # Displaying the Employee object again
print(divider)  # ===================
assembler.give_raise(12.00)
print(assembler.display())  # printing the HourlyEmployee object
print(divider)  # ===================
CEO = Employee()
print(CEO.display())  # Displaying the Employee object again

# Garbage collection
del supervisor
del assembler
del CEO
