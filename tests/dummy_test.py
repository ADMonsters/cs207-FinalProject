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

# g = make_expression(log(x), vars=[x])

# x/2
# 2/x

# fpow = make_expression(cos(x)**2, vars=[x])
# print(fpow.deriv(np.pi/3))
# print((-2*np.cos(np.pi/3)*np.sin(np.pi/3)))
# print(fpow.deriv(np.pi))
# print((-2*np.cos(np.pi)*np.sin(np.pi)))

fv1 = make_expression(x+y, x-y, vars=[x,y])
print(fv1)
print(((np.sin(np.pi / 6) / (np.pi / 6)) + np.log(np.pi / 6)*np.cos(np.pi / 6))*(np.pi / 6)**(1/2))
print(1 / (100*np.log(10)))
