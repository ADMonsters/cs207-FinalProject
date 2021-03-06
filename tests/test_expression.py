"""
test_expression.py

Testing methods in class Var and Expression
"""
import pytest
import numpy as np
import superjacob as sd
from superjacob import make_expression
from superjacob.expression import *
import math


def test_Var_eval():
    x = Var('x')
    assert x.eval(2) ==  2, 'Variable evaluation error.'
    assert x.eval(0) ==  0, 'Variable evaluation error.'

def test_Var_deriv():
    x = Var('x')
    assert x.deriv(2) ==  1, 'Initial derivative of variable is not 1.'
    assert x.deriv(0) ==  1, 'Initial derivative of variable is not 1.'
    
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
    f = make_expression(2 * sd.sin(x), vars = [x])
    assert np.abs( f.eval(2) - (2 * np.sin(2) )  ) < 1e-7, 'Expression evaluation error.'
    assert np.abs( f.eval(4) - (2 * np.sin(4) )  ) < 1e-7, 'Expression evaluation error.'
    
    # f = cos(x) + tan(x) * 2
    f = make_expression(sd.cos(x) + sd.tan(x) * 2, vars = [x])
    assert np.abs( f.eval(np.pi) - (np.cos(np.pi) + np.tan(np.pi) * 2 )  ) < 1e-7, 'Expression evaluation error.'
    assert np.abs( f.eval(0) - (np.cos(0) + np.tan(0) * 2 )  ) < 1e-7, 'Expression evaluation error.'
    
    # f = 2 - log(x)
    f = make_expression(2 - sd.log(x,np.e), vars = [x])
    assert np.abs( f.eval(8) - (2 - np.log(8) )  ) < 1e-7, 'Expression evaluation error.'
    assert np.abs( f.eval(4) - (2 - np.log(4) )  ) < 1e-7, 'Expression evaluation error.'
    
    # f = 2 / exp(x)
    f = make_expression(2/sd.exp(x), vars = [x])
    assert np.abs( f.eval(4) - 2/np.exp(4) ) < 1e-7, 'Expression evaluation error.'
    assert np.abs( f.eval(10) -  2/np.exp(10) ) < 1e-7, 'Expression evaluation error.'
    
    # f = 2^x - sec(x)
    f = make_expression(sd.pow(2,x) - sd.sec(x), vars = [x])
    assert np.abs( f.eval(np.pi) - (math.pow(2,np.pi) - 1/np.cos(np.pi)) ) < 1e-7, 'Expression evaluation error.'
    assert np.abs( f.eval(-np.pi) - (math.pow(2,-np.pi) - 1/np.cos(-np.pi)) ) < 1e-7, 'Expression evaluation error.'
    
    # f = csc(x) - cot(x)
    f = make_expression(sd.csc(x) - sd.cot(x), vars = [x])
    assert np.abs( f.eval(np.pi/2) - (1/np.sin(np.pi/2) - 1/np.tan(np.pi/2)) ) < 1e-7, 'Expression evaluation error.'
    assert np.abs( f.eval(-np.pi/2) - (1/np.sin(-np.pi/2) - 1/np.tan(-np.pi/2)) ) < 1e-7, 'Expression evaluation error.'

    

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
    f = make_expression(2 * sd.sin(x), vars = [x])
    assert np.abs( f.deriv(2) - ( 2*np.cos(2))  ) < 1e-7, 'Expression derivative error.'
    assert np.abs( f.deriv(-2) - ( 2*np.cos(-2))  ) < 1e-7, 'Expression derivative error.'
    
    
    # f = cos(x) + tan(x) * 2
    f = make_expression(sd.cos(x) + sd.tan(x) * 2, vars = [x])
    assert np.abs( f.deriv(np.pi) - ( 2*(1/np.cos(np.pi))**2 - np.sin(np.pi))  ) < 1e-7, 'Expression derivative error.'
    assert np.abs( f.deriv(-np.pi) - (2*(1/np.cos(-np.pi))**2 - np.sin(-np.pi))  ) < 1e-7, 'Expression derivative error.'
    

    # f = 2 - log(x)
    f = make_expression(2 - sd.log(x, np.e), vars = [x])
    assert np.abs( f.deriv(4) - ( -1/4)) < 1e-7, 'Expression derivative error.'
    assert np.abs( f.deriv(8) - ( -1/8)) < 1e-7, 'Expression derivative error.'
    
     # f = 2 / exp(x)
    f = make_expression(2 / sd.exp(x), vars = [x])
    assert math.floor(np.abs( f.deriv(4) - ( -2*np.exp(-4))  )) < 1e-7, 'Expression derivative error.'
    assert np.abs( f.deriv(0) - ( -2*np.exp(0)) ) < 1e-7,  'Expression derivative error.'
    
    # f = 2^x - sec(x)
    f = make_expression(sd.pow(2,x) - sd.sec(x), vars = [x])
    assert np.abs( f.deriv(np.pi) - (math.pow(2,np.pi)*np.log(2) - np.tan(np.pi) * 1/np.cos(np.pi)) ) < 1e-7, 'Expression derivative error.'
    assert np.abs( f.deriv(-np.pi) - (math.pow(2,-np.pi)*np.log(2) - np.tan(-np.pi) * 1/np.cos(-np.pi)) ) < 1e-7, 'Expression derivative error.'

    # f = csc(x) - cot(x)
    f = make_expression(sd.csc(x) - sd.cot(x), vars = [x])
    assert np.abs( f.deriv(np.pi/2) - (1/np.sin(np.pi/2)*(1/np.sin(np.pi/2) - 1/np.tan(np.pi/2) )) ) < 1e-7, 'Expression derivative error.'
    assert np.abs( f.deriv(-np.pi/2) - (1/np.sin(-np.pi/2)*(1/np.sin(-np.pi/2) - 1/np.tan(-np.pi/2) )) ) < 1e-7, 'Expression derivative error.'
