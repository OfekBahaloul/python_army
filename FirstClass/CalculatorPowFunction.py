def calculator_pow(num1, num2):
    """
    :param num1: first operand  -> base
    :param num2: second operand
    :return: the power of num1 by num2
    """
    if isinstance(num1, str) or isinstance(num2, str):
        print("you cant power strings")
        return None

    return pow(num1, num2)