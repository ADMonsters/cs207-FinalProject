"""
expression.py

Classes:
    Var
        - Base class for individual variables
    Expression
        - Inherits from Var
        - Can be combined into larger expressions
"""
from superdiff import operations as ops


class Var:
    """A Variable.

    Attributes:
        :name: str -- The common name for the variable (e.g. 'x', 'y', 'x1')

    Methods:
        eval () -> Number -- Evaluate the variable for a given input (always return the number itself)

    """
    def __init__(self, name):
        self.vars = []
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
        return ops.add.(self, other)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        return ops.sub(self, other)

    def __rsub__(self, other):
        return ops.sub(other, self)

    def __mul__(self, other):
        return ops.mul(self, other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __div__(self, other):
        return ops.div(self, other)

    def __rdiv__(self, other):
        return ops.div(other, self)

    def __pow__(self, power):
        return ops.pow(self, power)

    def __rpow__(self, base):
        return ops.pow(base, self)


class Expression(Var):
    def __init__(self, parent1, parent2, operation, varlist):
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
        self.vars = varlist
        self.matched_vars = self._match_vars_to_parents()

    def set_vars(self, varlist):
        self.vars = varlist
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

        TODO: Deal with unary operations

        :param args: tuple of values to evaluate the Expression at
        :return: Result (length depends on dimensionality of co-domain)
        """
        p1_args, p2_args = self._parse_args(*args)
        return self.operation(self.parent1(*p1_args), self.parent2(*p2_args))

    def deriv(self, *args, mode='forward'):
        """Differentiate this Expression at the specified point.

        Currently just runs forward mode.

        :param args: tuple -- values to evaluate the Expression at
        :param mode: str -- Whether to run in forward or reverse mode
            (possible options: {'forward', 'reverse', 'auto'})
        :return: Result (length depends on dimensionality of co-domain)
        """
        p1_args, p2_args = self._parse_args(*args)
        return self.operation.deriv(self.parent1.deriv(*p1_args),
                                    self.parent2.deriv(*p2_args),
                                    self.parent1(*p1_args),
                                    self.parent2(*p2_args))

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

    def _parse_args(self, *args):
        """Check input length and parse arguments in correct order for each parent.

        :param args: tuple[Numeric] -- Arguments to be parsed
        :return: (tuple[Numeric], tuple[Numeric]) -- p1_args and p2_args
        """
        self._check_input_length(*args)
        p1_args = self._get_input_args(self.parent1, *args)
        p2_args = self._get_input_args(self.parent2, *args)
        return p1_args, p2_args

    def __call__(self, *args, **kwargs):
        return self.eval(*args)

    def __str__(self):
        return self.operation.__str__(self.parent1, self.parent2)


class Scalar(Var):
    """
    A scalar variable

    Methods:
        eval() -> Number -- Return the scalar value
        deriv() -> Number -- Return the derivative value (always 0)
    """
    def __init__(self, x):
        self.x = x
        super().__init__(str(x))

    def eval(self, *args):
        return self.x

    def deriv(self, *args):
        return 0
