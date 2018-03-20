class Phone(object):
    def __init__(self, phone_number):
        # Retain only the digits in the string
        number_list = [char for char in phone_number if char.isdigit()]

        # Check number length. if length is 11, and number begins with country code 1, then return last 10 numbers
        if (len(number_list) == 11) and number_list[0] == "1":
            number_list = number_list[1:]
        # If number_length is incorrect, or if the area code is incorrect, raise an error
        elif (len(number_list) != 10) or (number_list[0] not in [1, 2, 3, 4, 5, 6, 7, 8, 9]):
            raise ValueError("Invalid phone number")

        self.number = "".join(number_list)
