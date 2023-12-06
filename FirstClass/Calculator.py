import CalculatorAddFunction
import CalculatorSubFunction
import CalculatorDivFunction
import CalculatorMulFunction
import CalculatorPowFunction

def use_calculator(num1, num2, operation):
    """
    :param num1: first operand
    :param num2: second operand
    :param operation: the operation that will be applied to num1 and num2
    :return: the result of the operation of num1 and num2
    """

    if type(num1) != float or type(num2) != float or type(operation) != str:
        print("you enterd an incorrect type in one of the vertiables")
        return None

    value = 0
    match operation:
        case "+":
            value = CalculatorAddFunction.calculator_add(num1, num2)

        case "-":
            value = CalculatorSubFunction.calculator_sub(num1, num2)

        case "/":
            value = CalculatorDivFunction.calculator_div(num1, num2)

        case "*":
            value = CalculatorMulFunction.calculator_mul(num1, num2)

        case "**":
            value = CalculatorPowFunction.calculator_pow(num1, num2)

        case _:
            print("you did not enter a viable opertion in the calculator !")
            return None

    return value