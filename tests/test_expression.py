"""
test_expression.py

Testing methods in class Var and Expression
"""

import sys
sys.path.insert(1, '../superdiff/')
from superdiff import make_expression
from expression import Var
from expression import Expression
import operations as ops

def test_Var_eval():
    x = Var('x')
    assert x.eval(2) ==  2, 'Variable evaluation error.'
    assert x.eval(4) ==  4, 'Variable evaluation error.'
    return 'passed.'

def test_Var_deriv():
    x = Var('x')
    assert x.deriv(2) ==  1, 'Initial derivative of variable is not 1.'
    assert x.deriv(4) ==  1, 'Initial derivative of variable is not 1.'
    return 'passed.'
    
def test_Exp_parents():
    x = Var('x')
    y = Var('y')
    f = Expression(x, y, ops.add, [x,y])
    assert f.parent1 == x , 'Parent1 does not match.'
    assert f.parent2 == y , 'Parent1 does not match.'
    assert f.parents == [x,y] , 'Parent1 does not match.'
    return 'passed'

def test_Exp_eval():
    f = Expression(x, y, ops.add, [x,y])
    assert f.eval(2,4) ==  6, 'Expression evaluation error.'
    return 'passed'

x = Var('x')
y = Var('y')

f = make_expression(2+x, vars = [x])

# Var needs .vars attribute or check if Expression is Var for the last single Var
# Also what to do with numbers like f = 2*x, 2 does not have varlist
#f = Expression(x, y, ops.add, [x,y])
print(f)

# start testing
#print('Test variable evaluation:', test_Var_eval())
#print('Test variable derivative:', test_Var_deriv())

#print('Test expression parents:', test_Exp_parents())
print('Test expression evaluation:', test_Exp_eval())


