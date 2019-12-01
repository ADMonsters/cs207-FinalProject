from typing import Union
import numpy as np
from superdiff.expression import Expression, Var, VectorExpression
from superdiff import operations as ops


def make_expression(*exprs: Union[Var, Expression], vars=None) -> Union[Expression, VectorExpression]:
    """Returns an expression with the varlist in the specified order

    :param expr: Expression | VectorExpression -- the expression (or iterable of expressions
    :param vars: list[Var] -- A list of Var objects, default None
    """
    for expr in exprs:
        if vars is not None:
            expr.set_vars(vars)
    if len(exprs) > 1:
        return VectorExpression(exprs, varlist=vars)
    else:
        return exprs[0]


# Operations
def add(expr1, expr2):
    return ops.Add.expr(expr1, expr2)


def sub(expr1, expr2):
    return ops.Sub.expr(expr1, expr2)


def mul(expr1, expr2):
    return ops.Mul.expr(expr1, expr2)


def div(expr1, expr2):
    return ops.Div.expr(expr1, expr2)


def pow(expr1, expr2):
    return ops.Pow.expr(expr1, expr2)


def sqrt(expr):
    return ops.Sqrt.expr(expr)


def neg(expr):
    return ops.Neg.expr(expr)


def exp(expr):
    return ops.Exp.expr(expr)


def log(expr1, expr2 = np.e):
    return ops.Log.expr(expr1, expr2)


def nlog(expr):
    return ops.NLog.expr(expr)


def sin(expr):
    return ops.Sin.expr(expr)


def cos(expr):
    return ops.Cos.expr(expr)


def tan(expr):
    return ops.Tan.expr(expr)


def csc(expr):
    return ops.Csc.expr(expr)


def sec(expr):
    return ops.Sec.expr(expr)


def cot(expr):
    return ops.Cot.expr(expr)


def dot(expr1, expr2):
    return ops.Dot.expr(expr1, expr2)
