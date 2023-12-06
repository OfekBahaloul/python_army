def calculator_sub(num1, num2):
    """
    :param num1: first operand
    :param num2: second operand
    :return: the sub Of num2 from num1
    """
    if isinstance(num1, str) or isinstance(num2, str):
        print("you cant sub up strings")
        return None

    return num1 - num2