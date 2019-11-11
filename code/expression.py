"""
expression.py

Classes:
    Var
        - Base class for individual variables
    Expression
        - Inherits from Var
        - Can be combined into larger expressions
"""


class Var:
    """A Variable.

    Attributes:
        :name: str -- The common name for the variable (e.g. 'x', 'y', 'x1')

    Methods:
        eval () -> Number -- Evaluate the variable for a given input (always return the number itself)

    """
    def __init__(self, name):
        self.name = name

    def eval(self, x):
        """
        Evaluate the variable at x (identity function)

        :param x: Number -- The point to evaluate the Var at
        :return: Number -- The number x itself
        """
        return x

    def deriv(self, x):
        """
        Evaluate the derivative at x (returns 1 always)

        :param x: Number -- The point to differentiate the Var at
        :return: int -- Always returns 1
        """
        return 1

    def __str__(self):
        return self.name

    def __add__(self, other):
        pass

    def __radd__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __rsub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __rmul__(self, other):
        pass

    def __div__(self, other):
        pass

    def __rdiv__(self, other):
        pass

    def __mod__(self, other):
        pass

    def __rmod__(self, other):
        pass

    def __pow__(self, power, modulo=None):
        pass

    def __rpow__(self, other):
        pass


class Expression:
    def __init__(self, parent1, parent2, operation, vars):
        """
        Initialize an Expression.

        :param parent1: First parent Expression
        :param parent2: Second parent Expression
        :param operation: Operation to combine the two parents
        :param vars: Varlist
            Must be in the same order in which numbers will be passed in upon
            evaluation or differentiation of the Expression
        """
        self.parent1 = parent1
        self.parent2 = parent2
        self.parents = [self.parent1, self.parent2]
        self.operation = operation
        self.vars = vars
        self.matched_vars = self._match_vars_to_parents()

    def _match_vars_to_parents(self):
        """Matches variables to parent1 and parent2
        :return: list[tuple] -- Mapping of vars -> parent Expression objects
        """
        matched_vars = []
        for var in self.vars:
            parents_of_var = []
            for parent in self.parents:
                if var in parent.vars:
                    parents_of_var.append(parent)
            matched_vars.append((var, parents_of_var))
        return matched_vars

    def eval(self, *args):
        """Evaluate this Expression at the specified point

        :param args: tuple of values to evaluate the Expression at
        :return: Result (length depends on dimensionality of co-domain)
        """
        self._check_input_length(*args)
        p1_args = self._get_input_args(self.parent1, *args)
        p2_args = self._get_input_args(self.parent2, *args)

        return self.operation(self.parent1(*p1_args), self.parent2(*p2_args))

    def deriv(self, *args):
        """Differentiate this Expression at the specified point

        :param args: tuple -- values to evaluate the Expression at
        :return: Result (length depends on dimensionality of co-domain)
        """
        pass

    def _get_input_args(self, parent, *args):
        """Parse the arguments in terms of the ordering for the parent

        :param parent: Parent Expression to be evaluated
        :param args: Arguments in order of self.vars
        :return: list[Var]
        """
        input_args = [args[self.vars.index(parent_var)] for parent_var in parent.vars]
        return input_args

    def _check_input_length(self, *args):
        """Check that the input length matches this function's domain dimensionality.

        :param args: Input arguments
        :return: None

        :raises: AssertionError
        """
        assert len(args) == len(self.vars), \
            f'Input length does not match dimension of Expression domain ({len(args)}, ({len(self.vars)})'

    def __call__(self, *args, **kwargs):
        return self.eval(*args)
