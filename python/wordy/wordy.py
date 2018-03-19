def calculate(question):
    operation = {
        'plus': lambda a, b: a + b,
        'minus': lambda a, b: a - b,
        'multiplied': lambda a, b: a * b,
        'divided': lambda a, b: a / b,
        'raised': lambda a, b: a ** b,
    }
    offsets = {
        'plus': 1,
        'minus': 1,
        'multiplied': 2,
        'divided': 2,
        'raised': 4,
    }

    split_question = question.split()

    answer = None
    operator_count = 0
    operand_count = 0

    for index, word in enumerate(split_question):
        if word.lstrip("-").rstrip("?").isdigit():
            operand_count += 1

        if word in offsets.keys():
            operator_count += 1

            try:
                num1 = int(split_question[index - 1])
                num2 = int(split_question[index + offsets[word]].rstrip("?").rstrip("st").rstrip("nd").rstrip("rd").rstrip("th"))
            except:
                raise ValueError("Missing operand")

            if answer:
                answer = operation[word](answer, num2)
            else:
                answer = operation[word](num1, num2)

    if operand_count != operator_count + 1:
        raise ValueError("missing operator")
    elif answer is not None:
        return answer
    else:
        raise ValueError("Improper question")
