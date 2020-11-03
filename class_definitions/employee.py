"""
Author: Elijah Morishita
elmorishita@dmacc.edu
11/2/2020
This program is used for creating an example of multiple derived classes
"""


class Employee:

    # The constructor
    def __init__(self, last_name, first_name, address, phone_number, salaried, start_date, salary):
        """
        This constructor sets the variables
        :param last_name:
        :param first_name:
        :param address:
        :param phone_number:
        :param salaried:
        :param start_date:
        :param salary:
        """
        self._last_name = last_name
        self._first_name = first_name
        self._address = address
        self._phone_number = phone_number
        self._salaried = salaried
        self._start_date = start_date
        self._salary = salary

    def display(self):
        """
        This function brings the variables together and formats them based
        on if the contructors parameters are either Salaried or Hourly
        :return: either a salried or Hourly string
        """
        if self._salaried == "Salaried":
            info = str(self._first_name + " " + self._last_name + "\n" +
                       self._address + "\n" +
                       self._phone_number + "\n" +
                       "Salaried Employee: " + self._salary + "/year" + "\n" +
                       "Start Date: " + self._start_date)
            return info

        elif self._salaried == "Hourly":
            info = str(self._first_name + " " + self._last_name + "\n" +
                       self._address + "\n" +
                       self._phone_number + "\n" +
                       "Hourly Employee: " + self._salary + "/hour" + "\n" +
                       "Start Date: " + self._start_date)
            return info


# The Driver
emp = Employee("Morishita", "Elijah", "123 Main St.\nDes Moines, IA 50265", "(555) 555-5555", "Salaried", "10/26/2001", "100,000.00")
print(emp.display())
del emp
