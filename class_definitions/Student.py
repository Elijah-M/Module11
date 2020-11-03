class Student:
    """ The Student class"""

    def __init__(self, name, major, start_date, gpa=4.0):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'- ")
        if not (name_characters.issuperset(name)):
            raise ValueError
        self._name = name
        self._major = major
        self._start_date = start_date
        self._gpa = gpa

    def change_major(self, major):
        """
        changes the major
        :param major:
        :return:
        """
        self._major = major

    def update_gpa(self, gpa):
        """
        changes the gpa
        :param gpa:
        :return:
        """
        self._gpa = gpa

    def display(self):
        """
        displays the student's information
        :return: student_info
        """
        gpa_str = str(self._gpa)  # convert from float to string
        student_info = str("Name: " + self._name + "\n"\
                           + "Major: " + self._major + "\n"\
                           + "Start Date: " + self._start_date + "\n"\
                           + "GPA: " + gpa_str)
        return student_info


# Driver
freshmen = Student("Elijah Morishita", "Coding", "11/2/2020")
print(freshmen.display())
freshmen.change_major('Being Awesome!')
freshmen.update_gpa(3.0)
print('=' * 40)  # just a divider
print(freshmen.display())
