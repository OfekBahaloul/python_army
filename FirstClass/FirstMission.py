def factorial(factorial_number):
    """
    :param factorial_number: a number that represents an index of a factorial number
    :return: the number in the factorial index
    """
    if not isinstance(factorial_number, int):
        print("you should have enterd a number !")
        return None

    if factorial_number < 0:
        print("there is no such thing as a negative factorial!")
        return None

    current_sum = 1
    for i in range(1, factorial_number):
        current_sum *= i

    return current_sum


def fibonachi(num_of_fibonachi):
    """
    :param num_of_fibonachi: index in the fibonachi sequence
    :return: the fibonachi number in the num index
    """
    if not isinstance(num_of_fibonachi, int):
        print("you should have enterd a number !")
        return None

    if num_of_fibonachi <= 0:
        print("there is no such thing as a negative fibonachi !")
        return 0
    elif num_of_fibonachi == 1:
        return 1
    elif num_of_fibonachi == 2:
        return 1

    return fibonachi(num_of_fibonachi - 1) + fibonachi(num_of_fibonachi - 2)


def gcd(number1, number2):
    """
    :param number1: number to find its common dividor with number2
    :param number2: number to find its common dividor with number1
    :return: the common dividor of both number1 and number2
    """
    if isinstance(number1, str) or isinstance(number2, str):
        print("you should have enterd a number !")
        return None

    if number1 == 0:
        return number2

    return gcd(number2 % number1, number1)

