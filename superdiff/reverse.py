"""
Implementing reverse mode differentiation
"""
from numbers import Number

import numpy as np

from superdiff.expression import Var, Expression, get_input_args


class ReverseDiff:
    """
    Class implementing reverse mode differentiation
    """
    def __init__(self, expr):
        self.expr = expr
        self.vars = expr.vars
        self.trace = {}
        self.bars = {}

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
                derivs=[1]
            )
            return args[0]
        else:
            parvals = self.forward(expr.parent1), self.forward(expr.parent2)
            currval = expr.operation(*parvals)
            d1val, d2val = expr.operation.reverse(*parvals)
            self.trace[expr] = dict(
                currval=currval,
                derivs=[d1val, d2val]
            )
            # Updating children for the reverse pass
            for i, parent in enumerate(expr.parents):
                if parent is not None:
                    children = self.trace[parent].get('children', [])
                    children.append((expr, i))  # i tells parent which parent it is (0 or 1)
                    self.trace[parent]['children'] = children
            return currval

    def reverse(self):
        """Compute the reverse pass of forward mode differentiation

        :return: gradient
        """
        return np.array([self._bar(var) for var in self.vars])

    def _bar(self, var):
        if var in self.bars:
            return self.bars.get(var)
        else:
            children = self.trace[var].get('children', [])
            if not children:
                return 1
            res = 0
            for child, i in children:
                res += self._bar(child) * self.trace[child]['derivs'][i]
            return res
