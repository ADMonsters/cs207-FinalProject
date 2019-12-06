"""
test_expression_multivar.py

Testing multivariate autodiff and vectorized variable
"""
import pytest
import numpy as np
import superjacob as sd
from superjacob import make_expression
from superjacob.expression import *
import math


def test_Exp_multivar():
    ''' Checking multivariate functions with scalar input. '''
    
    x = Var('x')
    y = Var('y')
    
    # f = x - y
    f = make_expression(x - y * 2, vars = [x,y])
    assert f.eval(0,8) ==  -16, 'Expression evaluation error.'
    assert f.deriv(0,8, var = x) == 1, 'Expression partial derivative error.'
    assert f.deriv(0,8, var = y) == -2, 'Expression partial derivative error.'
    assert (f.deriv(0,8) == np.array([1,-2])).all, 'Expression partial derivative error.'
    
def test_Exp_eval():
    ''' Checking eval method in class Expression with vectorized inputs. '''
    x = Var('x')
    y = Var('y')
    
    # f = x - y
    f = make_expression(x-y, x+y, vars = [x,y])
    assert (f.eval(2, 4) ==  np.array([-2,6]) ).all(), 'Expression evaluation error.'
    
#    # x is R2, y is R1
#    xval = np.array([2,4])
#    yval = 1
#    assert (f.eval(xval, yval) ==  np.array([1,3]) ).all(), 'Expression evaluation error.'
#    # x is R2, y is R2
#    xval = np.array([2,4])
#    yval = np.array([2,4])
#    assert (f.eval(xval, yval) ==  np.array([0,0]) ).all(), 'Expression evaluation error.'
#    #x is R2, y is R4, should raise error
#    xval = np.array([2,4])
#    yval = np.array([2,4,0,0])
#    with pytest.raises(ValueError):
#        f.eval(xval, yval)
#    
#    # Should raise error when wrong number of arguments were provided
#    with pytest.raises(AssertionError):
#        f.eval(4)
#    
#    # Should raise error when parameter is a length-one array
#    with pytest.raises(AssertionError):
#        f.eval([4],[4,5])
#    
test_Exp_eval()

#def test_Exp_deriv_arguments():
#    ''' Checking deriv method in class Expression with vectorized inputs. 
#        The test cases check the arguments passed in for deriv method. '''
#    x = Var('x')
#    y = Var('y')
#    # f = 2x - y, x is R2, y is R1
#    f = make_expression(2 * x - y, vars = [x,y])
#    
#    with pytest.raises(AssertionError):
#        f.deriv(4, var = x)
#        
#    with pytest.raises(AssertionError):
#        f.deriv(4,[4,5], var = x)
#        
#    with pytest.raises(AssertionError):
#        f.deriv([4],[4,5], var = x)
#        
#test_Exp_deriv_arguments()  

def test_Exp_deriv_forward():
    ''' Checking deriv method in class Expression with vectorized inputs. 
        The test cases check the derivation value with forward mode. '''

    x = Var('x')
    y = Var('y')
    
    # f = 2x - y, x is R2, y is R1
    f = make_expression(2 * x - y, vars = [x,y])
    #print(f.deriv(val, mode='reverse', var = x))
    assert f.deriv(2,4, mode='forward', var = x) ==  2 , 'Expression derivation error.'
    assert f.deriv(2,4, mode='forward', var = y) ==  -1, 'Expression derivation error.'
    assert (f.deriv(2,4, mode='forward') ==  np.array([2,-1]) ).all(), 'Expression derivation error.'
    
    
    f = make_expression(x-y, x+y, vars = [x,y])
    assert (f.deriv(2, 4, mode='forward', var = x) ==  [1,1]).all, 'Expression derivation error.'
    assert (f.deriv(2, 4, mode='forward', var = y) ==  [-1,1]).all, 'Expression derivation error.'
    assert (f.deriv(2, 4, mode='forward') ==  [1,1]).all, 'Expression derivation error.'
    
    
    # f = 2x - y, x is R2, y is R1
    # TODO: sd.sum()
    # sd.dot()
    #f = make_expression(sd.sum(x) - y, vars = [x,y])
    
test_Exp_deriv_forward()
def test_Exp_deriv_reverse():
    ''' Checking deriv method in class Expression with vectorized inputs. 
        The test cases check the derivation value with forward mode. '''
    x = Var('x')
    y = Var('y')
    
    # f = 2x - y, x is R2, y is R1
    f = make_expression(2 * x - y, vars = [x,y])
    #print(f.deriv(2,4, mode='reverse', var = x))
    assert f.deriv(2,4, mode='reverse', var = x) ==  2 , 'Expression derivation error.'
    assert f.deriv(2,4, mode='reverse', var = y) ==  -1, 'Expression derivation error.'
    assert (f.deriv(2,4, mode='reverse') ==  np.array([2,-1]) ).all(), 'Expression derivation error.'
    
    f = make_expression(x-y, x+y, vars = [x,y])
    assert (f.deriv(2, 4, mode='reverse', var = x) ==  [1,1]).all, 'Expression derivation error.'
    assert (f.deriv(2, 4, mode='reverse', var = y) ==  [-1,1]).all, 'Expression derivation error.'
    assert (f.deriv(2, 4, mode='reverse') ==  [1,1]).all, 'Expression derivation error.'
    
#test_Exp_deriv_reverse()