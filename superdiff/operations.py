import numpy as np
from numbers import Number
from .expression import Var, Expression


class OperationType(type):
    def __str__(self):
        return self.__name__


class BaseOperation:
    __metaclass__ = OperationType

    @classmethod
    def check_type(cls, *args):
        """
        :param args: tuple(Object) -- Parameters to check
        :return: None
        :raises: AssertionError if all elements of args are not a Var or Number
        """
        for x in args:
            assert isinstance(x, Var) or isinstance(x, Number), "Not a number/Variable/Expression"


class UnaryOperation(BaseOperation):
    @classmethod
    def expr(cls, expr):
        """Create a new expression

        :param expr: Var | Number -- Parent expression
        :return: Var | Number -- new expression
        """
        cls.check_type(expr)
        return Expression(expr, None, cls)

    @classmethod
    def eval(cls, num):
        """Evaluate the operation at `num`

        :param num: Number -- argument to the unary operation
        :return: Number -- result of evaluation
        """
        raise NotImplementedError()

    @classmethod
    def deriv(cls, val, der):
        """Evaluate the derivative at value = `val` and derivative = `deriv`

        :param val: Number -- Value of the argument
        :param der: Number -- Value of the derivative of the argument
        :return: Number -- The derivative
        """
        raise NotImplementedError()


class BinaryOperation(BaseOperation):
    @classmethod
    def expr(cls, expr1, expr2):
        """Create a new expression

        :param expr1: Var | Number -- Expression or number to become parent 1
        :param expr2: Var | Number -- Expression or number to become parent 2
        :return:
        """
        cls.check_type(expr1, expr2)
        return Expression(expr1, expr2, cls)

    @classmethod
    def eval(cls, num1, num2):
        """Evaluate the expression at `num2`, `num2`

        :param num1: Number -- First argument to the operation
        :param num2: Number -- Second argument to the operation
        :return:
        """
        raise NotImplementedError()

    @classmethod
    def deriv(cls, num1, deriv1, num2, deriv2):
        """Differentiate the expression at the given values

        :param num1: Number -- Value of parent 1
        :param deriv1: Number -- Value of derivative of parent 1
        :param num2: Number -- Value of parent 2
        :param deriv2: Number -- Value of parent 2
        :return:
        """
        raise NotImplementedError()


class Add(BinaryOperation):
    @classmethod
    def eval(cls, num1, num2):
        # super().check_type(num1)
        # super().check_type(num2)
        return num1 + num2

    @classmethod
    def deriv(cls, num1, deriv1, num2, deriv2):
        return deriv1 + deriv2


class Sub(BinaryOperation):
    @classmethod
    def eval(cls, num1, num2):
        return num1 - num2

    @classmethod
    def deriv(cls, num1, deriv1, num2, deriv2):
        return deriv1 - deriv2


class Mul(BinaryOperation):
    @classmethod
    def eval(cls, num1, num2):
        return num1 * num2

    @classmethod
    def deriv(cls, num1, deriv1, num2, deriv2):
        return num1 * deriv2 + num2 * deriv1


class Div(BinaryOperation):
    @classmethod
    def eval(cls, num1, num2):
        return num1 / num2

    @classmethod
    def deriv(cls, num1, deriv1, num2, deriv2):
        print(num1,deriv1,num2, deriv2)
        print((num1 * deriv2 - num2 * deriv1) / (num2 ** 2))
        return -(num1 * deriv2 - num2 * deriv1) / (num2 ** 2)


class Pow(BinaryOperation):
    @classmethod
    def eval(cls, num1, num2):
        return num1 ** num2

    @classmethod
    def deriv(cls, num1, deriv1, num2, deriv2):
        return np.exp(num2 * np.log(num1)) * (deriv2 * np.log(num1) + num2 * deriv1 / num1)

class Exp(UnaryOperation):
    @classmethod
    def eval(cls, num):
        return np.exp(num)

    @classmethod
    def deriv(cls, num, deriv):
        return deriv*np.exp(num)

class NLog(UnaryOperation):
    @classmethod
    def eval(cls, num):
        return np.log(num)

    @classmethod
    def deriv(cls, val, der):
        return der / val

class Log(BinaryOperation):
    @classmethod
    def eval(cls, num, base = np.e):
        return np.log(num) / np.log(base)

    @classmethod
    def deriv(cls, val, der, base = np.e, base_der = 0):
        return (((der / val) * np.log(base)) - ((base_der / base) * np.log(val))) / (np.log(base)**2)


class Sin(UnaryOperation):
    @classmethod
    def eval(cls, num):
        return np.sin(num)

    @classmethod
    def deriv(cls, val, der):
        return np.cos(val) * der


class Cos(UnaryOperation):
    @classmethod
    def eval(cls, num):
        return np.cos(num)

    @classmethod
    def deriv(cls, val, der):
        return -np.sin(val) * der


class Tan(UnaryOperation):
    @classmethod
    def eval(cls, num):
        return np.tan(num)

    @classmethod
    def deriv(cls, val, der):
        return der / (np.cos(val) ** 2)

class Csc(UnaryOperation):
    @classmethod
    def eval(cls, num):
        return 1/np.sin(num)

    @classmethod
    def deriv(cls, val, der):
        return -der*(1/np.sin(val))*(1/np.tan(val))

class Sec(UnaryOperation):
    @classmethod
    def eval(cls, num):
        return 1/np.cos(num)

    @classmethod
    def deriv(cls, val, der):
        return der*(1/np.cos(val))*np.tan(val)

class Cot(UnaryOperation):
    @classmethod
    def eval(cls, num):
        return 1/np.tan(num)

    @classmethod
    def deriv(cls, val, der):
        return -der*(1/np.sin(val))**2
