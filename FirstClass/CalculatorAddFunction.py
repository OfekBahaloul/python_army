def calculator_add(num1, num2):
    """
    :param num1: first operand
    :param num2: second operand
    :return: the addition of both num1 and num2
    """
    if isinstance(num1, str) or isinstance(num2, str):
        print("you cant add up strings")
        return None

    return num1 + num2
