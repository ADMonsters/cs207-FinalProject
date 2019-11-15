import numpy as np

from superdiff import expression as ex
from superdiff import operations as ops

a, b = 2, 3
x, y = ex.Var('x'), ex.Var('y')
f = ex.Expression(x, y, ops.add, [x, y])

print(f._parse_args(1, 3))
print(f.eval(1, 3))