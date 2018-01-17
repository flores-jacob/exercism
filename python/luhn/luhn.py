class Luhn(object):
    def __init__(self, string_input):
        self.string_input = string_input
        self.preprocessed_input = self.preprocess()

    def preprocess(self):
        return self.string_input.replace(" ", "")

    def is_valid(self):
        string_len = len(self.preprocessed_input)

        # check if string length is less than 1
        if string_len <= 1:
            return False

        string_sum = 0
        # Multiply every second digit from the right by two (and subtract
        # 9 if necessary, then add this to the sum.
        # For every other digit from the right, just add them to the sum
        for i in range(string_len):
            current_char = self.preprocessed_input[string_len - 1 - i]
            if not current_char.isdigit():
                return False
            num_val = int(current_char)
            if (i + 1) % 2 == 0:
                num_val *= 2
                if num_val > 9:
                    num_val -= 9
            string_sum += num_val

        # Check if sum is divisible by 10
        return string_sum % 10 == 0
