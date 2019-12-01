"""
test_expression_multivar.py

Testing multivariate autodiff and vectorized variable
"""
import pytest
import numpy as np
import superdiff as sd
from superdiff import make_expression
from superdiff.expression import *
import math

from unittest import TestCase as tc

def test_Exp_multivar():
    x = Var('x')
    y = Var('y')
    
    # f = x - y
    f = make_expression(x - y * 2, vars = [x,y])
    assert f.eval(0,8) ==  -16, 'Expression evaluation error.'
    assert f.deriv(0,8, var = x) == 1, 'Expression partial derivative error.'
    assert f.deriv(0,8, var = y) == -2, 'Expression partial derivative error.'
    
def test_Exp_eval():
    x = Var('x')
    y = Var('y')
    z = Var('z')
    
    # f = [-1,3] + x
    f = make_expression([1,3] + x, vars = [x])
    assert f.eval([2,4]) ==  [3,7], 'Expression evaluation error.'
    
    try:
        f.eval(4)
    except TypeError :
        pass
    except:
        raise Exception('Did not raise error when variable has wrong dimension.')
    
    # f = x - y
    f = make_expression(x - y, vars = [x,y])
    assert f.eval([ [2,4], [-1,-3] ]) ==  [3,7], 'Expression evaluation error.'
    
    try:
        f.eval(4)
    except TypeError :
        pass
    except:
        raise Exception('Did not raise error when eval parameter has wrong type of arguments, not a list')
    
    # ???
    try:
        f.eval([4])
    except TypeError :
        pass
    except:
        raise Exception('Did not raise error when eval parameter has wrong type of arguments, not a vector')
    

    try:
        f.eval([4,5])
    except TypeError :
        pass
    except:
        raise Exception('Did not raise error when eval parameter has wrong type of arguments, not a vector')
        
    try:
        f.eval([ [4,5] ])
    except TypeError :
        pass
    except:
        raise Exception('Did not raise error when eval parameter has wrong number of arguments, not list of lists')
        
        
    
def test_Exp_deriv():
    x = Var('x')
    
    # f = [-1,3] + x
    f = make_expression([-1,3] + x, vars = [x])
    assert f.deriv(2) ==  1, 'Expression derivative error.'
    assert f.deriv(0) ==  1, 'Expression derivative error.'
    
test_Exp_multivar()