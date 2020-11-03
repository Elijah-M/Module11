"""
Author: Elijah Morishita
elmorishita@dmacc.edu
11/2/2020
This program combines two classes, Customer and Invoice
"""


class Customer:

    # The constructor
    def __init__(self, customer_id=1, last_name="Morishita", first_name="Elijah",
                 phone_number="(555) 555-5555", address="123 Main St.\nDes Moines, IA 50265"):
        """
        This constructor sets the variables, with the exception of customer_id which is required
        :param customer_id:
        :param last_name:
        :param first_name:
        :param phone_number:
        :param address:
        """

        if isinstance(customer_id, int) == False:
            print("Non-numeric value entered")
            raise AttributeError

        self._customer_id = customer_id
        self._last_name = last_name
        self._first_name = first_name
        self._phone_number = phone_number
        self._address = address

        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not (name_characters.issuperset(last_name) and name_characters.issuperset(first_name)):
            raise ValueError

    def __str__(self):
        """
        A string conversion method
        :return:
        """
        cust_string = str(self._customer_id)
        return "Customer ID: " + cust_string + "\n"\
        + self._last_name + ', ' + self._first_name + "\n"\
        + self._phone_number + "\n"\
        + self._address

    def __repr__(self):
        """
        An official true string conversion (more accurate)
        :return:
        """
        cust_string = str(self._customer_id)
        return "Customer ID: " + cust_string + "\n"\
        + self._last_name + ', ' + self._first_name + "\n"\
        + self._phone_number + "\n"\
        + self._address

    def display(self):
        """
        This function returns the string of a class object
        :return:
        """
        cust = Customer()
        return cust


class Invoice:
    """
    A constructor that sets the variables
    """
    def __init__(self, invoice_id,  cust_obj, items_with_price={}):

        self._invoice_id = invoice_id
        self._items_with_price = items_with_price
        print(cust_obj.display())

    def __str__(self):
        """
        A string conversion method
        :return:
        """
        invoice_string = str(self._invoice_id)
        return invoice_string

    def __repr__(self):
        """
        An official true string conversion (more accurate)
        :return:
        """
        invoice_string = str(self._invoice_id)
        return invoice_string

    def add_item(self, x):
        """
        This function adds items to a dictionary
        :param x:
        :return:
        """
        self._items_with_price.update(x)

    def create_invoice(self):
        """
        This function calculates the values of the dictionary, prints the tax total,
        and prints the full total
        :return:
        """
        print(invoice, "\n", "=" * 40)
        for x, y in self._items_with_price.items():
            print(x, y)

        tax = 0.06  # tax amount

        tax_total = list(self._items_with_price.values())  # converting the values of the dict to a list

        tax_total_sum = 0
        for x in range(0, len(tax_total)):
            tax_total_sum = tax_total_sum + tax_total[x]

        tax = tax_total_sum * tax  # Tax Total
        total = tax_total_sum + tax  # Total invoice with tax

        print("Tax.....", tax)
        print("Total...", total)


# Driver
captain_mal = Customer(1, 'Reynolds', 'Mel', 'No phones', 'Firefly, somewhere in the verse')
invoice = Invoice(1, captain_mal)
invoice.add_item({'iPad': 799.99})
invoice.add_item({'Surface': 999.99})
invoice.create_invoice()
del captain_mal
