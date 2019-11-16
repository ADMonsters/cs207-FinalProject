import numpy as np
from numbers import Number
from .expression import Var, Expression


class OperationType(type):
    def __str__(self):
        return self.__name__


class BaseOperation:
    __metaclass__ = OperationType

    @classmethod
    def check_type(cls, x):
        """
        :param x: Object -- Parameter to check
        :return: None
        :raises: AssertionError if `x` is not a Var or Number
        """
        assert isinstance(x, Var) or isinstance(x, Number), "Not a number/Variable/Expression"


class UnaryOperation(BaseOperation):
    @classmethod
    def expr(cls, expr):
        """Create a new expression

        :param expr: Var | Number -- Parent expression
        :return: Var | Number -- new expression
        """
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
        return (num1 * deriv2 - num2 * deriv1) / (num2 ** 2)


class Pow(BinaryOperation):
    @classmethod
    def eval(cls, num1, num2):
        return num1 ** num2

    @classmethod
    def deriv(cls, num1, deriv1, num2, deriv2):
        return np.log(num2 * np.log(num1)) * (deriv2 * np.log(num1) + num2 * deriv1 / num1)


class Log(UnaryOperation):
    @classmethod
    def eval(cls, num):
        return np.log(num)

    @classmethod
    def deriv(cls, val, der):
        return val / der


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

#
# def checktype(x):
#     '''
#     raises error if the input is not a number/Variable/Expression
#     '''
#     assert isinstance(x, Var) or isinstance(x, Number), "Not a number/Variable/Expression"
#
#
# class add():
#
#     @staticmethod
#     def expr(left, right): # this method makes an Expression
#         checktype(left)
#         checktype(right)
#
#         node = Expression(parent1=left, parent2=right, operation=add)
#         return node
#
#     @staticmethod
#     def value(left, right):
#
#         return left + right
#
#     @staticmethod
#     def deriv(left, right):
#
#         return left_der + right_der
#
#
# class sub(Binary):
#
#     @staticmethod
#     def expr(left, right): # this method makes an Expression
#         checktype(left)
#         checktype(right)
#
#         node = Expression(parent1=left, parent2=right, operation=sub)
#         return node
#
#     @staticmethod
#     def value(left, right):
#
#         return left - right
#
#     @staticmethod
#     def deriv(left_der, right_der, left_val, right_val):
#
#         return left_der - right_der
#
#
# class mul():
#
#     @staticmethod
#     def expr(left, right):  # this method makes an Expression
#         checktype(left)
#         checktype(right)
#
#         node = Expression(parent1=left, parent2=right, operation=mul)
#         return node
#
#     @staticmethod
#     def value(left, right):
#
#         return left * right
#
#     @staticmethod
#     def deriv(left_der, right_der, left_val, right_val):
#
#         result = left_der * right_val + left_val * right_der
#         return result
#
#
# class div():
#
#     @staticmethod
#     def expr(left, right): # this method makes an Expression
#         checktype(left)
#         checktype(right)
#
#         node = Expression(parent1=left, parent2=right, operation=div)
#         return node
#
#     @staticmethod
#     def value(left, right):
#
#         return left / right
#
#     @staticmethod
#     def deriv(left_der, right_der, left_val, right_val):
#
#         result = (left_der * right_val - left_val * right_der) / (right_val)**2
#         return result
#
#
#
# def neg(expression):
#     '''
#     unary operation that returns the negative of something
#     '''
#     return 0 - expression
#
#
#
# def pos(expression):
#     '''
#     unary operation that returns the positive of something
#     '''
#     return 0 + expression
#
#
# class log():
#     """
#     This is natural logarithm.
#     param exponent -- an Expression or a number
#     """
#
#     @staticmethod
#     def expr(exponent):
#         if isinstance(exponent, Var):  # returns an Expression
#
#             node = Expression(parent1=exponent, parent2=None, operation=log)
#             return node
#
#         elif isinstance(exponent, Number):  # log(number) is just a number
#             return np.log(exponent)
#
#         else:
#             raise TypeError("Not a number/Variable/Expression")
#
#     @staticmethod
#     def value(exponent):
#
#         return np.log(exponent)
#
#     @staticmethod
#     def deriv(exponent_der, exponent_val):
#
#         result = 1 / exponent_val * exponent_der
#         return result
#
# class exp():
#     """
#     This is e to the x-th power.
#     param exponent -- an Expression or a number
#     """
#
#     @staticmethod
#     def expr(exponent):
#         if isinstance(exponent, Var):  # returns an Expression
#
#             node = Expression(parent1=exponent, parent2=None, operation=exp)
#             return node
#
#         elif isinstance(exponent, Number):  # exp(number) is just a number
#             return np.exp(exponent)
#
#         else:
#             raise TypeError("Not a number/Variable/Expression")
#
#     @staticmethod
#     def value(exponent):
#
#         return np.e ** exponent
#
#     @staticmethod
#     def deriv(exponent_der, exponent_val):
#
#         result = exponent_val * exponent_der
#         return result
#
#
# def pow(base, exponent):
#     '''
#     returns an Expression
#     pow(base, exponent) = exp(exponent * log(base))
#     '''
#     nodes = Expression(exp.expr(exponent * log.expr(base)))
#     return nodes
#
#
#
# class sin():
#     """
#     This is sine function.
#     param angle -- an Expression or a number
#     """
#
#     @staticmethod
#     def expr(exponent):
#         if isinstance(angle, Var):  # returns an Expression
#
#             node = Expression(parent1=angle, parent2=None, operation=sin)
#             return node
#
#         elif isinstance(angle, Number):  # exp(number) is just a number
#             return np.sin(angle)
#
#         else:
#             raise TypeError("Not a number/Variable/Expression")
#
#
#     @staticmethod
#     def value(angle):
#
#         return np.sin(angle)
#
#     @staticmethod
#     def deriv(angle_der, angle_val):
#
#         result = np.cos(angle_val) * angle_der
#         return result
#
#
# class cos():
#     """
#     This is cosine function.
#     param angle -- an Expression or a number
#     """
#
#     @staticmethod
#     def expr(exponent):
#         if isinstance(angle, Var):  # returns an Expression
#
#             node = Expression(parent1=angle, parent2=None, operation=cos)
#             return node
#
#         elif isinstance(angle, Number):  # exp(number) is just a number
#             return np.cos(angle)
#
#         else:
#             raise TypeError("Not a number/Variable/Expression")
#
#     @staticmethod
#     def value(angle):
#
#         return np.cos(angle)
#
#     @staticmethod
#     def deriv(angle_der, angle_val):
#
#         result = -np.sin(angle_val) * angle_der
#         return result
#
#
# class tan():
#     """
#     This is tangent function.
#     param angle -- an Expression or a number
#     """
#
#     @staticmethod
#     def expr(exponent):
#         if isinstance(angle, Var):  # returns an Expression
#
#             node = Expression(parent1=angle, parent2=None, operation=tan)
#             return node
#
#         elif isinstance(angle, Number):  # exp(number) is just a number
#             return np.tan(angle)
#
#         else:
#             raise TypeError("Not a number/Variable/Expression")
#
#     @staticmethod
#     def value(angle):
#
#         return np.tan(angle)
#
#     @staticmethod
#     def deriv(angle_der, angle_val):
#
#         result = 1 / np.cos(angle_val)**2 * angle_der
#         return result
