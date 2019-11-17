"""
test_expression.py

Testing methods in class Var and Expression
"""
import numpy as np
from superdiff import make_expression
from superdiff.expression import *
from superdiff import operations as ops

def test_Var_eval():
    x = Var('x')
    assert x.eval(2) ==  2, 'Variable evaluation error.'
    assert x.eval(4) ==  4, 'Variable evaluation error.'

def test_Var_deriv():
    x = Var('x')
    assert x.deriv(2) ==  1, 'Initial derivative of variable is not 1.'
    assert x.deriv(4) ==  1, 'Initial derivative of variable is not 1.'
    
def test_Exp_parents():
    x = Var('x')
    y = Var('y')
    f = make_expression( x+y , vars = [x,y])
    assert f.parent1 == x , 'Parent1 does not match.'
    assert f.parent2 == y , 'Parent2 does not match.'
    assert f.parents == [x,y] , 'Parents does not match.'

def test_Exp_eval():
    x = Var('x')
    f = make_expression(2 + x, vars = [x])
    assert f.eval(2) ==  4, 'Expression evaluation error.'
    assert f.eval(4) ==  6, 'Expression evaluation error.'
    
    # f = 2 + 2x
    f = make_expression(2 + 2 * x, vars = [x])
    assert f.eval(2) ==  6, 'Expression evaluation error.'
    assert f.eval(-4) ==  -6, 'Expression evaluation error.'
    
    # f = 2*sin(x)
    f = make_expression(2 * ops.sin(x), vars = [x])
    assert f.eval(2) ==  4, 'Expression evaluation error.'
    assert f.eval(-4) ==  8, 'Expression evaluation error.'
    
    # f = cos(x) + tan(x) * 2
    f = make_expression(ops.cos(x) + ops.tan(x) * 2, vars = [x])
    assert np.abs( f.eval(np.pi) - (np.cos(np.pi) + np.tan(np.pi) * 2 )  ) < 1e-7, 'Expression evaluation error.'
    assert np.abs( f.eval(0) - (np.cos(0) + np.tan(0) * 2 )  ) < 1e-7, 'Expression evaluation error.'
    
    # f = 2 - log(x)
    f = make_expression(2 - ops.log(x), vars = [x])
    assert np.abs( f.eval(8) - (2 - np.log(8) )  ) < 1e-7, 'Expression evaluation error.'
    assert np.abs( f.eval(4) - (2 - np.log(4) )  ) < 1e-7, 'Expression evaluation error.'
    
    # f = 2 / exp(x)
    f = make_expression(2 / ops.exp(x), vars = [x])
    assert np.abs( f.eval(4) - 2/np.log(4) ) < 1e-7, 'Expression evaluation error.'
    assert np.abs( f.eval(10) - 2/np.log(10) ) < 1e-7, 'Expression evaluation error.'
    
    

def test_Exp_deriv():
    x = Var('x')
    
    # f = 2 + x
    f = make_expression(2 + x, vars = [x])
    assert f.deriv(2) ==  1, 'Expression derivative error.'
    assert f.deriv(0) ==  1, 'Expression derivative error.'
    
    # f = 2 + 2x
    f = make_expression(2 + 2 * x, vars = [x])
    assert f.deriv(4) ==  2, 'Expression derivative error.'
    assert f.deriv(0) ==  2, 'Expression derivative error.'
    
    # f = 2 * sin(x)
    f = make_expression(2 * ops.sin(x), vars = [x])
    assert np.abs( f.deriv(2) - ( 2*np.cos(2))  ) < 1e-7, 'Expression derivative error.'
    assert np.abs( f.deriv(-2) - ( 2*np.cos(-2))  ) < 1e-7, 'Expression derivative error.'
    
    
    # f = cos(x) + tan(x) * 2
    f = make_expression(ops.cos(x) + ops.tan(x) * 2, vars = [x])
    assert np.abs( f.deriv(np.pi) - ( 2*(1/np.cos(np.pi))**2 - np.sin(np.pi))  ) < 1e-7, 'Expression derivative error.'
    assert np.abs( f.deriv(-np.pi) - (2*(1/np.cos(-np.pi))**2 - np.sin(-np.pi))  ) < 1e-7, 'Expression derivative error.'
    
    
    # f = 2 - log(x)
    f = make_expression(2 - ops.log(x), vars = [x])
    assert np.abs( f.deriv(4) - ( -1/4)) < 1e-7, 'Expression derivative error.'
    assert np.abs( f.deriv(8) - ( -1/8)) < 1e-7, 'Expression derivative error.'
    
     # f = 2 / exp(x)
    f = make_expression(2 / ops.exp(x), vars = [x])
    assert np.abs( f.deriv(4) - ( -2*np.exp(-4))  ) < 1e-7, 'Expression derivative error.'
    assert np.abs( f.deriv(0) - ( -2*np.exp(0)) ) < 1e-7,  'Expression derivative error.'
    
    

x = Var('x')
y = Var('y')
#scalar_2 = Scalar(2)
f = make_expression(2+x, vars = [x])

# Var needs .vars attribute or check if Expression is Var for the last single Var
# Also what to do with numbers like f = 2*x, 2 does not have varlist
#f = Expression(x, y, ops.add, [x,y])
print(f)



