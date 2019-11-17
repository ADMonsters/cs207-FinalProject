"""
expression.py

Classes:
    Var
        - Base class for individual variables
    Expression
        - Inherits from Var
        - Can be combined into larger expressions
"""
from typing import Union
from numbers import Number

import superdiff as sd


class Var:
    """A Variable.

    Attributes:
        :name: str -- The common name for the variable (e.g. 'x', 'y', 'x1')

    Methods:
        eval () -> Number -- Evaluate the variable for a given input (always return the number itself)

    """
    def __init__(self, name):
        self._vars = None
        self.name = name

    def eval(self, x):
        """
        Evaluate the variable at x (identity function)

        :param x: Number -- The point to evaluate the Var at
        :return: Number -- The number x itself
        """
        return x

    def deriv(self, x: Union[bool, Number]) -> Number:
        """Evaluate the derivative of this variable.

        `x` is a boolean indicator variable
            True (or non-zero) if this variable is being differentiated
            False (or zero) if this variable is not being differentiated

        :param x: bool | Number -- Whether the derivative is being taken with
            respect to this variable
        :return: int -- 1 or 0
        """
        if x:
            return 1
        else:
            return 0

    @property
    def vars(self):
        return [self]

    def __str__(self):
        return self.name
        
    def __call__(self, *args, **kwargs):
        return self.eval(*args)

    def __add__(self, other):
        return sd.add(self, other)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        return sd.sub(self, other)

    def __rsub__(self, other):
        return sd.sub(other, self)

    def __mul__(self, other):
        return sd.mul(self, other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __div__(self, other):
        return sd.div(self, other)

    def __rdiv__(self, other):
        return sd.div(other, self)

    def __pow__(self, power):
        return sd.pow(self, power)

    def __rpow__(self, base):
        return sd.pow(base, self)


class Expression(Var):
    def __init__(self, parent1, parent2, operation, varlist=None):
        """
        Initialize an Expression.

        :param parent1: First parent Expression
        :param parent2: Second parent Expression
        :param operation: Operation to combine the two parents
        :param varlist: Varlist
            Must be in the same order in which numbers will be passed in upon
            evaluation or differentiation of the Expression
        """
        super().__init__('f')
        self.parent1 = parent1
        self.parent2 = parent2
        self.parents = [self.parent1, self.parent2]
        self.operation = operation
        if varlist is None:
            self._vars = self._get_parent_vars(self.parent1)
            self._vars += [v for v in self._get_parent_vars(self.parent2) if v not in self._vars]
        else:
            self._vars = varlist
        self.matched_vars = self._match_vars_to_parents()

    def set_vars(self, varlist):
        self._vars = varlist
        self.matched_vars = self._match_vars_to_parents()

    @property
    def vars(self):
        return self._vars

    @vars.setter
    def vars(self, vars):
        self._vars = vars

    def _match_vars_to_parents(self):
        """Matches variables to parent1 and parent2
        :return: list[tuple] -- Mapping of vars -> parent Expression objects
        """
        matched_vars = {}
        for var in self.vars:
            parents_of_var = []
            for parent in self.parents:
                if var in self._get_parent_vars(parent):
                    parents_of_var.append(parent)
            matched_vars.update({var: parents_of_var})
        return matched_vars

    def eval(self, *args):
        """Evaluate this Expression at the specified point

        TODO: Deal with unary operations

        :param args: tuple of values to evaluate the Expression at
        :return: Result (length depends on dimensionality of co-domain)
        """
        if self.parent2 is None:
            return self._unary_eval(*args)
        else:
            return self._binary_eval(*args)


    def deriv(self, *args, mode='forward'):
        """Differentiate this Expression at the specified point.

        Currently just runs forward mode.

        :param args: tuple -- values to evaluate the Expression at
        :param mode: str -- Whether to run in forward or reverse mode
            (possible options: {'forward', 'reverse', 'auto'})
        :return: tuple(Number) | Number -- Result (length depends on dimensionality of co-domain)
        """
        p1_args, p2_args = self._parse_args(*args)
        res = []
        for var in self.vars:
            res.append(self.operation.deriv(self._eval_parent(self.parent1, *p1_args), # Evaluate and store once
                                            self._deriv_parent(self.parent1, var, *p1_args),
                                            self._eval_parent(self.parent2, *p2_args),
                                            self._deriv_parent(self.parent2, var, *p2_args)))
        if len(res) == 1:
            return res[0]
        else:
            return tuple(res)

    def _unary_eval(self, *args):
        return self.operation.eval(self._eval_parent(self.parent1, *args))

    def _binary_eval(self, *args):
        p1_args, p2_args = self._parse_args(*args)
        return self.operation.eval(self._eval_parent(self.parent1, *p1_args), self._eval_parent(self.parent2, *p2_args))

    def _get_input_args(self, parent, *args):
        """Parse the arguments in terms of the ordering for the parent

        :param parent: Parent Expression to be evaluated
        :param args: Arguments in order of self.vars
        :return: list[Var]
        """
        if not isinstance(parent, Var):
            return []
        input_args = [args[self.vars.index(parent_var)] for parent_var in parent.vars]
        return input_args

    def _check_input_length(self, *args):
        """Check that the input length matches this function's domain dimensionality.

        :param args: Input arguments
        :return: None

        :raises: AssertionError
        """
        assert len(args) == len(self.vars), \
            f'Input length does not match dimension of Expression domain ({len(args)}, {len(self.vars)})'

    def _parse_args(self, *args):
        """Check input length and parse arguments in correct order for each parent.

        :param args: tuple[Numeric] -- Arguments to be parsed
        :return: (tuple[Numeric], tuple[Numeric]) -- p1_args and p2_args
        """
        self._check_input_length(*args)
        p1_args = self._get_input_args(self.parent1, *args)
        p2_args = self._get_input_args(self.parent2, *args)
        return p1_args, p2_args

    @staticmethod
    def _get_parent_vars(parent: Union[Var, Number, None]):
        """Get the vars for given parent

        :param parent: Var | Number | None -- The parent of interest
        :return: list[Var]
        """
        if parent is None or isinstance(parent, Number):
            return []
        elif isinstance(parent, Var):
            return [parent]
        else:
            return parent.vars[:]

    @staticmethod
    def _eval_parent(parent: Union[Var, Number], *args) -> Number:
        """Evaluate a parent at `args`, checking if the parent is None or a Number

        :param parent: Var | Number | None -- The parent to evaluate
        :return: Number
        """
        if isinstance(parent, Number):
            return parent
        else:
            return parent(*args)

    @staticmethod
    def _deriv_parent(parent: Union[Var, Number], var: Var, *args) -> Number:
        """Evaluate derivative of a parent at `args`, checking if the parent is a Number

        :param parent: The parent of interest
        :param var: Var -- Variable with respect to which the derivative is
            being taken
        :param args: Point to differentiate parent at
        :return: Number
        """
        if isinstance(parent, Number):
            return 0
        else:
            if var in parent.vars:
                return parent.deriv(*args)
            else:
                return 0

    def __call__(self, *args, **kwargs):
        return self.eval(*args)

    def __str__(self):
        # TODO: Make this more informative
        return f'{str(self.operation)}: ({str(self.parent1)}, {str(self.parent2)})'
