"""
Implementing reverse mode differentiation
"""
from numbers import Number

from superdiff.expression import Var, Expression, get_input_args


class ReverseDiff:
    """
    Class implementing reverse mode differentiation
    """
    def __init__(self, expr):
        self.expr = expr
        self.vars = expr.vars
        self.trace = {}

    def forward(self, expr, *args):
        """Compute the forward pass of reverse mode differentiation

        :param expr: Var -- Expression to be differentiated
        :param args: tuple -- Arguments to differentiate the expression at
        :return: Number -- evaluated expression
        """
        if expr is None:
            return 0
        if isinstance(expr, Number):
            return expr
        if expr in self.trace:  # Here we check if we have already visited this node
            return args[0]
        if not isinstance(expr, Expression):
            self.trace[expr] = dict(
                currval=args[0],
                d1val=1,
                d2val=0
            )
            return args[0]
        else:
            parvals = self.forward(expr.parent1), self.forward(expr.parent2)
            currval = expr.operation(*parvals)
            d1val, d2val = expr.operation.reverse(*parvals)
            self.trace[expr] = dict(
                currval=currval,
                d1val=d1val,
                d2val=d2val
            )
            # Updating children for the reverse pass
            for parent in expr.parents:
                if parent is not None:
                    children = self.trace[parent].get('children', [])
                    children.append(expr)
                    self.trace[parent]['children'] = children
            return currval

    def reverse(self, expr, *args):
        """Compute the reverse pass of forward mode differentiation

        :param expr: Var -- Expression to be differentiated
        :param args: tuple -- Arguments to differentiate the expression at
        :return: gradient
        """
        grad = np.zeros(len(self.vars))
        for var in self.vars:
            