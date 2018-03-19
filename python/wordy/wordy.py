def calculate(question):
    split_question = question.split()

    answer = None

    for index, word in enumerate(split_question):
        if (word == "plus") or (word == "minus"):
            num1 = split_question[index - 1]
            num2 = split_question[index + 1].rstrip("?")

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
        elif (word == "multiplied") or (word == "divided"):
            num1 = split_question[index - 1]
            num2 = split_question[index + 2].rstrip("?")
            if word == "multiplied":
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
            num1 = split_question[index - 1]
            num2 = split_question[index + 4].rstrip("st").rstrip("nd").rstrip("rd").rstrip("th")

            if answer:
                answer **= int(num2)
            else:
                answer = int(num1) ** int(num2)

    if answer is not None:
        return answer
    else:
        raise ValueError("Improper question")