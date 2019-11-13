from typing import Union

from expression import Expression, Var


def make_expression(expr: Union[Var, Expression], vars=None) -> Expression:
    """Returns an expression with the varlist in the specified order

    :param expr: Expression -- the expression
    :param vars: list[Var] -- A list of Var objects, default None
    """
    if vars is not None:
        expr.set_vars(vars)
    return expr
