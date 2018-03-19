def calculate(question):
    split_question = question.split()

    answer = None

    for index, word in enumerate(split_question):
        if (word == "plus") or (word == "minus"):
            offset = 1
        elif (word == "multiplied") or (word == "divided"):
            offset = 2
        elif word == "raised":
            offset = 4
        else:
            offset = None

        if offset:
            num1 = split_question[index - 1]
            num2 = split_question[index + offset].rstrip("?").rstrip("st").rstrip("nd").rstrip("rd").rstrip("th")

            if word == "plus":
                if answer:
                    answer += int(num2)
                else:
                    answer = int(num1) + int(num2)
            elif word == "minus":
                if answer:
                    answer -= int(num2)
                else:
                    answer = int(num1) - int(num2)
            elif word == "multiplied":
                if answer:
                    answer *= int(num2)
                else:
                    answer = int(num1) * int(num2)
            elif word == "divided":
                if answer:
                    answer /= int(num2)
                else:
                    answer = int(num1) / int(num2)
            elif word == "raised":
                if answer:
                    answer **= int(num2)
                else:
                    answer = int(num1) ** int(num2)

    if answer is not None:
        return answer
    else:
        raise ValueError("Improper question")