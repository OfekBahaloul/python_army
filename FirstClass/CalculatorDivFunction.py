def calculator_div(num1, num2):
    """
    :param num1: first operand
    :param num2: second operand
    :return: the division Of num2 and num1
    """
    if isinstance(num1, str) or isinstance(num2, str):
        print("you cant divis strings")
        return None

    return num1 / float(num2)