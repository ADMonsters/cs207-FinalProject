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
            return None
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
            # Parsing args
            p1_args, p2_args = get_input_args(expr.parent1, expr.vars, *args), \
                               get_input_args(expr.parent2, expr.vars, *args)
            parvals = self.forward(expr.parent1, *p1_args), self.forward(expr.parent2, *p2_args)

            # For now, implementing unary/binary as an if-statement. Consider subclassing
            if parvals[1] is None:
                currval = expr.operation.eval(parvals[0])
                d1val = expr.operation.reverse(parvals[0])
                derivs = [d1val]
            else:
                currval = expr.operation.eval(*parvals)
                d1val, d2val = expr.operation.reverse(*parvals)
                derivs = [d1val, d2val]
            self.trace[expr] = dict(
                currval=currval,
                derivs=derivs
            )
            # Updating children for the reverse pass
            for i, parent in enumerate(expr.parents):
                if isinstance(parent, Var):
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

    def __call__(self, *args, **kwargs):
        self.forward(self.expr, *args)
        return self.reverse()
