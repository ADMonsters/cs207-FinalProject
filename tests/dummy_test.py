import pytest
import numpy as np

from superdiff.operations import *
from superdiff.expression import *
from superdiff.superdiff import *

a, b = 2, 3
x, y = Var("x"), Var("y")
# f = Expression(x, y, Add, varlist=[x,y])

# print(f.eval(1,3))

# f2 = make_expression(x+x,vars=[x])
# f3 = make_expression(pow(x,2), vars=[x])
# # f2 = Expression(x, x, Add, varlist=[x])
# print(f2.eval(1))
# print(f2.deriv(1))
# print(f._parse_args(1,3))

# g = make_expression((x+y)**2, [x,y])

x/2
2/x