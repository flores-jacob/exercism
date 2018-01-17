class Luhn(object):
    def __init__(self, string_input):
        self.string_input = string_input

    def is_valid(self):
        processed_input = self.string_input.replace(" ", "")

        # check if string length is less than 1 or string has non digit chars
        if len(processed_input) <= 1 or (not processed_input.isdigit()):
            return False

        # get sum of digits according to the luhn rules
        doubles_sum = sum([int(num) * 2 - 9 if int(num) * 2 > 9 else int(num) * 2 for num in processed_input[-2::-2]])
        singles_sum = sum([int(num) for num in processed_input[-1::-2]])

        # check if sum is divisible by 10
        return (doubles_sum + singles_sum) % 10 == 0
